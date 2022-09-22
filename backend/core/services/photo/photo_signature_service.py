import os.path
import os.path
import time
from shutil import copyfile
from typing import Dict, Union, IO

from stegano.exifHeader import exifHeader
from stegano.lsbset import lsbset, generators


class PhotoSignatureService:
    file_path: str

    def __init__(self, file_path: str):
        self.file_path = file_path

    def sign_image(self, signature: str, image_file_path: Union[str, IO[bytes]]):
        copied_file_path = "{}_{}.tmp".format(self.file_path, time.time())
        copyfile(self.file_path, copied_file_path)

        exifHeader.hide(input_image_file=copied_file_path, img_enc=image_file_path, secret_message=signature)
        os.remove(copied_file_path)

        secret_image = lsbset.hide(
            input_image=image_file_path,
            message=signature,
            generator=generators.fermat()
        )
        secret_image.save(image_file_path)


    def get_sign_from_image(self) -> Dict:
        signature_from_exif = exifHeader.reveal(self.file_path)
        signature_from_data = lsbset.reveal(self.file_path, generators.eratosthenes())

        return {
            'signature_from_data': signature_from_data,
            'signature_from_exif': signature_from_exif,
            'matched': signature_from_data is not None and signature_from_data == signature_from_exif
        }
