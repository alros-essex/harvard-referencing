import os
import pickle

from .collection import Collection

class Storage:
    """Abstraction of the filesystem"""

    def __init__(self, base_path = './harvard_collections_data'):
        """Creates the singleton
        
        Args:
            base_path: path of the data (useful for testing)
        Returns:
            None
        """
        self.__base_path = base_path
        self.__init_storage()

    def __init_storage(self) -> None:
        """Create data folder"""
        if not os.path.isdir(self.__base_path):
            os.mkdir(self.__base_path)

    def __load(self, filename:str):
        """Data deserialization

        Args:
            filename: file with the data
        Returns:
            deserialized data
        """
        with open(os.path.join(self.__base_path, filename), "rb") as f:
            data = pickle.load(f)
        return data

    def __save(self, filename:str, data) -> None:
        """Data serialization

        Args:
            filename: file with the data
        Returns:
            None
        """
        with open(os.path.join(self.__base_path, filename), "wb") as f:
            pickle.dump(data, f)

    def __delete(self, filename:str) -> None:
        """Delete a file

        Args:
            filename: file to delete
        Returns:
            None
        """
        os.remove(os.path.join(self.__base_path, filename))

    def __load_collection(self, collection_name:str) -> Collection:
        """Load a collection
        
        Args:
            collection_name: name of the collection. The filename is [collection_name].bin
        Returns:
            the collection from disk
        """
        return self.__load('{collection}.bin'.format(collection = collection_name))
            
    def save_collection(self, collection: Collection) -> None:
        """It saves a collection in a file with the same name

        Args:
            collection: Collection to save. The filename will be collection.name+.bin
        Returns:
            None
        """
        self.__save('{collection}.bin'.format(collection = collection.name), collection)

    def delete_collection(self, collection: Collection) -> None:
        """It deletes a collection from the storage

        Args:
            collection: collection to delete
        Returns:
            None
        """
        self.__delete('{collection}.bin'.format(collection = collection.name))

    def list_all_collections(self):
        """Find all collections in the storage

        Args:
            None
        Returns:
            list of collection names
        """
        files = os.listdir(self.__base_path)
        def split(filename:str):
            return filename[0:filename.rfind(".")]
        names = list(map(split, files))
        names.sort()
        return names

    def find_collection_by_name(self, name: str) -> Collection:
        """It loads a collection

        Args:
            name: collection name
        Returns:
            Collection loaded from disk
        """
        return self.__load_collection(name)          

    def erase_data(self):
        """It erases the storage

        WARNING: it wipes all data (for testing!)

        Args:
            None
        Returns:
            None
        """
        for file in os.listdir(self.__base_path):
            os.remove('{path}/{file}'.format(path = self.__base_path, file = file))
        os.rmdir(self.__base_path)