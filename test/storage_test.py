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
        reference = Reference.new_book("My User", "My Collection")          \
            .with_authors('Armstrong, G., Kotler, P. & Opresnik, O.') \
            .with_year('2016')                                        \
            .with_title('Marketing: An Introduction')                 \
            .with_edition('13th')                                     \
            .with_place_of_publication('Harlow')                      \
            .with_publisher('Pearson Education Limited')              \
            .build()
        self.storage.insert_reference('My User', 'My Collection', reference)
        db_references = self.storage.select_references_by_collection('My User', 'My Collection')
        self.assertEquals(1,len(db_references))
        self.asserEquals(reference, db_references[0])

if __name__ == '__main__':
    unittest.main()