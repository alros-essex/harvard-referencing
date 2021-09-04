from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.state import State
from harvard.utility import Utility

class HandlerActiveCollection(HandlerBase):
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, collection: Collection):
        ref_lines, ref_options = self.__build_references(collection.references)
        opt_lines, opt_options = self.__build_options(collection.references)
        Utility.print_lines([
            '',
            '@title {name}'.format(name = collection.name),
            '@subtitle {description}'.format(description = collection.description),
            '',
            '@title   References:',
            ref_lines,
            opt_lines])
        user_input = Utility.prompt_user_for_input(options=opt_options)
        if user_input == 'N':
            return State.CREATE_NEW_REFERENCE, collection
        elif user_input == 'C':
            return State.NO_COLLECTIONS, collection
        elif user_input == 'M':
            return State.DELETE_COLLECTION, collection
        elif user_input == 'D':
            return State.DELETE_REFERENCE, {'collection': collection, 'options': ref_options}
        else:
            return State.EDIT_REFERENCE, {'collection': collection,'options': ref_options}

    def __build_references(self, references):
        lines = []
        options = []
        if references == []:
            lines.append('@option <empty>')
        else:
            for i, reference in enumerate(references):
                lines.append('    [{index}] : {ref}'.format(index = i, ref=reference.format_console()))
                options.append(i)
        lines.append('')
        return lines, options

    def __build_options(self, references):
        lines = [
            '@option Create [N]ew reference',
            '@option [C]lose collection',
            '@option Eli[M]inate collection',
            '']
        options = ['N','C','M']
        if len(references) > 0:
            lines.insert(2,'@option [E]dit reference')
            lines.insert(3,'@option [D]elete reference')
            options.insert(2, 'E')
            options.insert(3, 'D')
        return lines, options