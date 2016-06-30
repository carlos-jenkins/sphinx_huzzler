#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Carlos Jenkins
# Copyright (c) 2013 Michael Dowling
#
# This software may be modified and distributed under the terms
# of the MIT license. See the LICENSE file for details.

from setuptools import setup, find_packages


def read(filename):
    """
    Read a file relative to setup.py location.
    """
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, filename)) as fd:
        return fd.read()


def find_version(filename):
    """
    Find package version in file.
    """
    import re
    content = read(filename)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def find_requirements(filename):
    """
    Find requirements in file.
    """
    import string
    content = read(filename)
    requirements = []
    for line in content.splitlines():
        line = line.strip()
        if line and line[:1] in string.ascii_letters:
            requirements.append(line)
    return requirements


setup(
    name='sphinx_huzzler',
    version=find_version('lib/sphinx_huzzler/__init__.py'),
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    package_data={
        'sphinx_huzzler': [
            'sphinx_huzzler/*.{}'.format(ext)
            for ext in ['conf', 'html']
        ] + [
            'sphinx_huzzler/static/*.{}'.format(ext)
            for ext in ['js', 'map', 'css_t']
        ] + [
            'sphinx_huzzler/static/js/*.{}'.format(ext)
            for ext in ['js']
        ] + [
            'sphinx_huzzler/static/css/*.{}'.format(ext)
            for ext in ['css']
        ] + [
            'sphinx_huzzler/static/fonts/*.{}'.format(ext)
            for ext in ['woff']
        ]
    },

    # Dependencies
    install_requires=find_requirements('requirements.txt'),

    # Metadata
    author='Carlos Jenkins',
    author_email='carlos@jenkins.co.cr',
    description=(
        'Huzzler is Guzzler with Huntr.'
    ),
    long_description=read('README.rst'),
    url='https://sphinx_huzzler.readthedocs.org/',
    keywords='sphinx_huzzler',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
