import os
import shutil
from urllib.parse import urlparse

import requests

from core.services.file.file_service import get_random_file_temp_path

INFOTREM_USER_AGENT = 'InfoTrem-CrawlerAgent/1.0.0'


def download_url(url: str) -> str:
    headers = {
        'user-agent': INFOTREM_USER_AGENT
    }

    local_filename = get_random_file_temp_path()

    with requests.get(url, headers=headers, stream=True) as req:
        with open(local_filename, 'wb') as file:
            shutil.copyfileobj(req.raw, file)

    return local_filename


def get_content_from_url(url):
    headers = {
        'user-agent': INFOTREM_USER_AGENT
    }

    response = requests.get(url, headers=headers, stream=True)
    return response.content


def check_if_url_is_downloadable(url):
    headers = {
        'user-agent': INFOTREM_USER_AGENT
    }

    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return False

    return True


def get_file_name_from_url(url):
    parser = urlparse(url)
    return os.path.basename(parser.path)
