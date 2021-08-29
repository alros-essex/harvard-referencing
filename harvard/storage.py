import pickle
import os

from .collection import Collection
from .reference import Reference

class Storage:

    __base_path = './harvard_collections_data'

    def __init__(self):
        self.__init_storage()

    def __init_storage(self) -> None:
        if not os.path.isdir(Storage.__base_path):
            os.mkdir(Storage.__base_path)

    def __load(self, filename:str):
        with open('{path}/{filename}'.format(path = Storage.__base_path, filename = filename), "rb") as f:
            data = pickle.load(f)
        return data

    def __save(self, filename:str, data) -> None:
        with open('{path}/{file}'.format(path = Storage.__base_path, file = filename), "wb") as f:
            pickle.dump(data, f)
            
    def __load_collection(self, collection_name:str) -> Collection:
        return self.__load('{collection}.bin'.format(collection = collection_name))
            
    def save_collection(self, collection: Collection) -> None:
        self.__save('{collection}.bin'.format(collection = collection.name), collection)

    def list_all_collections(self):
        files:list = os.listdir(Storage.__base_path)
        def split(filename:str):
            return filename[0:filename.rfind(".")]
        names = list(map(split, files))
        names.sort()
        return names

    def find_collection_by_name(self, name: str) -> Collection:
        return self.__load_collection(name)          

    def erase_data(self):
        for file in os.listdir(Storage.__base_path):
            os.remove('{path}/{file}'.format(path = Storage.__base_path, file = file))
        os.rmdir(Storage.__base_path)