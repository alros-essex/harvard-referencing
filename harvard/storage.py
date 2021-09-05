import os
import pickle

from .collection import Collection

class Storage:
    """
    Abstraction of the filesystem
    """

    def __init__(self, base_path = './harvard_collections_data'):
        self.__base_path = base_path
        self.__init_storage()

    def __init_storage(self) -> None:
        """
        create folder
        """
        if not os.path.isdir(self.__base_path):
            os.mkdir(self.__base_path)

    def __load(self, filename:str):
        """
        data deserialization
        """
        with open(os.path.join(self.__base_path, filename), "rb") as f:
            data = pickle.load(f)
        return data

    def __save(self, filename:str, data) -> None:
        """
        data serialization
        """
        with open(os.path.join(self.__base_path, filename), "wb") as f:
            pickle.dump(data, f)

    def __delete(self, filename:str) -> None:
        """
        file delete
        """
        os.remove(os.path.join(self.__base_path, filename))

    def __load_collection(self, collection_name:str) -> Collection:
        """
        file read
        """
        return self.__load('{collection}.bin'.format(collection = collection_name))
            
    def save_collection(self, collection: Collection) -> None:
        """
        it saves a collection in a file with the same name
        """
        self.__save('{collection}.bin'.format(collection = collection.name), collection)

    def delete_collection(self, collection: Collection) -> None:
        """
        it deletes a collection from the storage
        """
        self.__delete('{collection}.bin'.format(collection = collection.name))

    def list_all_collections(self):
        """
        finds all collections in the storage
        """
        files = os.listdir(self.__base_path)
        def split(filename:str):
            return filename[0:filename.rfind(".")]
        names = list(map(split, files))
        names.sort()
        return names

    def find_collection_by_name(self, name: str) -> Collection:
        """
        it loads a collection
        """
        return self.__load_collection(name)          

    def erase_data(self):
        """
        WARNING: it wipes all data (for testing!)
        """
        for file in os.listdir(self.__base_path):
            os.remove('{path}/{file}'.format(path = self.__base_path, file = file))
        os.rmdir(self.__base_path)