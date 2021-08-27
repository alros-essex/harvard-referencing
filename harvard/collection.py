class Collection():

    def __init__(self, user, name, description):
        self._user = user
        self._name = name
        self._description = description

    def user(self):
        return self._user

    def name(self):
        return self._name

    def description(self):
        return self._description
    
    def __eq__(self, o: object) -> bool:
        return (isinstance(o, Collection) 
            and self._user == o._user
            and self._name == o._name
            and self._description == o._description)