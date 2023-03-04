import os
import random
import string

from core.utils.arvan import upload_object

ARVAN_USER_IMAGE_URL = 'https://fertilizer.s3.ir-thr-at1.arvanstorage.ir/'


def upload_image(req=None, field=None):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
    if req.data['user'][field] != "":
        upload_object(
            image_data=req.data['user'][field],
            bucket_name="fertilizer",
            object_name="{0}.jpg".format(str(ran))
        )
        os.remove("{0}.jpg".format(str(ran)))
        req.data['user'].pop(field)
        req.data['user'][field] = ARVAN_USER_IMAGE_URL + "{0}.jpg".format(str(ran))
    elif req.data['user'][field] == "":
        req.data['user'][field] = "empty"
    return req


def upload_listed_image(req=None, field=None):
    image_list = []
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
    if req.data['user'][field] != []:
        for item in req.data['user'][field]:
            upload_object(
                image_data=item,
                bucket_name="fertilizer",
                object_name="{0}.jpg".format(str(ran))
            )
            os.remove("{0}.jpg".format(str(ran)))
            image_list.append(ARVAN_USER_IMAGE_URL + "{0}.jpg".format(str(ran)))
        req.data['user'].pop(field)
        req.data['user'][field] = image_list
    elif req.data['user'][field] == "":
        req.data['user'][field] = "empty"
    return req
