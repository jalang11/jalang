import os
from setuptools import setup, find_packages

# Important constants
NAME = "smtp"
VERSION = "3.0.1"
REPO = "https://github.com/jalang11/jalang/"
DESC = """smtp is a security-oriented research framework for
conducting bruteforce attacks against a multitude of protocols and services"""

# Main setup method
setup(
    name = NAME,
    version = VERSION,
    author = "jalanG",
    author_email = 'jalang@hush.ai',
    description = DESC,
    license = "GPLv3",
    url=REPO,
    download_url='{}/archive/v{}'.format(REPO, VERSION),
    keywords=[
        'passwords',
        'cryptography',
        'systems',
        'secret-sharing',
        'privacy',
    ],
    packages = find_packages(exclude=('tests',)),
    entry_points = {
        'console_scripts': [
            'smtp=smtp.__main__:main'
        ],
    },
    install_requires=[
        'paramiko',
        'selenium',
        'xmpppy',
        'requests'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ]
)
