import boto3
import logging
from botocore.exceptions import ClientError
from django.http import HttpResponse
from PIL import Image
import io
import base64


def connect():
    logging.basicConfig(level=logging.INFO)

    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url='https://s3.ir-thr-at1.arvanstorage.ir',
            aws_access_key_id='7634268d-d870-4dc6-93e2-bbbfafb6c1a7',
            aws_secret_access_key='4b170bdb9424900775dcae28e879fe534d0dc0d1'
        )
    except Exception as exc:
        logging.info(exc)
    return s3_resource


def upload_object(image_data, bucket_name, object_name):
    resource_connect = connect()
    s3_resource = resource_connect
    bucket = s3_resource.Bucket(bucket_name)
    buffer = io.BytesIO()
    imgdata = base64.b64decode(image_data)
    img = Image.open(io.BytesIO(imgdata))
    new_img = img.resize((500, 500))  # x, y
    new_img.save(buffer, format="PNG")
    img_b64 = base64.b64encode(buffer.getvalue())
    with open(object_name, "wb") as fh:
        fh.write(base64.standard_b64decode(img_b64))
        # base64.standard_b64decode(image_data)
    with open(object_name, "rb") as fh:
        bucket.put_object(
            ACL='public-read',
            Body=fh,
            Key=object_name
        )
