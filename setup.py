#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mnowotka'

from setuptools import setup

setup(
    name='babyshortener',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'run_shortener=babyshortener.run_shortener:main']
    },
    author='Michal Nowotka',
    author_email='mmmnow@gmail.com',
    description='Simple url shortener implemented using Flask',
    url='https://github.com/mnowotka/babyshortener',
    license='MIT',
    packages=['babyshortener',
              ],
    long_description=open('README.md').read(),
    tests_require=['WebTest'],
    install_requires=['flask', 'flask_sqlalchemy'],
    package_data={
        'babyshortener': ['samples/*', 'static/*', 'tests/*'],
        },
    include_package_data=False,
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Flask',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Internet :: WWW/HTTP :: WSGI :: Server'],
    zip_safe=False,
)
