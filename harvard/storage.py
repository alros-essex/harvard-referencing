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
                id NUMBER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                user TEXT NOT NULL)''',
                {})

    def insert(self, collection):
        self._execute("INSERT INTO collections(id, name, description, user) VALUES(:id, :name, :description, :user)",
            { "id": collection.id(), "name": collection.name(), "description": collection.description(), "user": collection.user() })

    def select_by_name(self, name):
        cur = self._execute("SELECT id, user, name, description FROM collections where name = :name", { "name": name })
        row = cur.fetchone()
        if row == None:
            return None
        else:
            return Collection(
                id = row[0], 
                user = row[1], 
                name = row[2], 
                description = row[3])

    def _execute(self, statement, params):
        cur = self.con.cursor()
        cur.execute(statement, params)
        self.con.commit()
        return cur
    

