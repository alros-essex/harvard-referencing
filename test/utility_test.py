import unittest

from harvard.utility import Utility

class TestStorage(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_list_collections(self):
        self.assertEqual('T',Utility._extract_option_letter("@option something some[T]ing"))
        self.assertIsNone(Utility._extract_option_letter("@option something something"))

if __name__ == '__main__':
    unittest.main()