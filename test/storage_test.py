from harvard.reference import Reference
import unittest
import os

from harvard.collection import Collection
from harvard.reference import Reference
from harvard.storage import Storage


class TestStorage(unittest.TestCase):

    def setUp(self):
        Storage._path_to_database = 'test_references.db'
        self.storage = Storage()

    def tearDown(self):
        os.remove(Storage._path_to_database)
        return super().tearDown()

    def test_insert_select_collection(self):
        collection = Collection('My User','My Collection','Just a test')
        self.storage.insert_collection(collection)
        db_collection = self.storage.select_collection_by_name('My User', 'My Collection')
        self.assertEqual(collection, db_collection)

    def test_inser_select_reference(self):
        pass

if __name__ == '__main__':
    unittest.main()