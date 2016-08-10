import unittest

import upload.injectionContainer as injectionContainer
from upload.strategy.dummys.injectedContainerDummy import ContainerMock

class TestRequestParams(unittest.TestCase):
    """
    Class test for request params class
    """

    def test_open_file_error(self):
        """
        test case secured upload
        """
        injectionContainer.Container.update(
            ContainerMock().container()
        )

        from upload.shared \
            import open_file

        with self.assertRaises(FileNotFoundError):
            open_file.execute('FailedTest', 'r')

if __name__ == '__main__':
    unittest.main()
