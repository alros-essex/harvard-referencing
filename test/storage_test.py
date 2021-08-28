from harvard.reference import BookReference
import unittest
import os

from harvard.collection import Collection
from harvard.reference import Reference
from harvard.storage import Storage


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = Storage()

    def tearDown(self):
        return super().tearDown()

    def test_insert_select_collection(self):
        collection = Collection(name = 'My Collection', description = 'Just a test')
        self.storage.insert_collection(collection)
        db_collection = self.storage.select_collection_by_name('My Collection')
        self.assertEqual(collection, db_collection)

    def test_inser_select_reference(self):
        reference = BookReference(
            authors = 'Armstrong, G., Kotler, P. & Opresnik, O.',
            year = '2016',
            title = 'Marketing: An Introduction',
            edition = '13th',
            place = 'Harlow',
            publisher = 'Pearson Education Limited')
        collection = Collection(name = 'My Collection', description = 'My Collection')
        self.storage.insert_collection(collection)
        self.storage.insert_reference(collection, reference)
        db_references = self.storage.select_references_by_collection(collection)
        self.assertEquals(1,len(db_references))
        self.assertEquals(reference, db_references[0])

if __name__ == '__main__':
    unittest.main()