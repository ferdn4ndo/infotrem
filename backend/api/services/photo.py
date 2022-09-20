import os
import time
from shutil import copyfile
from typing import Union, IO, Dict

from rawkit.options import WhiteBalance
from rawkit.raw import Raw
from stegano import exifHeader, lsbset
from stegano.lsbset import generators


def render_photo_from_cr2_raw_file(original_filename, dest_filename):
    with Raw(filename=original_filename) as raw:
        raw.options.white_balance = WhiteBalance(camera=False, auto=True)
        raw.save(filename=dest_filename)
    return True


def sign_image(signature: str, image_file_path: Union[str, IO[bytes]]):
    copied_file_path = "{}_{}.tmp".format(image_file_path, time.time())
    copyfile(image_file_path, copied_file_path)

    exifHeader.hide(input_image_file=copied_file_path, img_enc=image_file_path, secret_message=signature)
    os.remove(copied_file_path)

    secret_image = lsbset.hide(
        input_image=image_file_path,
        message=signature,
        generator=generators.fermat()
    )
    secret_image.save(image_file_path)


def get_sign_from_image(source_image: Union[str, IO[bytes]]) -> Dict:
    signature_from_exif = exifHeader.reveal(source_image)
    signature_from_data = lsbset.reveal("./image.png", generators.eratosthenes())

    return {
        'signature_from_data': signature_from_data,
        'signature_from_exif': signature_from_exif,
        'matched': signature_from_data is not None and signature_from_data == signature_from_data
    }
