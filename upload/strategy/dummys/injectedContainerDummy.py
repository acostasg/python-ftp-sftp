import mock

from shared.Singleton import SingleMetaClass
from strategy import requestParams


class ContainerMock(metaclass=SingleMetaClass):
    """
    Dummy container for testing
    """
    pass

    def __init__(
            self
    ):
        ftp_mock = self.get_ftp_mock()

        ftp_mock_base = self.get_ftp_mock_base(ftp_mock)

        pysftp_mock = self.get_pysftp_mock(ftp_mock)

        fnmatch_mock = self.get_fnmatch_mock()

        os_mock = self.get_os_mock()

        yaml_mock = self.get_yaml_mock()

        sys_mock = mock.Mock()

        strategy_mock = self.get_strategy_mock()

        request_params = self.get_request_params_vo()

        config_mock = self.get_config_mock(request_params)

        handle_mock = self.get_handle_mock(config_mock)

        logger_mock = self.get_logger_mock()

        open_mock = mock.Mock(return_value='tests')

        self.__container = {
            'ftplib.ftp': ftp_mock_base,
            'pysftp': pysftp_mock,
            'fnmatch': fnmatch_mock,
            'os': os_mock,
            'yaml': yaml_mock,
            'sys': sys_mock,
            'config_app': handle_mock,
            'logger': logger_mock,
            'open': open_mock,
            'strategy.secure': strategy_mock,
            'strategy.unsecure': strategy_mock
        }
        pass

    @staticmethod
    def get_logger_mock():
        logger_mock = mock.Mock()
        logger_mock.warning = mock.Mock(return_value=0)
        logger_mock.info = mock.Mock(return_value=0)
        logger_mock.basicConfig = mock.Mock(return_value=0)
        return logger_mock

    @staticmethod
    def get_handle_mock(config_mock):
        handle_mock = mock.Mock()
        handle_mock.Handle = mock.Mock(return_value=config_mock)
        return handle_mock

    @staticmethod
    def get_config_mock(request_params):
        config_mock = mock.Mock()
        config_mock.get_strategy = mock.Mock(return_value=1)
        config_mock.get_connections = mock.Mock(return_value={})
        config_mock.get_request = mock.Mock(return_value=request_params)
        return config_mock

    @staticmethod
    def get_request_params_vo():
        request_params = requestParams.RequestParams()
        request_params.connectionInfo = {'host': 'host', 'username': 'username', 'secret': 'secret', 'port': 20}
        request_params.localPath = 'localPath'
        request_params.pattern = '*.pattern'
        request_params.prefix = 'test_report'
        request_params.remotePath = 'remotePath'
        return request_params

    @staticmethod
    def get_strategy_mock():
        strategy_mock = mock.Mock()
        strategy_mock.upload = mock.Mock(return_value=True)
        return strategy_mock

    @staticmethod
    def get_yaml_mock():
        yaml_mock = mock.Mock()
        yaml_mock.load = mock.Mock(return_value={
            'secure': {'host': 'host', 'username': 'username', 'secret': 'secret', 'port': 20},
            'unsercure': {'host': 'host', 'username': '', 'secret': '', 'port': 20},
            'local': {'path': 'path', 'prefix': 'prefix', 'pattern': ''},
            'remote': {'path': 'path'},
            'strategy': {'default': 1},
        })
        return yaml_mock

    @staticmethod
    def get_os_mock():
        os_mock = mock.Mock()
        os_mock.listdir = mock.Mock(return_value={'tests'})
        return os_mock

    @staticmethod
    def get_fnmatch_mock():
        fnmatch_mock = mock.Mock()
        fnmatch_mock.fnmatch = mock.Mock(return_value=True)
        return fnmatch_mock

    @staticmethod
    def get_pysftp_mock(ftp_mock):
        pysftp_mock = mock.Mock()
        pysftp_mock.Connection = mock.Mock(return_value=ftp_mock)
        pysftp_mock.put = mock.Mock(return_value=0)
        pysftp_mock.storlines = mock.Mock(return_value=0)
        return pysftp_mock

    @staticmethod
    def get_ftp_mock_base(ftp_mock):
        ftp_mock_base = mock.Mock()
        ftp_mock_base.FTP = mock.Mock(return_value=ftp_mock)
        return ftp_mock_base

    @staticmethod
    def get_ftp_mock():
        ftp_mock = mock.Mock()
        ftp_mock.connect = mock.Mock(return_value=0)
        ftp_mock.login = mock.Mock(return_value=0)
        ftp_mock.cwd = mock.Mock(return_value=0)
        ftp_mock.storlines = mock.Mock(return_value=0)
        ftp_mock.quit = mock.Mock(return_value=0)
        ftp_mock.close = mock.Mock(return_value=0)
        ftp_mock.put = mock.Mock(return_value=0)
        return ftp_mock

    def container(self):
        return self.__container
