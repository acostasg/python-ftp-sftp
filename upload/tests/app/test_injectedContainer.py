import unittest

import upload.injectionContainer as injectionContainer
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestInjectedContainer(unittest.TestCase):
    """
    Class test for injected dependency container
    """

    def test_injection_container(self):
        """
        Test case for injected container class
        """
        injectionContainer.Container.update({
            'ftplib.ftp': None,
            'pysftp': None,
            'fnmatch': None,
            'os': None,
            'yaml': None,
            'sys': None,
            'config_app': None,
            'logger': None,
            'strategy.secure': None,
            'strategy.unsecure': None,
            'open': None,
            'get_opt': None
        })

        open_test = injectionContainer.Container.dependency('open')

        self.assertIsNotNone(open_test)

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

if __name__ == '__main__':
    unittest.main()
