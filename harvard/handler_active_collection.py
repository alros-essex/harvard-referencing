from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.state import State
from harvard.utility import Utility

class HandlerActiveCollection(HandlerBase):
    """This is the handler used when a collection is open and ready to be manipulated"""

    def __init__(self,storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)

    def handle(self, collection: Collection):
        """Handle the current context
        
        Args:
            option: current context
        Returns:
            next state and next context
        """
        # prepare the data for the screen
        ref_lines, ref_options = self.__build_references(collection.references)
        opt_lines, opt_options = self.__build_options(collection.references)
        # print everything with some formatting
        Utility.print_lines([
            '',
            '@title {name}'.format(name = collection.name),
            '@subtitle {description}'.format(description = collection.description),
            '',
            '@title   References:',
            ref_lines,
            opt_lines])
        # get the desired action
        user_input = Utility.prompt_user_for_input(options=opt_options)
        if user_input == 'N':
            # user want a new reference
            return State.CREATE_NEW_REFERENCE, collection
        elif user_input == 'C':
            # user wants to close the collection
            return State.NO_COLLECTIONS, collection
        elif user_input == 'M':
            # user wants to delete the collection
            return State.DELETE_COLLECTION, collection
        elif user_input == 'D':
            # user wants to delete a reference
            return State.DELETE_REFERENCE, {'collection': collection, 'options': ref_options}
        elif user_input == 'P':
            # print everything and quit
            lines, _ = self.__build_references(references=collection.references, for_print=True)
            Utility.print_lines([
                '', 
                '@title References for your paper',
                '',
                lines,
                ''
                '@subtitle Goodbye!'
                ])
            # ...and bye bye!
            return State.EXIT, _
        else:
            # user wants to edit a reference
            return State.EDIT_REFERENCE, {'collection': collection,'options': ref_options}

    def __build_references(self, references, for_print = False):
        """prepare the output lines and the corresponding options
        
        Args:
            references: all references in the collection
            for_print: when it's true, some formatting is skipped
        Returns:
            the lines and the options to select them
        """
        lines = []
        options = []
        if references == []:
            lines.append('<empty>' if for_print else '@option <empty>')
        else:
            for i, reference in enumerate(references):
                # delegate formatting to the reference
                ref = reference.format_console()
                # some formatting
                lines.append('{ref}'.format(ref=ref) if for_print else '    [{index}] : {ref}'.format(index = i, ref=ref))
                options.append(i)
        lines.append('')
        return lines, options

    def __build_options(self, references):
        """create the screen
        
        Args:
            reference: all references in the collection
        Returns:
            the lines and the options to select them
        """
        lines = [
            '@option Create [N]ew reference',
            '@option [C]lose collection',
            '@option Eli[M]inate collection',
            '@option Exit application and [P]rint'
            '']
        options = ['N','C','M','P']
        if len(references) > 0:
            lines.insert(2,'@option [E]dit reference')
            lines.insert(3,'@option [D]elete reference')
            options.insert(2, 'E')
            options.insert(3, 'D')
        return lines, options

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.ACTIVE_COLLECTION