#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

readme = open('README.rst').read()

def get_version():
    try:
        import subprocess
        p = subprocess.Popen('hg id -t', shell=True, stdout=subprocess.PIPE)
        tag = p.stdout.read()[1:].strip()
        return tag
    except:
        return 'dev'

setup(
    name='demosp',
    version=get_version(),
    description="""MPASS Demo SP""",
    long_description=readme,
    author='Haltu',
    packages=find_packages(),
    include_package_data=True,
    license="Haltu",
    zip_safe=False,
    keywords='demosp',
    install_requires=[
    ],
)

# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2
