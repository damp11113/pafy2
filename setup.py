#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for pafy.

https://github.com/damp11113/pafy2

python setup.py sdist bdist_wheel

"""

from setuptools import setup
from pafy import __version__

setup(
    name='pafy2',
    packages=['pafy2'],
    scripts=['scripts/ytdl'],
    version=__version__,
    description="Retrieve YouTube content and metadata with yt_dlp",
    keywords=["pafy2", "API", "YouTube", "youtube", "download", "video", "yt_dlp"],
    author="np1",
    author_email="damp51252@gmail.com",
    url="https://github.com/damp11113/pafy2/",
    download_url="https://github.com/damp11113/pafy2/tags",
    extras_require={
        'youtube-dl-backend': ["youtube-dl"],
        },
    include_package_data=True,
    license='LGPLv3',
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 "
        "(LGPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS 9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows XP",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Multimedia :: Sound/Audio :: Capture/Recording",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP"],
    long_description=open("README.rst").read()
)
