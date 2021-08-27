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
                PRIMARY KEY (user, name))''')
            self._execute('''CREATE TABLE quote_references(
                user TEXT NOT NULL,
                collection TEXT NOT NULL,
                type TEXT,
                authors TEXT,
                year TEXT,
                title TEXT,
                journal TEXT,
                volume TEXT,
                edition TEXT,
                issue TEXT,
                place_of_publication TEXT,
                publisher TEXT,
                available_from_url TEXT,
                date_of_access TEXT,
                page_numbers TEXT)''')
            

    def insert_collection(self, collection):
        self._execute("INSERT INTO collections(name, description, user) VALUES(:name, :description, :user)",
            { "name": collection.name(), "description": collection.description(), "user": collection.user() })

    def select_collection_by_name(self, user, collection):
        cur = self._execute("SELECT user, name, description FROM collections where user = :user and name = :name", 
            { "user": user, "name": collection })
        row = cur.fetchone()
        if row == None:
            return None
        else:
            return Collection(
                user = row[0], 
                name = row[1], 
                description = row[2])

    def insert_reference(self, user, collection, reference):
        pass

    def select_references_by_collection(self, user, collection):
        pass

    def _execute(self, statement, params={}):
        cur = self.con.cursor()
        cur.execute(statement, params)
        self.con.commit()
        return cur
    

