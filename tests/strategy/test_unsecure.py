import logging
import unittest
from unittest.mock import MagicMock

import injectionContainer
import strategy.requestParams as Request
from strategy.dummys.injectedContainerDummy import ContainerMock


class TestUnsecure(unittest.TestCase):
    def test_unsecured_upload(self):
        """
        test case unsecured upload
        :return:
        """
        from strategy \
            import unsecure as str_unsecure

        logger_mock = logging
        logger_mock.warning = MagicMock(return_value=0)
        logger_mock.info = MagicMock(return_value=0)

        request = Request.RequestParams()
        request.connectionInfo = {'host': '', 'port': '', 'username': '', 'password': ''}

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        unsecure = str_unsecure.Unsecure(logging)
        self.assertTrue(unsecure.upload(request))