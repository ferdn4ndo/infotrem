import logging
import os
import uuid
from typing import Dict

import requests
from boto3 import client
from botocore.exceptions import ClientError

from infotrem.errors import S3BucketError


def get_s3_client():
    s3 = client('s3', aws_access_key_id=os.environ['AWS_S3_ID'], aws_secret_access_key=os.environ['AWS_S3_KEY'])

    found = False
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        if bucket['Name'] == os.environ['AWS_S3_BUCKET']:
            found = True

    if not found:
        logging.error('Not seeing the s3 bucket (permissions in IAM?)')

    return s3


def get_expirable_download_url(storage_file, expiration=3600, force_download=False):
    """
    Generate a presigned URL to share an S3 object

    :param storage_file:
    :param expiration: Time in seconds for the presigned URL to remain valid
    :param force_download: if the file download should be enforced
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a pre-signed URL for the S3 object
    s3 = get_s3_client()
    try:
        return s3.generate_presigned_url(
            'get_object', Params={
                'Bucket': os.environ['AWS_S3_BUCKET'],
                'Key': storage_file.storage_file_path,
                'ResponseContentDisposition': 'inline' if not force_download else 'attachment',
                'ResponseContentType': storage_file.mime_type
            }, ExpiresIn=expiration
        )
    except ClientError as e:
        logging.error(e)
        return None


def get_new_unique_file(folder: str) -> Dict:
    file_uuid = str(uuid.uuid4())
    s3 = get_s3_client()

    exists = True
    s3_path = ""
    while exists:
        s3_path = os.path.join(os.environ['AWS_S3_FOLDER'], folder, file_uuid)
        try:
            s3.head_object(Bucket=os.environ['AWS_S3_BUCKET'], Key=s3_path)
        except ClientError as e:
            if e.response['ResponseMetadata']['HTTPStatusCode'] == 404:
                exists = False
            else:
                logging.error(e)

    return {
        "file_uuid": file_uuid,
        "remote_path": s3_path
    }


def upload_from_temp(local_path: str, remote_path: str):
    s3 = get_s3_client()
    with open(local_path, 'rb') as f:
        s3.put_object(Bucket=os.environ['AWS_S3_BUCKET'], Key=remote_path, Body=f.read())


def download_to_temp(remote_path: str, temp_path: str) -> str:
    s3 = get_s3_client()
    with open(temp_path, 'wb') as f:
        s3.download_fileobj(os.environ['AWS_S3_BUCKET'], remote_path, f)
    return temp_path


def upload_from_url(url, remote_path):
    s3 = get_s3_client()
    bucket_name = os.environ['AWS_S3_BUCKET']
    if not any([bucket.name == bucket_name for bucket in s3.buckets.all()]):
        logging.error("Unable to find bucket {} in S3 buckets list. Check IAM permissions.".format(bucket_name))
        raise S3BucketError

    # Given an Internet-accessible URL, download the image and upload it to S3,
    # without needing to persist the image to disk locally
    req_for_image = requests.get(url, stream=True)
    file_object_from_req = req_for_image.raw
    req_data = file_object_from_req.read()

    # Do the actual upload to s3
    file_uuid, storage_file_path = get_new_unique_file(os.environ['ORIGINAL_UPLOADED_FILES_FOLDER'])
    s3.Bucket(bucket_name).put_object(Key=remote_path, Body=req_data)
