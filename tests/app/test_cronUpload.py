import unittest

import injectionContainer

from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestUnsecure(unittest.TestCase):
    def test_cronUpload(self):

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        import cronUpload