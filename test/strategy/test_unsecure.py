import unittest

class TestUnsecure(unittest.TestCase):
    # @TODO
    def unsecured_upload(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
