# -*- coding: utf-8 -*-

from setuptools import setup


def read(filename):
    with open(filename) as f:
        return f.read()

setup(
    name = 'ebucks',
    version = '0.1.0',
    author = 'Konrad Blum',
    author_email = 'konrad@kblum.com',
    packages = ['ebucks',],
    url = 'https://github.com/kblum/ebucks',
    license = read('LICENSE'),
    description = 'Python module for scraping balance from eBucks website.',
    long_description = read('README.md'),
    keywords = 'ebucks',
    install_requires = [
        'beautifulsoup4==4.3.2',
    ],
)
