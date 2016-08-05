import logging
import unittest
from unittest.mock import MagicMock

import injectionContainer
import strategy.requestParams as Request
from strategy.dummys.injectedContainerDummy import ContainerMock


class TestSecure(unittest.TestCase):
    def test_secure_upload(self):
        from strategy \
            import secure as str_secure

        logger_mock = logging
        logger_mock.warning = MagicMock(return_value=0)
        logger_mock.info = MagicMock(return_value=0)

        request = Request.RequestParams()
        request.connectionInfo = {'host': '', 'port': '', 'username': '', 'password': ''}

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        unsecure = str_secure.Secure(logging)
        self.assertTrue(unsecure.upload(request))


if __name__ == '__main__':
    unittest.main()
