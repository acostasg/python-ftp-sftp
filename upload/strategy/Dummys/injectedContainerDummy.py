from unittest.mock \
    import patch


@patch(
    'ftplib',
    'pysftp',
    'fnmatch',
    'os',
    'yaml',
    'sys',
    'ConfigApp'
)
class ContainerMock:
    def __init__(
            self,
            ftp_mock,
            pysftp_mock,
            fnmatch_mock,
            os_mock,
            yaml_mock,
            sys_mock,
            config_app,
            logger
    ):
        self.ftp_mock = ftp_mock
        self.pysftp_mock = pysftp_mock
        self.fnmatch_mock = fnmatch_mock
        self.os_mock = os_mock
        self.yaml_mock = yaml_mock
        self.sys_mock = sys_mock
        self.config_mock = config_app
        self.logger_mock = logger

        self.__container = {
            'ftplib.ftp': self.ftp_mock,
            'pysftp': self.pysftp_mock,
            'fnmatch': self.fnmatch_mock,
            'os': self.os_mock,
            'yaml': self.yaml_mock,
            'sys': self.sys_mock,
            'config_app': self.config_mock,
            'logger': self.logger_mock
        }
        pass

    def container(self):
        return self.__container
