import pickle
import os

from .collection import Collection
from .reference import Reference
from .reference_book import BookReference
from .reference_ebook import EbookReference
from .reference_chapter import ChapterEditedBookReference
from .reference_vitalsource import VitalsourceReference

class Storage:

    def __init__(self, base_path = './harvard_collections_data'):
        self.__base_path = base_path
        self.__init_storage()

    def __init_storage(self) -> None:
        if not os.path.isdir(self.__base_path):
            os.mkdir(self.__base_path)

    def __load(self, filename:str):
        with open(os.path.join(self.__base_path, filename), "rb") as f:
            data = pickle.load(f)
        return data

    def __save(self, filename:str, data) -> None:
        with open(os.path.join(self.__base_path, filename), "wb") as f:
            pickle.dump(data, f)

    def __delete(self, filename:str) -> None:
        os.remove(os.path.join(self.__base_path, filename))

    def __load_collection(self, collection_name:str) -> Collection:
        return self.__load('{collection}.bin'.format(collection = collection_name))
            
    def save_collection(self, collection: Collection) -> None:
        self.__save('{collection}.bin'.format(collection = collection.name), collection)

    def delete_collection(self, collection: Collection) -> None:
        self.__delete('{collection}.bin'.format(collection = collection.name))

    def list_all_collections(self):
        files = os.listdir(self.__base_path)
        def split(filename:str):
            return filename[0:filename.rfind(".")]
        names = list(map(split, files))
        names.sort()
        return names

    def find_collection_by_name(self, name: str) -> Collection:
        return self.__load_collection(name)          

    def erase_data(self):
        for file in os.listdir(self.__base_path):
            os.remove('{path}/{file}'.format(path = self.__base_path, file = file))
        os.rmdir(self.__base_path)