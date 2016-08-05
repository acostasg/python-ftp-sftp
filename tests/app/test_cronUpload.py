import unittest

import injectionContainer

from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestCronUpload(unittest.TestCase):
    def test_cron_upload(self):

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        import cronUpload