from .collection import Collection

from os.path import exists
import sqlite3

class Storage:

    _path_to_database='references.db'

    def __init__(self):
        path_to_database = Storage._path_to_database
        to_be_initialized = not exists(path_to_database)
        self.con = sqlite3.connect(path_to_database)
        if to_be_initialized:
            self._execute('''CREATE TABLE collections(
                user TEXT NOT NULL,
                name TEXT NOT NULL,
                description TEXT NOT NULL, 
                PRIMARY KEY (user, name))''',
                {})
            

    def insert_collection(self, collection):
        self._execute("INSERT INTO collections(name, description, user) VALUES(:name, :description, :user)",
            { "name": collection.name(), "description": collection.description(), "user": collection.user() })

    def select_collection_by_name(self, user, name):
        cur = self._execute("SELECT user, name, description FROM collections where user = :user and name = :name", 
            { "user": user, "name": name })
        row = cur.fetchone()
        if row == None:
            return None
        else:
            return Collection(
                user = row[0], 
                name = row[1], 
                description = row[2])

    def _execute(self, statement, params):
        cur = self.con.cursor()
        cur.execute(statement, params)
        self.con.commit()
        return cur
    

