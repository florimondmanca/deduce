# setuptools is a fully-featured, actively-maintained, and stable
# library designed to facilitate packaging Python projects.
# setup.py is the build script for setuptools.
# It tells setuptools about your package (such as the name and version)
# as well as which code files to include.
# https://packaging.python.org/tutorials/packaging-projects/
# https://setuptools.readthedocs.io/en/latest/

import ast
import io
import re
import os
import sys
from setuptools import find_packages, setup, Command

DEPENDENCIES = []
EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


def get_version() -> str:
    main_file = os.path.join(CURDIR, "colon", "main.py")
    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
    with open(main_file, "r", encoding="utf8") as f:
        match = _version_re.search(f.read())
        version = match.group("version") if match is not None else '"unknown"'
    return str(ast.literal_eval(version))


setup(
    name="colon",
    version=get_version(),
    author="Florimond Manca",
    author_email="florimond.manca@gmail.com",
    description="Type hints-powered conversion",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bocadilloproject/colon",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=[],
    scripts=[],
    zip_safe=False,
    install_requires=DEPENDENCIES,
    python_requires=">=3.6",
    # license and classifier list:
    # https://pypi.org/pypi?%%3Aaction=list_classifiers
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
