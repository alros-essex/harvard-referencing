from .reference import Reference

class Collection():

    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description
        self.references = []
