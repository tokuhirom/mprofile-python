# -*- coding: utf-8 -*-
import sys
from setuptools import setup


REQUIRES = [
    'MySQL-python',
]

if sys.version_info < (2, 7):
    REQUIRES.append('argparse')

setup(
    name='mprofile',
    version='0.1.0',
    description='Python port of mprofile(MySQL profiler)',
    platforms=['linux', 'osx', 'unix', 'win32'],
    packages=['mprofile'],
    author='Tokuhiro Matsuno',
    url='https://github.com/tokuhirom/mprofile-python',
    license='MIT',
    keywords=['mysql', 'profile'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
    ],
    include_package_data=True,
    install_requires=REQUIRES,
    tests_require=[
        'pytest',
        'pytest-pep8',
        'pytest-flakes',
        'tox',
        'mock'],
    entry_points={
        'console_scripts': [
            'mpdump = mprofile.mpdump:main',
            'mpfilter = mprofile.mpfilter:main',
            'mpreport = mprofile.mpreport:main',
        ],
    },
)
