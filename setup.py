#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = ('flake8', 'black')

setup(
    name='pycharm_ext_tools',
    version='0.1.0',
    description='Flake8 and Black support for pycharm code selection',
    long_description='\n\n',
    author='Haim Daniel',
    author_email='haim.daniel@gmail.com',
    url='https://github.com/haim0n/pycharm_flake8_selection.git',
    packages=[
        'pycharm_flake8',
    ],
    package_dir={'pycharm_flake8': 'pycharm_flake8'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='pycharm_flake8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
)
