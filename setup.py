#!/usr/bin/env python

import os

from distutils.core import setup

docs = ''
if os.path.exists('README.md'):
    with open('README.md') as f:
        docs = f.read()

setup(
    name='pyconomic',
    version='0.1.1',
    description='Abstraction for e-conomic.com API',
    author='Mikkel Jans',
    author_email='mikkeljans@gmail.com',
    url='https://github.com/mikkeljans/pyconomic',
    packages=['pyconomic'],
    long_description=docs
)