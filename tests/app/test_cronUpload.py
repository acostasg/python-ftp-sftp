import unittest

import injectionContainer

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

        import cronUpload