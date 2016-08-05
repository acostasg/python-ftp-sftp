import unittest

import injectionContainer

from upload.strategy.dummys.injectedContainerDummy import ContainerMock


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