import logging
import unittest
from unittest.mock import MagicMock

import injectionContainer
import strategy.requestParams as Request
from strategy.dummys.injectedContainerDummy import ContainerMock


class TestStrategyFactory(unittest.TestCase):
    """
    Class test for strategy factory class
    """

    def test_strategy_factory(self):
        """
        test cases strategy factory
        :return:
        """
        import strategy.strategyFactory as Factory

        logger_mock = logging
        logger_mock.warning = MagicMock(return_value=0)
        logger_mock.info = MagicMock(return_value=0)

        request = Request.RequestParams()
        request.connectionInfo = {'host': '', 'port': '', 'username': '', 'password': ''}

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        strategy = Factory.Strategy(1, logger_mock)
        self.assertTrue(strategy.upload(request))

        strategy = Factory.Strategy(2, logger_mock)
        self.assertTrue(strategy.upload(request))
