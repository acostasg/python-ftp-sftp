import fnmatch
import ftplib
import logging
import os
import sys
from unittest.mock \
    import MagicMock

import pysftp
import yaml

import config.ConfigApp \
    as configApp
from shared.Singleton import SingleMetaClass


class ContainerMock(metaclass=SingleMetaClass):
    pass

    def __init__(
            self
    ):
        ftp_mock = ftplib
        ftp_mock.connect = MagicMock(return_value=0)
        ftp_mock.login = MagicMock(return_value=0)
        ftp_mock.cwd = MagicMock(return_value=0)
        ftp_mock.storlines = MagicMock(return_value=0)
        ftp_mock.quit = MagicMock(return_value=0)
        ftp_mock.close = MagicMock(return_value=0)
        ftp_mock.put = MagicMock(return_value=0)

        pysftp_mock = pysftp
        pysftp_mock.Connection = MagicMock(return_value=ftp_mock)
        pysftp_mock.put = MagicMock(return_value=0)
        pysftp_mock.storlines = MagicMock(return_value=0)

        fnmatch_mock = fnmatch
        fnmatch_mock.fnmatch = MagicMock(return_value=True)

        os_mock = os
        os_mock.listdir = MagicMock(return_value={'tests'})

        yaml_mock = yaml
        yaml_mock.load = MagicMock(return_value={
            'secure': {'host': 'host', 'username': 'username', 'secret': 'secret', 'port': 20},
            'unsercure': {'host': 'host', 'username': '', 'secret': '', 'port': 20},
            'local': {'path': 'path', 'prefix': 'prefix', 'pattern': ''},
            'remote': {'path': 'path'},
            'strategy': {'default': 1},
        })

        sys_mock = sys
        sys_mock.warn = MagicMock(return_value=0)

        config_mock = configApp
        config_mock.warn = MagicMock(return_value=0)

        logger_mock = logging
        logger_mock.warning = MagicMock(return_value=0)
        logger_mock.info = MagicMock(return_value=0)
        logger_mock.basicConfig = MagicMock(return_value=0)

        open_mock = MagicMock(return_value='tests')

        self.__container = {
            'ftplib.ftp': ftp_mock,
            'pysftp': pysftp_mock,
            'fnmatch': fnmatch_mock,
            'os': os_mock,
            'yaml': yaml_mock,
            'sys': sys_mock,
            'config_app': config_mock,
            'logger': logger_mock,
            'open': open_mock
        }
        pass

    def container(self):
        return self.__container
