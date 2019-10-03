#!/usr/bin/env python

import setuptools

with open('README.md', 'r') as fh:
    longDescription = fh.read()

setuptools.setup(name='pymonad',
    version='0.1.0',
    description='Some monadic value holders for Python',
    long_description=longDescription,
    long_description_content_type='text/markdown',
    author='Luc Sorel-Giffo',
    url='https://github.com/lucsorel/pymonad',
    packages=list(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)