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
        self.storage.erase_data()
        return super().tearDown()

    def test_list_collections(self):
        all = self.storage.list_all_collections()
        self.assertEqual([], all)
        self.storage.save_collection(Collection('my second name','my descr'))
        self.storage.save_collection(Collection('my first name', 'my descr'))
        all = self.storage.list_all_collections()
        self.assertEqual(['my first name','my second name'], all)

    def test_insert_find_collection(self):
        collection = Collection(name = 'My Collection', description = 'Just a test')
        self.storage.save_collection(collection)
        db_collection = self.storage.find_collection_by_name('My Collection')
        self.assertEqual(collection, db_collection)

    def test_insert_find_reference(self):
        reference = BookReference(
            authors = 'Armstrong, G., Kotler, P. & Opresnik, O.',
            year = '2016',
            title = 'Marketing: An Introduction',
            edition = '13th',
            place = 'Harlow',
            publisher = 'Pearson Education Limited')
        collection = Collection(name = 'My Collection', description = 'My Collection', references = [reference])
        self.storage.save_collection(collection)
        db_collection = self.storage.find_collection_by_name('My Collection')
        self.assertEquals(collection, db_collection)

if __name__ == '__main__':
    unittest.main()