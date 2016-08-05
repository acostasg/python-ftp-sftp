import unittest

import injectionContainer

from strategy.dummys.injectedContainerDummy import ContainerMock


class TestUnsecure(unittest.TestCase):
    def test_cronUpload(self):

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        import cronUpload


if __name__ == '__main__':
    unittest.main()
