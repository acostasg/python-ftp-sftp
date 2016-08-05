import os
import unittest
from unittest.mock import MagicMock

import yaml

import config.ConfigApp as ConfigApp
import injectionContainer
from strategy.dummys.injectedContainerDummy import ContainerMock


class TestSecure(unittest.TestCase):
    def test_configApp(self):
        import strategy.strategyFactory

        yaml_mock = yaml
        yaml_mock.load = MagicMock(return_value={
            'secure': {'host': 'host', 'username': 'username', 'secret': 'secret', 'port': 20},
            'unsercure': {'host': 'host', 'username': '', 'secret': '', 'port': 20},
            'local': {'path': 'path', 'prefix': 'prefix', 'pattern': ''},
            'remote': {'path': 'path'},
            'strategy': {'default': 1},
        })

        config_app = ConfigApp.Handle(os, yaml_mock)

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        config_unsercure = config_app.get_request(strategy.strategyFactory.Strategy.CONST_UNSECURE)
        self.addTypeEqualityFunc('requestParams', config_unsercure)

        config_sercure = config_app.get_request(strategy.strategyFactory.Strategy.CONST_SECURE)
        self.addTypeEqualityFunc('requestParams', config_sercure)

        config_sercure = config_app.get_strategy()
        self.assertEqual(config_sercure, strategy.strategyFactory.Strategy.CONST_SECURE)

        self.assertRaises(Exception, config_app.get_request)

        with self.assertRaises(Exception):
            config_app.get_request(999)