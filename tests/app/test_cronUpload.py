import unittest

import injectionContainer

from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestCronUpload(unittest.TestCase):
    """
    Test case for cron upload
    """
    def test_cron_upload(self):

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        import cronUpload