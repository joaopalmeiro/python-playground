#!/usr/bin/env python3

__author__ = "João Palmeiro"
__version__ = "0.1.0"
__license__ = "MIT"

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


def main():
    img = Image.open("joao.jpg")
    cropped_img = crop_max_square(img)
    cropped_img.save("squared_joao.jpg", quality=95)


if __name__ == "__main__":
    main()
