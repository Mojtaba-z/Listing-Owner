import base64
import io
import json
import random

import bigjson
from PIL import Image
from dotwiz import DotWiz  # -> imported for dotting access to dictionary in python


# d = {'hey': {'so': [{'this': {'is': {'pretty': {'cool': True}}}}]}}
#
# dw = DotWiz(d)
# ✫(hey=✫(so=[✫(this=✫(is=✫(pretty={'cool'})))]))
# assert dw.hey.so[0].this['is'].pretty.cool == dm.hey.so[0].this['is'].pretty.cool


def calculate_b64_size(b64string):
    return (len(b64string) * 3) / 4 - b64string.count('=', -2)


def is_valid_base64_image(image_string):
    # checking valid base64 image string
    try:
        image = base64.b64decode(image_string)
        img = Image.open(io.BytesIO(image))
    except Exception:
        raise Exception('file is not valid base64 image')
    # end of check base64 image string

    # checking image format I want to support
    if img.format.lower() in ["jpg", "jpeg", "png"]:

        # if you need to check image dimension
        width, height = img.size
        if width < 800 and height < 800:
            return True
        else:
            raise Exception(
                'image size exceeded, width and height must be less than 800 pixels')
        # end of checking dimentions

    else:
        raise Exception('Image is not valid, only \'base64\' image (jpg, jpeg, png) is valid')
    # end of checking image format


def gen_code() -> int:
    base_code = 100000
    code = random.randint(10000, 99999)
    code += base_code
    return code


def delete_multiple_keys_from_dict(keys, dictionary):
    for key in keys:
        del dictionary[key]
    return dictionary


def delete_list_keys_from_dict(dic, keys):
    unwanted = set(keys) - set(dic)
    for unwanted_key in unwanted:
        del dic[unwanted_key]
    return dic


def remove_nested_keys(dictionary, keys_to_remove):
    for key in keys_to_remove:
        if key in dictionary:
            del dictionary[key]

    for value in dictionary.values():
        if isinstance(value, dict):
            remove_nested_keys(value, keys_to_remove)

    return dictionary


def scrub(obj, bad_key=None):
    if isinstance(obj, dict):
        # the call to `list` is useless for py2 but makes
        # the code py2/py3 compatible
        for key in list(obj.keys()):
            if key == bad_key:
                del obj[key]
            else:
                scrub(obj[key], bad_key)
    elif isinstance(obj, list):
        for i in reversed(range(len(obj))):
            if obj[i] == bad_key:
                del obj[i]
            else:
                scrub(obj[i], bad_key)

    else:
        # neither a dict nor a list, do nothing
        pass


def write_json_to_file(js, filename):
    json_object = json.dumps(js, indent=4)
    with open(filename, "w") as f:
        f.write(json_object)


def read_json_from_file(filename):
    with open(filename, "rb") as f:
        file = bigjson.load(f)
    return file

