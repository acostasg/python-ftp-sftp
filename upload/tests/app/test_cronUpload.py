import unittest

import mock

import upload.injectionContainer as injectionContainer
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestCronUpload(unittest.TestCase):
    """
    Class Test cron upload
    """

    def test_cron_upload(self):
        """
        Test case upload file
        :return:
        """

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        with self.assertRaises(Exception):
            import upload.cronUpload as cronUpload

            self.assertTrue(cronUpload.execute_cron(
                'test_host',
                'test_username',
                'test_secret',
                80,
                'test_local',
                'test_remote',
                'test_prefix',
                'test_pattern',
                1
            ))

    def test_cron_upload_error(self):
        """
        Test case upload file
        :return:
        """

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        logger_mock = mock.Mock()
        logger_mock.basicConfig = Exception('Unknown')

        injectionContainer.Container.container.__setitem__('logger', logger_mock)

        with self.assertRaises(Exception):
            import upload.cronUpload as cronUpload

        with self.assertRaises(Exception):
            self.assertTrue(cronUpload.execute_cron(
                'test_host',
                'test_username',
                'test_secret',
                80,
                'test_local',
                'test_remote',
                'test_prefix',
                'test_pattern',
                1
            ))


if __name__ == '__main__':
    unittest.main()
