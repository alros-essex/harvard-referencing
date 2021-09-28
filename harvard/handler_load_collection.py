from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State
from harvard.utility import Utility

class HandlerLoadCollection(HandlerBase):
    """Handler to load a collection"""
    
    def __init__(self,storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)

    def handle(self, _):
        """Handle the current context
        
        Args:
            option: current context
        Returns:
            next state and next context
        """
        # find all collections
        collections = self.storage.list_all_collections()
        Utility.print_lines([
            '',
            '@title List of collections:'
        ])
        # if there's none...
        if collections == []:
            Utility.print_lines([
                '@option <empty>',
                ''])
            # go to the creation screen
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
            # create the screen
            lines, options = build_references()
            Utility.print_lines(lines)
            # let the user choose
            selected = Utility.prompt_user_for_input(options=options)
            collection = self.storage.find_collection_by_name(collections[int(selected)])
            # go to the main view with the chosen collection
            return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.LOAD_COLLECTION
