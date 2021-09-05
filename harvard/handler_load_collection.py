from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State
from harvard.utility import Utility

class HandlerLoadCollection(HandlerBase):
    
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        collections = self.storage.list_all_collections()
        Utility.print_lines([
            '',
            '@title List of collections:'
        ])
        if collections == []:
            Utility.print_lines([
                '@option <empty>',
                ''])
            return State.CREATE_NEW_COLLECTION, None
        else:
            def build_references():
                options = []
                lines = []
                for i, collection_name in enumerate(collections):
                    lines.append('@option [{index}] : {name}'.format(index = i, name = collection_name))
                    options.append(str(i))
                lines.append('')
                return lines, options
            lines, options = build_references()
            Utility.print_lines(lines)
            selected = Utility.prompt_user_for_input(options=options)
            collection = self.storage.find_collection_by_name(collections[int(selected)])
            return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        return State.LOAD_COLLECTION
