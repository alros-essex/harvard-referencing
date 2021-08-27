import unittest
import os

from harvard.collection import Collection
from harvard.storage import Storage

class TestDb(unittest.TestCase):

    def setUp(self):
        Storage._path_to_database = 'test_references.db'
        pass

    def tearDown(self):
        os.remove(Storage._path_to_database)
        return super().tearDown()

    def test_insert_select(self):
        storage = Storage()

        collection = Collection('abc123', 'My User','My Collection','Just a test')

        storage.insert_collection(collection)

        db_collection = storage.select_collection_by_name('My User', 'My Collection')

        print("db collection is {coll}".format(coll = db_collection))

        self.assertEqual(collection, db_collection)

if __name__ == '__main__':
    unittest.main()