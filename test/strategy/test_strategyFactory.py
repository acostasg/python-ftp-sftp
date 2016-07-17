import unittest

from unittest.mock \
    import patch
import strategy.RequestParams as Request
import injectionContainer
from injectionContainerDummy \
    import ContainerMock as ContainerMock


class TestSecure(unittest.TestCase):
    @patch('logging')
    def test_secure_upload(self, mock_logging):
        import strategy.StrategyFactory as Factory

        request = Request.RequestParams()

        injectionContainer.Container.update(
            ContainerMock().contxainer()
        )

        strategy = Factory.Strategy(1, mock_logging)
        self.assertTrue(strategy.upload(request))


if __name__ == '__main__':
    unittest.main()
