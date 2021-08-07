import numpy as np
from PIL import ImageColor
from skimage import color


def main():
    # https://pillow.readthedocs.io/en/stable/reference/ImageColor.html
    # hsl(hue, saturation%, lightness%)
    # https://coolors.co/ff8000
    orange = ImageColor.getrgb("hsl(30, 100%, 50%)")
    # https://coolors.co/ffd500
    yellow = ImageColor.getrgb("hsl(50, 100%, 50%)")
    blue = ImageColor.getrgb("hsl(230, 100%, 50%)")
    purple = ImageColor.getrgb("hsl(260, 100%, 50%)")

    # print(orange, yellow, blue, purple)

    orange_array = np.asarray(orange, dtype=np.uint8)
    orange_lab = color.rgb2lab(orange_array)

    yellow_array = np.asarray(yellow, dtype=np.uint8)
    yellow_lab = color.rgb2lab(yellow_array)

    blue_array = np.asarray(blue, dtype=np.uint8)
    blue_lab = color.rgb2lab(blue_array)

    purple_array = np.asarray(purple, dtype=np.uint8)
    purple_lab = color.rgb2lab(purple_array)

    print("Orange-Yellow:", color.deltaE_cie76(orange_lab, yellow_lab))
    print("Yellow-Blue:", color.deltaE_cie76(yellow_lab, blue_lab))
    print("Blue-Purple:", color.deltaE_cie76(blue_lab, purple_lab))


if __name__ == "__main__":
    main()
