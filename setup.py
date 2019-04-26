#!/usr/bin/env python

from distutils.core import setup
from glob import glob
from macpath import splitext, basename

from setuptools import find_packages

setup(name='Project',
      description='Python Distribution Utilities',
      version='1.0',
      author='Haoran Peng',
      packages=find_packages('Split'),
      package_dir={'': 'Split'},
      py_modules=[splitext(basename(path))[0] for path in glob('Split/*.py')],
     )
