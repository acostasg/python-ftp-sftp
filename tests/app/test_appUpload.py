import unittest

import injectionContainer
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestAppUpload(unittest.TestCase):
    """
    Class Test for app Upload
    """

    def test_app_upload(self):
        """
        Test case for upload file
        """
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
