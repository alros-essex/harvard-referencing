import copy
import unittest

from harvard.collection import Collection
from harvard.reference_book import BookReference

class TestCollection(unittest.TestCase):

    def test_basic_collection_functions(self):
        collection = Collection('my name', 'my description')

        self.assertEqual('my name', collection.name)
        self.assertEqual('my description', collection.description)
        self.assertEqual([], collection.references)

        reference = BookReference('a','y','t','p','p')
        collection.add_reference(copy.copy(reference))

        self.assertEqual([reference], collection.references)


