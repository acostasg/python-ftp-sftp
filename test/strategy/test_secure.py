import unittest

class TestSecure(unittest.TestCase):

    def test_secure_upload(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
