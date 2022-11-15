# Source: https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html
# https://webcolors.readthedocs.io/en/1.12/
# https://github.com/feedzai/feedzai-altair-theme/blob/master/feedzai_altair_theme/tokens.py#L98

from feedzai_altair_theme.tokens import COLOR_PRIMITIVES
from scipy.spatial import KDTree
from webcolors import CSS3_NAMES_TO_HEX, hex_to_rgb


def find_closest_named_color(color):
    names = list(CSS3_NAMES_TO_HEX.keys())
    rgb_values = [hex_to_rgb(color) for color in CSS3_NAMES_TO_HEX.values()]

    kdt_db = KDTree(rgb_values)
    _, index = kdt_db.query(color)

    return names[index]


def find_closest_color(color, candidate_colors, candidate_names):
    kdt_db = KDTree(candidate_colors)
    _, index = kdt_db.query(color)

    return candidate_names[index]


if __name__ == "__main__":
    color_palette = COLOR_PRIMITIVES["teal"]
    candidate_names = list(color_palette.keys())
    candidate_colors = [hex_to_rgb(color) for color in color_palette.values()]
    # print(candidate_names, candidate_colors)

    reference_color = (20, 152, 181)

    closest_color = find_closest_color(
        reference_color, candidate_colors, candidate_names
    )
    print(
        closest_color,
        color_palette[closest_color],
        hex_to_rgb(color_palette[closest_color]),
    )

    print(find_closest_named_color(reference_color))
    # print(find_closest_named_color((190, 53, 25)))
