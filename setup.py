#!/usr/bin/env python

from distutils.core import setup

with open('README.md') as f:
    docs = f.read()

setup(
    name='pyconomic',
    version='0.1.0',
    description='Abstraction for e-conomic.com API',
    author='Mikkel Jans',
    author_email='mikkeljans@gmail.com',
    url='',
    packages=['pyconomic'],
    install_requires=["suds"],
    long_description=docs
)