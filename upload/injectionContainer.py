import fnmatch
import ftplib
import logging
import os
import sys

import pysftp
import yaml

import config.ConfigApp as ConfigApp
from shared import SingletonMetaClass as Singleton


class Container:
    __metaclass__ = Singleton.SingletonMetaClass

    def __init__(self):
        pass

    __container = {
        'ftplib.ftp': ftplib.FTP(),
        'pysftp': pysftp,
        'fnmatch': fnmatch,
        'os': os,
        'yaml': yaml,
        'sys': sys,
        'config_app': ConfigApp,
        'logger': logging
    }

    @staticmethod
    def dependency(key):
        return Container.__container.get(key)

    @staticmethod
    def update(container):
        return Container.__container.update(container)
