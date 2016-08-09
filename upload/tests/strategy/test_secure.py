import logging
import unittest

import mock

import upload.injectionContainer as injectionContainer
import upload.strategy.requestParams as Request
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestSecure(unittest.TestCase):
    """
    Class test for sercure strategy
    """

    def test_secure_upload(self):
        """
        test case secured upload
        """
        injectionContainer.Container.update(
            ContainerMock().container()
        )

        from upload.strategy \
            import secure as str_secure

        logger_mock = logging
        logger_mock.warning = mock.Mock(return_value=0)
        logger_mock.info = mock.Mock(return_value=0)

        request = Request.RequestParams()
        request.connectionInfo = {'host': '', 'port': '', 'username': '', 'password': ''}

        unsecure = str_secure.Secure(logging)
        self.assertTrue(unsecure.upload(request))


if __name__ == '__main__':
    unittest.main()
