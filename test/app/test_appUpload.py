import unittest

import injectionContainer

from strategy.dummys.injectedContainerDummy import ContainerMock


class TestUnsecure(unittest.TestCase):
    def test_appUpload(self):

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        import appUpload

        appUpload.execute(
            injectionContainer.Container.dependency('logger'),
            injectionContainer.Container.dependency('config_app'),
            injectionContainer.Container.dependency('sys'),
            injectionContainer.Container.dependency('os'),
            injectionContainer.Container.dependency('yaml')
        )


if __name__ == '__main__':
    unittest.main()
