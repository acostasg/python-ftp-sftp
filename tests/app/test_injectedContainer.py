import unittest

import injectionContainer
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestRequestParams(unittest.TestCase):
    def test_injection_container(self):

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        self.assertEqual(
            injectionContainer.Container.get_container(),
            ContainerMock().container()
        )