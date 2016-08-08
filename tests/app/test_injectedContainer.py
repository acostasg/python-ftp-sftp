import unittest

import injectionContainer
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestInjectedContainer(unittest.TestCase):
    def test_injection_container(self):
        injectionContainer.Container.update(
            ContainerMock().container()
        )

        self.assertEqual(
            injectionContainer.Container.get_container(),
            ContainerMock().container()
        )

    def test_injection_container_with_error(self):
        with self.assertRaises(Exception):
            injectionContainer.Container.dependency('failed')
