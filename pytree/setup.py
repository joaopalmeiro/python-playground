import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text().split()

setup(
    name="pytree",
    version="0.0.1",
    description="A simple Python package to obtain a recursive directory listing.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/joaopalmeiro/python-playground/tree/master/pytree",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    entry_points={"console_scripts": ["pytree=pytree.__main__:main",]},
)
