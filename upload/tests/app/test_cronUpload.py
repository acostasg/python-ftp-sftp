import unittest

import mock
import sys

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

        sys.stdout = sys.__stdout__

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
            1,
            injectionContainer.Container.dependency('logger')
        ))

    def test_cron_execute_error(self):
        """
        Test case upload file
        :return:
        """
        import getopt

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        get_opt = mock.Mock()
        get_opt.getopt = mock.Mock(side_effect=getopt.GetoptError)
        get_opt.GetoptError = getopt.GetoptError

        injectionContainer.Container.container.__setitem__('get_opt', get_opt)

        sys.stdout = sys.__stdout__

        with self.assertRaises(Exception):
            import upload.cronUpload as cronUpload


    def test_cron_upload_error(self):
        """
        Test case upload file
        :return:
        """

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        logger_mock = mock.Mock()
        logger_mock.basicConfig = mock.Mock(side_effect=Exception('foo'))

        injectionContainer.Container.container.__setitem__('logger', logger_mock)

        sys.stdout = sys.__stdout__

        import upload.cronUpload as cronUpload

        with self.assertRaises(Exception):
            cronUpload.execute_cron(
                'test_host',
                'test_username',
                'test_secret',
                80,
                'test_local',
                'test_remote',
                'test_prefix',
                'test_pattern',
                1,
                logger_mock
            )


if __name__ == '__main__':
    unittest.main()
