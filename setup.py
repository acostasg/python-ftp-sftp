# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='UploadFiles ftp/sftp',

    test_suite='nose.collector',
    tests_require=['nose'],

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.9.0',

    description='Upload files from directory secure/unsercure project',
    long_description='Upload files from directory with pattern secure and unsercure strategy',

    # The project's main homepage.
    url='https://github.com/acostasg/upload',

    # Author details
    author='Albert',
    author_email='git@lescases.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='upload files from directory with pattern secure and unsercure strategy',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["upload"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['importlib', 'pyyaml', 'pysftp', 'mock'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,tests]
    extras_require={
        'dev': ['check-manifest'],
        'tests': ['coverage', 'unittest', 'mock', 'patch'],
    }
)