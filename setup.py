import os

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requires = [r for r in f.read().split(os.linesep) if r]

url = "https://github.com/rugleb?tab=repositories"

packages = find_packages(include=["project"])

setup(name="test",
      version="0.0.1",
      description="test description",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url=url,
      download_url=url,
      author="Gleb Karpushkin",
      author_email="rugleb@gmail.com",
      packages=packages,
      install_requires=install_requires,
      python_requires=">=3.7",
      platforms=["macOS", "POSIX", "Windows"],
      include_package_data=True,
      zip_safe=True,
      license="MIT",
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Internet",
          "Framework :: AsyncIO",
      ])
