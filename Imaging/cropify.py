#!/usr/bin/env python3

# https://github.com/docopt/docopt/blob/master/examples/naval_fate.py
# https://github.com/docopt/docopt/blob/master/examples/validation_example.py
# https://github.com/docopt/docopt/blob/master/examples/options_shortcut_example.py
"""A Python CLI to crop a square from a rectangular image.

Usage:
  cropify.py IMG
  cropify.py -h | --help
  cropify.py -v | --version

Arguments:
  IMG           path to the image to crop

Options:
  -h --help     show this help message and exit
  -v --version  show version and exit

"""

__author__ = "João Palmeiro"
__version__ = "0.1.0"
__license__ = "MIT"

from docopt import docopt
from PIL import Image


# Image object: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image
def crop_center(img: Image.Image, crop_w: int, crop_h: int) -> Image.Image:
    w, h = img.size

    # (0, 0) -> upper left corner
    left = (w - crop_w) // 2
    upper = (h - crop_h) // 2
    right = (w + crop_w) // 2
    lower = (h + crop_h) // 2

    return img.crop((left, upper, right, lower))


def crop_max_square(img: Image.Image) -> Image.Image:
    size = min(img.size)
    return crop_center(img, size, size)


def main(input_path: str) -> None:
    img = Image.open(input_path)
    cropped_img = crop_max_square(img)
    cropped_img.save("squared_joao.jpg", quality=95)


if __name__ == "__main__":
    args = docopt(__doc__, version=__version__)
    # print(args)

    main(args["IMG"])
