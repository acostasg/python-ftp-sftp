import os
import unittest

import mock

import upload.config.config_app as config
import upload.injectionContainer as injectionContainer
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestConfigApp(unittest.TestCase):
    """
    Class test for config App
    """

    def test_config_app(self):
        """
        test configAapp class
        :return:
        """
        import upload.strategy.strategyFactory as strategyFactory

        yaml_mock = mock.Mock()
        yaml_mock.load = mock.Mock(return_value={
            'secure': {'host': 'host', 'username': 'username', 'secret': 'secret', 'port': 20},
            'unsercure': {'host': 'host', 'username': '', 'secret': '', 'port': 20},
            'local': {'path': 'path', 'prefix': 'prefix', 'pattern': ''},
            'remote': {'path': 'path'},
            'strategy': {'default': 1},
        })

        os_mock = mock.Mock()
        os_mock.path.dirname = 'test'

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        config_app = config.Handle(os, yaml_mock)

        config_unsercure = config_app.get_request(strategyFactory.Strategy.CONST_UNSECURE)
        self.addTypeEqualityFunc('requestParams', config_unsercure)

        config_sercure = config_app.get_request(strategyFactory.Strategy.CONST_SECURE)
        self.addTypeEqualityFunc('requestParams', config_sercure)

        config_sercure = config_app.get_strategy()
        self.assertEqual(config_sercure, strategyFactory.Strategy.CONST_SECURE)

        self.assertRaises(Exception, config_app.get_request)

        with self.assertRaises(Exception):
            config_app.get_request(999)


if __name__ == '__main__':
    unittest.main()
