#!/usr/bin/python3

import setuptools

# Work around "TypeError: 'NoneType' object is not callable" 
# during `python setup.py test`
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html
import multiprocessing

with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name = 'python-dbusmock',
    version = '0.1.1',
    description = 'Mock D-Bus objects',
    long_description = readme,
    author = 'Martin Pitt',
    author_email = 'martin.pitt@ubuntu.com',
    url = 'https://launchpad.net/python-dbusmock',
    download_url = 'https://launchpad.net/python-dbusmock/+download',
    license = 'LGPL 3+',
    py_modules = ['dbusmock'],
    test_suite = 'nose.collector',

    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: BSD',
        'Operating System :: Unix',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
