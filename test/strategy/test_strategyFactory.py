import unittest

import injectionContainer
import strategy.requestParams as Request
import logging
from unittest.mock import MagicMock
from strategy.dummys.injectedContainerDummy import ContainerMock


class TestSecure(unittest.TestCase):

    def test_strategy_factory(self):
        import strategy.strategyFactory as Factory

        logger_mock = logging
        logger_mock.warning = MagicMock(return_value=0)
        logger_mock.info = MagicMock(return_value=0)

        request = Request.RequestParams()
        request.connectionInfo = {'host': ''}

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        strategy = Factory.Strategy(1, logger_mock)
        self.assertTrue(strategy.upload(request))


if __name__ == '__main__':
    unittest.main()
