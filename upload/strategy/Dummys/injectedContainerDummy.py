import fnmatch
import ftplib
import logging
import os
import sys
from unittest.mock \
    import MagicMock

import pysftp
import yaml

from config \
    import ConfigApp as configApp


class ContainerMock:
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

        pysftp_mock = pysftp
        pysftp_mock.Connection = MagicMock(return_value=ftp_mock)

        fnmatch_mock = fnmatch
        fnmatch_mock.fnmatch = MagicMock(return_value=0)

        os_mock = os
        os_mock.listdir = MagicMock(return_value={})

        yaml_mock = yaml
        yaml_mock.load = MagicMock(return_value=0)

        sys_mock = sys
        sys_mock.warn = MagicMock(return_value=0)

        config_mock = configApp
        config_mock.warn = MagicMock(return_value=0)

        logger_mock = logging
        logger_mock.warning = MagicMock(return_value=0)
        logger_mock.info = MagicMock(return_value=0)

        self.__container = {
            'ftplib.ftp': ftp_mock,
            'pysftp': pysftp_mock,
            'fnmatch': fnmatch_mock,
            'os': os_mock,
            'yaml': yaml_mock,
            'sys': sys_mock,
            'config_app': config_mock,
            'logger': logger_mock
        }
        pass

    def container(self):
        return self.__container
