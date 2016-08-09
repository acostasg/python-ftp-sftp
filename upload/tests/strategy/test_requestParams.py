import unittest

import upload.strategy.requestParams as Request


class TestRequestParams(unittest.TestCase):
    """
    Class test for request params class
    """

    def test_request_params(self):
        """
        test case unsecured upload
        :return:
        """
        request_params = Request.RequestParams()
        request_params.connectionInfo = {"tests": "tests"}
        request_params.localPath = 'localPath'
        request_params.pattern = '*.pattern'
        request_params.prefix = 'test_report'
        request_params.remotePath = 'remotePath'

        self.assertEqual(request_params.connectionInfo, {'tests': 'tests'})
        self.assertEqual(request_params.localPath, 'localPath')
        self.assertEqual(request_params.pattern, '*.pattern')
        self.assertEqual(request_params.prefix, 'test_report')
        self.assertEqual(request_params.remotePath, 'remotePath')

        str_request = str(request_params)

        self.assertEqual(
            '{"connectionInfo":{\'tests\': \'tests\'},"localPath":"localPath",'
            '"remotePath":"remotePath","prefix":"test_report","pattern":"*.pattern"}',
            str_request)


if __name__ == '__main__':
    unittest.main()
