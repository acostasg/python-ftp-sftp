import unittest

import strategy.requestParams as Request


class TestRequestParams(unittest.TestCase):
    def test_request_params(self):
        request_params = Request.RequestParams()
        request_params.connectionInfo = {'test': 'test'}
        request_params.localPath = 'localPath'
        request_params.pattern = '*.pattern'
        request_params.prefix = 'test_report'
        request_params.remotePath = 'remotePath'

        self.assertEqual(request_params.connectionInfo, {'test': 'test'})
        self.assertEqual(request_params.localPath, 'localPath')
        self.assertEqual(request_params.pattern, '*.pattern')
        self.assertEqual(request_params.prefix, 'test_report')
        self.assertEqual(request_params.remotePath, 'remotePath')


if __name__ == '__main__':
    unittest.main()
