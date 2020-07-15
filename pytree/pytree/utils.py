import platform
from shutil import get_terminal_size
import os


def get_indentation(depth, is_dir, spaces=4):
    depth = depth if (depth == 0 or not is_dir) else depth - 1

    return " " * spaces * depth


def tree_wo_indentation_lines():
    cwd = os.getcwd()

    for dirpath, _, filenames in os.walk(cwd):
        depth = dirpath.replace(cwd, "", 1).count(os.sep)

        indentation = get_indentation(depth, True)
        inner_indentation = get_indentation(depth, False)

        bname = os.path.basename(dirpath)

        extra_space = " " if depth > 0 else ""

        print(f"{indentation}{extra_space}{bname}")

        for fn in filenames:
            print(f"{inner_indentation} {fn}")


def clean_terminal():
    os_name = platform.system()

    if os_name == "Darwin" or os_name == "Linux":
        os.system("clear")
    elif os_name == "Windows":
        os.system("cls")
    else:
        print("\n" * get_terminal_size().lines, end="")

