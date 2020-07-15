# __main__.py

from pathlib import Path
from utils import clean_terminal, tree_wo_indentation_lines


SPACE = " " * 4
ONE_PART = "│   "
TWO_PARTS = "└── "
THREE_PARTS = "├── "


def tree_generator(root, pre_indentation_line):
    """
    Based on: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
    """
    file_and_dir_names = sorted(root.iterdir())
    indentation_lines = [THREE_PARTS] * (len(file_and_dir_names) - 1) + [TWO_PARTS]

    # Using `zip` (instead of comparing each element to the last one on a list,
    # for example) is important to abstract the possible names of files and folders
    # from which indentation lines they should have.
    branches = zip(indentation_lines, file_and_dir_names)

    for indentation_line, path in branches:
        yield pre_indentation_line + indentation_line + path.name

        if path.is_dir():
            new_pre_indentation_line = (
                ONE_PART if indentation_line == THREE_PARTS else SPACE
            )
            yield from tree_generator(
                path, pre_indentation_line + new_pre_indentation_line
            )


def get_root_representation(root, root_representation):
    if root_representation == "name":
        return root.name
    elif root_representation == "dot":
        return "."
    else:
        return ""


def main(root, pre_indentation_line, root_representation):
    print(get_root_representation(root, root_representation))
    for branch in tree_generator(root, ""):
        print(branch)


if __name__ == "__main__":
    clean_terminal()
    main(Path.cwd(), "", "dot")
    # tree_wo_indentation_lines()
