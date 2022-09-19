import logging
import os.path
import re
from typing import Dict, Optional, List

from PIL import Image
from PIL.ExifTags import TAGS


class PhotoExifService:
    file_path: str
    exif_data: Dict

    def __init__(self, file_path: str):
        self.file_path = file_path

        self.exif_data = self.get_image_information()

    def get_image_information(self):
        """Retrieves a dict of data about a given image file"""
        if not os.path.isfile(path=self.file_path):
            raise FileNotFoundError(f"Unable to locate file at '{self.file_path}'")

        return self.get_image_exif()

    def get_image_exif(self) -> Dict:
        ret = {}
        image = Image.open(self.file_path)
        info = image._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value

        ret['IMAGE_WIDTH'], ret['IMAGE_HEIGHT'] = image.size
        return ret

    def parse_exif_string_to_list(self, original_string: str) -> Optional[List]:
        if not re.match(r"^\(\d+,\s*\d+\)$", str(original_string)):
            return None

        return str(original_string).replace(' ', '').replace('(', '').replace(')', '').split(',')

    def get_exif_focal_length(self) -> Optional[float]:
        if 'FocalLength' not in self.exif_data:
            return None

        data_parts = self.parse_exif_string_to_list(self.exif_data['FocalLength'])
        if data_parts is None:
            logging.warning('Unable to parse focal length: {}'.format(self.exif_data['FocalLength']))

            return None

        return float(data_parts[0]) / float(data_parts[1])

    def get_exif_aperture(self) -> Optional[str]:
        if 'FNumber' not in self.exif_data:
            return None

        data_parts = self.parse_exif_string_to_list(self.exif_data['FNumber'])
        if data_parts is None:
            logging.warning('Unable to parse aperture: {}'.format(self.exif_data['FNumber']))
            return None

        return 'f/{:.1f}'.format(float(data_parts[0]) / float(data_parts[1]))

    def get_exif_exposition(self) -> Optional[str]:
        if 'ExposureTime' not in self.exif_data:
            return None

        data_parts = self.parse_exif_string_to_list(self.exif_data['ExposureTime'])
        if data_parts is None:
            logging.warning('Unable to parse exposure time: {}'.format(self.exif_data['ExposureTime']))
            return None

        return '{}/{}'.format(data_parts[0], data_parts[1])

    def get_exif_flash_fired(self) -> Optional[bool]:
        """
        Parses the "flash" value from exif do determine if it was fired.

        Possible values:
        +-------------------------------------------------------+------+----------+-------+
        |                        Status                         | Hex  |  Binary  | Fired |
        +-------------------------------------------------------+------+----------+-------+
        | No Flash                                              | 0x0  | 00000000 | No    |
        | Fired                                                 | 0x1  | 00000001 | Yes   |
        | "Fired, Return not detected"                          | 0x5  | 00000101 | Yes   |
        | "Fired, Return detected"                              | 0x7  | 00000111 | Yes   |
        | "On, Did not fire"                                    | 0x8  | 00001000 | No    |
        | "On, Fired"                                           | 0x9  | 00001001 | Yes   |
        | "On, Return not detected"                             | 0xd  | 00001011 | Yes   |
        | "On, Return detected"                                 | 0xf  | 00001111 | Yes   |
        | "Off, Did not fire"                                   | 0x10 | 00010000 | No    |
        | "Off, Did not fire, Return not detected"              | 0x14 | 00010100 | No    |
        | "Auto, Did not fire"                                  | 0x18 | 00011000 | No    |
        | "Auto, Fired"                                         | 0x19 | 00011001 | Yes   |
        | "Auto, Fired, Return not detected"                    | 0x1d | 00011101 | Yes   |
        | "Auto, Fired, Return detected"                        | 0x1f | 00011111 | Yes   |
        |  No flash function                                    | 0x20 | 00100000 | No    |
        | "Off, No flash function"                              | 0x30 | 00110000 | No    |
        | "Fired, Red-eye reduction"                            | 0x41 | 01000001 | Yes   |
        | "Fired, Red-eye reduction, Return not detected"       | 0x45 | 01000101 | Yes   |
        | "Fired, Red-eye reduction, Return detected"           | 0x47 | 01000111 | Yes   |
        | "On, Red-eye reduction"                               | 0x49 | 01001001 | Yes   |
        | "On, Red-eye reduction, Return not detected"          | 0x4d | 01001101 | Yes   |
        | "On, Red-eye reduction, Return detected"              | 0x4f | 01001111 | Yes   |
        | "Off, Red-eye reduction"                              | 0x50 | 01010000 | No    |
        | "Auto, Did not fire, Red-eye reduction"               | 0x58 | 01011000 | No    |
        | "Auto, Fired, Red-eye reduction"                      | 0x59 | 01011001 | Yes   |
        | "Auto, Fired, Red-eye reduction, Return not detected" | 0x5d | 01011101 | Yes   |
        | "Auto, Fired, Red-eye reduction, Return detected"     | 0x5f | 01011111 | Yes   |
        +-------------------------------------------------------+------+----------+-------+

        :param exif_data:
        :return: If the flash was fired, or None if the exif information is not present
        """
        if 'Flash' not in self.exif_data:
            return None

        return bool((int(self.exif_data['Flash']) & 1) > 0)


    def get_exif_orientation(self) -> Optional[Dict]:
        """
        Retrieves the orientation angle and flip flag based on the EXIF flash data
        :return:
        """
        if 'Flash' not in self.exif_data:
            return None

        flash_value = int(self.exif_data['Flash'])

        return {
            'orientation_angle': self.get_orientation_angle_from_flash_value(flash_value),
            'is_flipped': True if flash_value in [2, 4, 5, 7] else False,
        }

    @staticmethod
    def get_orientation_angle_from_flash_value(flash_value: int) -> int:
        """
        EXIF Value	Row #0 is:	    Column #0 is:

         +--------------+---------------------------------------+-------+----------+
        | EXIF Value    | Row #0 location   | Row #1 location   | Angle | Flipped  |
        +---------------+---------------------------------------+-------+----------+
        |      1        | Top               | Left side         |   0   |    NO    |
        |      2        | Top               | Right side        |   0   |   YES    |
        |      3        | Bottom            | Right side        |  180  |    NO    |
        |      4        | Bottom            | Left side         |  180  |   YES    |
        |      5        | Left side         | Top               |   90  |   YES    |
        |      6        | Right side        | Top               |   90  |    NO    |
        |      7        | Right side        | Bottom            |  270  |   YES    |
        |      8        | Left side         | Bottom            |  270  |    NO    |
        +---------------+---------------------------------------+-------+----------+

        :param flash_value: The 'Flash' value from EXIF data
        :return: The orientation angle of the photo
        """
        if flash_value in [0, 1]:
            return 0

        if flash_value in [3, 4]:
            return 180

        if flash_value in [5, 6]:
            return 90

        return 270
