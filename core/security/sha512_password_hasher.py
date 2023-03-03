import re
from collections import OrderedDict

from django.contrib.auth.hashers import BasePasswordHasher, mask_hash
from django.utils.encoding import force_str
from django.utils.crypto import constant_time_compare
from django.utils.translation import ugettext_noop as _


class CryptSHA512PasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the crypt-sha512 algorithm, with configurable rounds

    Allows the use of iterated sha512 password hashing as provided by glibc2.7+'s crypt() using $6$ salts.
    This is compatible with the password hashes in the /etc/shadow of modern Linux distros, while providing
    better security than the ancient DES-based crypt (available in Django as CryptPasswordHasher).
    """
    algorithm = "csha512"
    library = "crypt"
    rounds = 5000  # Default as of glibc2.7

    def salt(self):
        crypt = self._load_library()
        salt = crypt.mksalt(crypt.METHOD_SHA512)
        if not re.match('^\$6\$[A-Za-z0-9./]+$', salt):
            raise Exception('Unrecognized salt!? ({})'.format(salt))
        salt = '$6$rounds=' + str(self.rounds) + '$' + salt[3:]
        # The Django User.password field has max_length=128, and a b64 sha512 hash is 86 characters.
        # After considering the separating '$', this leaves 41 characters for the prefix, which is a
        # tight fit. To ensure it fits, we truncate the prefix to 41 characters, but this may lop off
        # characters from the actual salt. This is OK, as crypt(3) specifies the salt length as
        # *up to* 16.
        # However, if the prefix length exceeds 49 characters, we have to cut off more than 8 chars
        # from the salt, which would leave us with a salt shortar than 8 chars. We refuse this.
        # Assuming the "csha512" algorithm name, this leaves up to 15 chars for up to 10^15-1 rounds.
        max_len = 128 - 86 - 1 - len(self.algorithm)

        if len(salt) > max_len + 8:
            raise Exception('Hash prefix string too long, refusing to truncate salt to fewer than 8 characters.')
        return salt[:max_len]

    def encode(self, password, salt):
        crypt = self._load_library()
        # TODO: '$rounds=X' after salt?
        data = crypt.crypt(force_str(password), salt)
        return "%s%s" % (self.algorithm, data)

    def verify(self, password, encoded):
        crypt = self._load_library()
        algorithm, rest = encoded.split('$', 1)
        salt, hash = rest.rsplit('$', 1)
        salt = '$' + salt
        assert algorithm == self.algorithm
        return constant_time_compare('%s$%s' % (salt, hash), crypt.crypt(force_str(password), salt))

    def safe_summary(self, encoded):
        algorithm, prefix, *rounds, salt, hash = encoded.split('$')
        assert algorithm == self.algorithm
        if rounds:
            rounds = rounds[0].split('=')[1]
        else:
            rounds = 'default'

        return OrderedDict([
            (_('algorithm'), algorithm),
            (_('prefix'), prefix),
            (_('rounds'), rounds),
            (_('salt'), mask_hash(salt)),
            (_('hash'), mask_hash(hash)),
        ])

    def harden_runtime(self, password, encoded):
        pass
