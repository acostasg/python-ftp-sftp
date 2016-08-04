import unittest
import injectionContainer
from unittest.mock import MagicMock
import logging
import os
import yaml
from config \
    import ConfigApp as config_app
import strategy.requestParams as Request
from strategy.dummys.injectedContainerDummy import ContainerMock


class TestSecure(unittest.TestCase):
    # TODO
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

        config_app.Handle(os, yaml_mock)

        injectionContainer.Container.update(
            ContainerMock().container()
        )


if __name__ == '__main__':
    unittest.main()
