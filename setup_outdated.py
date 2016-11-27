#!/usr/bin/python3.5

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("analysis.pyx")
)
