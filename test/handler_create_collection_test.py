import unittest

from harvard.handler_create_collection import HandlerCreateNewCollection

class TestReference(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.maxDiff = None

    def test_names(self):      
        h = HandlerCreateNewCollection(None)
        self.assertFalse(h._is_valid_name(' abc'))
        self.assertFalse(h._is_valid_name('abc '))
        self.assertFalse(h._is_valid_name('±abc'))
        self.assertFalse(h._is_valid_name('../abc'))
        self.assertTrue(h._is_valid_name('abcABC123-__'))
