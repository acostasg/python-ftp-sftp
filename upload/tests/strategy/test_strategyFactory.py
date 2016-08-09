import unittest

import injectionContainer
import upload.strategy.requestParams as Request
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


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

        request = Request.RequestParams()
        request.connectionInfo = {'host': '', 'port': '', 'username': '', 'password': ''}

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        strategy = Factory.Strategy(1)
        self.assertTrue(strategy.upload(request))

        strategy = Factory.Strategy(2)
        self.assertTrue(strategy.upload(request))


if __name__ == '__main__':
    unittest.main()
