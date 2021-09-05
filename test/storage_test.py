import unittest

from harvard.collection import Collection
from harvard.reference_book import BookReference
from harvard.storage import Storage


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = Storage('./harvard_collections_data_test')

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

    def test_insert_delete_collection(self):
        collection = Collection(name = 'My Collection', description = 'My Collection')
        self.storage.save_collection(collection)
        self.assertEqual(1, len(self.storage.list_all_collections()))
        self.storage.delete_collection(collection)
        self.assertEqual(0, len(self.storage.list_all_collections()))

if __name__ == '__main__':
    unittest.main()