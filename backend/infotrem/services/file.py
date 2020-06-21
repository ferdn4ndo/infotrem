import hashlib
import os
import pathlib
import shutil
import time

import magic
import requests

from django.core.files.uploadedfile import InMemoryUploadedFile


def get_mime_type(file_or_path) -> str:
    return magic.from_file(file_or_path, mime=True)


def check_if_media(file_path) -> bool:
    mime_type = get_mime_type(file_path)

    if mime_type is None:
        return False

    mime_start = mime_type.split('/')[0]
    return mime_start == 'video' or mime_start == 'image'


def generate_file_hash(filepath: str):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_temp_path():
    temp_folder = os.environ['TEMP_FOLDER'] if 'TEMP_FOLDER' in os.environ else '/temp'

    if not os.path.isdir(temp_folder):
        pathlib.Path(temp_folder).mkdir(parents=True, exist_ok=True)

    return temp_folder


def get_random_file_temp_path() -> str:
    file_path = os.path.join(get_temp_path(), "{:.4f}.tmp".format(time.time()))
    while os.path.isfile(file_path):
        file_path = os.path.join(get_temp_path(), "{:.4f}.tmp".format(time.time()))
    return file_path


def save_from_memory(memory_file: InMemoryUploadedFile) -> str:
    local_filename = get_random_file_temp_path()
    with open(local_filename, 'wb') as file:
        shutil.copyfileobj(memory_file.read, file)
    return local_filename


# def check_file_mime_type(temp_file_path):
#     mime_type = get_mime_type(temp_file_path)
#     if mime_type not in ALLOWED_MIME_TYPES:
#         os.remove(temp_file_path)
#         raise InvalidFileMimeType("Mime type '{}' not allowed!".format(mime_type))
#
#
#
#
#
# def check_file_size_limit(temp_file_path):
#     file_size = len(open(temp_file_path).read())
#     if file_size > MAX_UPLOAD_SIZE:
#         os.remove(temp_file_path)
#         raise FileOversizeLimit("Exceeded limit of {} bytes!".format(MAX_UPLOAD_SIZE))
#
#
# def get_new_unique_file_identifier(module_folder: str) -> str:
#     file_uuid = str(uuid.uuid4())
#     s3 = get_s3_client()
#
#     exists = True
#     while exists:
#         s3_path = os.path.join(os.environ['AWS_S3_FOLDER'], module_folder, file_uuid)
#         try:
#             s3.head_object(Bucket=os.environ['AWS_S3_BUCKET'], Key=s3_path)
#         except ClientError as e:
#             if e.response['ResponseMetadata']['HTTPStatusCode'] == 404:
#                 exists = False
#             else:
#                 logging.error(e)
#
#     return file_uuid
#
#
# def get_local_file_temp_path(file_uuid: str, module_folder: str) -> str:
#     return os.path.join(os.environ['TEMP_FOLDER'], module_folder, file_uuid)
#
#
# def upload_raw_data(file_data, storage_file: StorageFile):
#     s3 = get_s3_client()
#     s3.put_object(Bucket=os.environ['AWS_S3_BUCKET'], Key=storage_file.storage_filepath, Body=file_data)
#     return create_expirable_download_url(file_data)
#
#
# def upload_from_url(url: str, file_uuid: str, module_folder: str) -> str:
#     if not check_if_url_is_downloadable(url):
#         raise PreConditionFailed("The url is not downloadable")
#
#
#
#     file_data = get_content_from_url(url)
#     return upload_raw_data(file_data=file_data, file_uuid=file_uuid, module_folder=module_folder)
#
#
# def save_posted_file_to_temp(temp_post_file: TemporaryUploadedFile) -> str:
#     temp_filename = os.path.join(os.environ['TEMP_PATH'], '{}_{}'.format(uuid.uuid4(), int(time.time())))
#     file_data = temp_post_file.read()
#     with open(temp_filename, 'wb') as temp_file:
#         temp_file.write(file_data)
#     return temp_filename
#
#
# def create_storage_file_from_temp(temp_file_path: str, user: User, original_filename: str = ''):
#     mime = get_mime_type(temp_file_path)
#     file_type = ALLOWED_MIME_TYPES[mime]
#
#     stored_file = StorageFile.objects.create(
#         file_type=file_type,
#         mime_type=mime,
#         original_filename=original_filename,
#         storage_type=StorageType.FILE_STORAGE_S3,
#         created_by=user
#     )
#
#     if file_type == FileType.TYPE_MEDIA_IMAGE:
#         sign_image(signature=stored_file.signature_key, temp_file_path=stored_file.)
#
#
# def upload_from_post(temp_post_file: TemporaryUploadedFile, user: User) -> StorageFile:
#     temp_file_path = save_posted_file_to_temp(temp_post_file)
#     check_file_size_limit(temp_file_path)
#     check_file_mime_type(temp_file_path)
#
#     stored_file = create_storage_file_from_temp(temp_file_path)
#
#
#
#     with open(temp_file_path, 'rb') as file_data:
#         storage_url = upload_raw_data(stored_file=storage_file, module_folder='uploads')
#     stored_file.raw_file_path = storage_url
#
#     # ToDo: create thumbnails
#
#     stored_file.processed = True
#     stored_file.save()
#
#     return stored_file
#
