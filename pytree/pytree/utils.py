import platform
from shutil import get_terminal_size
import os


def get_indentation(depth, is_dir, spaces=3):
    depth = depth if (depth == 0 or not is_dir) else depth - 1
    return " " * spaces * (depth)


def clean_terminal():
    os_name = platform.system()

    if os_name == "Darwin" or os_name == "Linux":
        os.system("clear")
    elif os_name == "Windows":
        os.system("cls")
    else:
        print("\n" * get_terminal_size().lines, end="")

