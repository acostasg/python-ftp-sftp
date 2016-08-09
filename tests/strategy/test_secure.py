import logging
import unittest
import mock

import injectionContainer
import strategy.requestParams as Request
from strategy.dummys.injectedContainerDummy import ContainerMock


class TestSecure(unittest.TestCase):
    """
    Class test for sercure strategy
    """

    def test_secure_upload(self):
        """
        test case secured upload
        """
        from strategy \
            import secure as str_secure

        logger_mock = logging
        logger_mock.warning = mock.Mock(return_value=0)
        logger_mock.info = mock.Mock(return_value=0)

        request = Request.RequestParams()
        request.connectionInfo = {'host': '', 'port': '', 'username': '', 'password': ''}

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        unsecure = str_secure.Secure(logging)
        self.assertTrue(unsecure.upload(request))
