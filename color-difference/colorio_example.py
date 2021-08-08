import colorio

# import numpy as np

ILLUMINANT: str = "D50"
# ILLUMINANT: str = "D65"


def main():
    hsl = colorio.cs.HSL()

    # Default white point: D65 (`whitepoints_cie1931["D65"]`, observer -> 2)
    # Color.js white point: D50 (https://colorjs.io/docs/spaces.html)
    # https://github.com/LeaVerou/color.js/blob/549e0d0e38a6e0d0375b49889caf0ab494613f8e/src/color.js#L955
    # colorjs_d50 = (
    #     np.array([0.3457 / 0.3585, 1.00000, (1.0 - 0.3457 - 0.3585) / 0.3585]) * 100
    # )
    # whitepoint = colorjs_d50
    whitepoint = colorio.illuminants.whitepoints_cie1931[ILLUMINANT]

    lab = colorio.cs.CIELAB(whitepoint=whitepoint)

    # https://github.com/nschloe/colorio/blob/v0.7.5/src/colorio/cs/_hsl.py#L44
    orange = hsl.to_rgb1((30, 1, 0.5))
    yellow = hsl.to_rgb1((50, 1, 0.5))

    # print(orange)
    # print(yellow)

    # https://github.com/nschloe/colorio/blob/v0.7.5/src/colorio/cs/_cielab.py
    # https://github.com/nschloe/colorio/blob/v0.7.5/src/colorio/cs/_color_space.py

    orange_lab = lab.from_rgb1(orange)
    yellow_lab = lab.from_rgb1(yellow)

    print(orange_lab)
    # print(yellow_lab)

    print("Orange-Yellow:", colorio.diff.cie76(orange_lab, yellow_lab))


if __name__ == "__main__":
    main()
