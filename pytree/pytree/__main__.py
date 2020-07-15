# __main__.py

import os

from utils import get_indentation, clean_terminal

ONE_PART = "│"
TWO_PARTS = "└──"
THREE_PARTS = "├──"


def main():
    cwd = os.getcwd()

    for dirpath, _, filenames in os.walk(cwd):
        depth = dirpath.replace(cwd, "", 1).count(os.sep)

        indentation = get_indentation(depth)
        inner_indentation = get_indentation(depth)

        bname = os.path.basename(dirpath)

        print(f"{indentation}{bname}")

        for fn in filenames:
            print(f"{inner_indentation}{fn}")


if __name__ == "__main__":
    clean_terminal()
    main()
