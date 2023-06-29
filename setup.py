import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="diagnostic",

    description="Example project structure.",

    author="Camilo Rodriguez",

    packages=find_packages(),
    package_dir={"":"diagnostic"}
    long_description=read('README.md'),
)
