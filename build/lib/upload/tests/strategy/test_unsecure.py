import logging
import unittest
import mock

import injectionContainer
import strategy.requestParams as Request
from strategy.dummys.injectedContainerDummy import ContainerMock


class TestUnsecure(unittest.TestCase):
    """
    Class test for unsercure strategy
    """

    def test_unsecured_upload(self):
        """
        test case unsecured upload
        :return:
        """
        from strategy \
            import unsecure as str_unsecure

        logger_mock = logging
        logger_mock.warning = mock.Mock(return_value=0)
        logger_mock.info = mock.Mock(return_value=0)

        request = Request.RequestParams()
        request.connectionInfo = {'host': '', 'port': '', 'username': '', 'password': ''}

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        unsecure = str_unsecure.Unsecure(logging)
        self.assertTrue(unsecure.upload(request))
