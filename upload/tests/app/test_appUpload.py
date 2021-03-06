import unittest

import mock

import upload.injectionContainer as injectionContainer
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

        from upload import appUpload

        result = appUpload.execute(
            injectionContainer.Container.dependency('logger'),
            injectionContainer.Container.dependency('config_app'),
            injectionContainer.Container.dependency('os'),
            injectionContainer.Container.dependency('yaml')
        )

        self.assertTrue(result)

    def test_app_upload_config_error(self):
        """
        Test case for upload file exception
        """
        injectionContainer.Container.update(
            ContainerMock().container()
        )

        from upload import appUpload

        config_mock = mock.Mock()
        config_mock.Handle = Exception('Corrupt configuration files')

        with self.assertRaises(Exception):
            appUpload.execute(
                injectionContainer.Container.dependency('logger'),
                config_mock,
                injectionContainer.Container.dependency('os'),
                injectionContainer.Container.dependency('yaml')
            )

    def test_app_upload_execute_error(self):
        """
        Test case for upload file exception
        """
        injectionContainer.Container.update(
            ContainerMock().container()
        )

        from upload import appUpload

        config_mock = mock.Mock()
        config_mock.get_strategy = Exception('Corrupt configuration files')

        with self.assertRaises(Exception):
            appUpload.execute(
                injectionContainer.Container.dependency('logger'),
                config_mock,
                injectionContainer.Container.dependency('os'),
                injectionContainer.Container.dependency('yaml')
            )


if __name__ == '__main__':
    unittest.main()
