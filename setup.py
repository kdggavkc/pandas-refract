from setuptools import setup

import pandas_refracts
import sys


if sys.version_info[0] >= 3:
    openf = open
else:
    import codecs

    openf = codecs.open


def read(fn):
    with openf(fn, encoding="utf-8") as fp:
        return fp.read()


setup(
    name="pandas_refracts",
    version=pandas_refracts.__version__,
    description="Split a dataframe by boolean array",
    long_description=(read("README.rst")),
    url="http://github.com/nickclawrence/pandas-refract/",
    license=pandas_refracts.__license__,
    author=pandas_refracts.__author__,
    author_email="nickclawrence@gmail.com",
    py_modules=["pandas-refracts"],
    install_requires=[
        'numpy',
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
