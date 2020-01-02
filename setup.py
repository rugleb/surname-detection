import os

from setuptools import find_packages, setup

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = [
        r for r in f.read().split(os.linesep) if r
    ]

URL = "https://github.com/rugleb/surname-detection"

PACKAGES = find_packages(include=["project"])

PLATFORMS = [
    "macOS",
    "POSIX",
    "Windows",
]

CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Operating System :: OS Independent",
]

setup(
    name="surname-detection",
    version="0.0.1",
    description="Identify the word that are surname",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    download_url=URL,
    author="Gleb Karpushkin",
    author_email="rugleb@gmail.com",
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.7",
    platforms=PLATFORMS,
    include_package_data=True,
    zip_safe=True,
    license="MIT",
    classifiers=CLASSIFIERS,
)
