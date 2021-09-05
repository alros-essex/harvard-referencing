from harvard.reference_un_resolution import UNResolutionReference
from harvard.edit_reference import EditReference
from harvard.utility import Utility

class EditUNResolutions(EditReference):

    def edit(self, reference: UNResolutionReference = None):
        values = {}
        values['year'] = self.prompt_user_for_input('Year', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Title', reference.title if reference is not None else None)
        type = Utility.prompt_user_for_input(text = '[G]eneral Assembly or [S]ecurity Council', options = ['G', 'S'])
        values['resolution_number'] = self.prompt_user_for_input('Resolution number', reference.resolution_number if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return UNResolutionReference(
            year = values['year'],
            title = values['title'],
            resolution_number = values['resolution_number'],
            url = values['url'],
            accessed = values['accessed'],
            general_assembly = type == 'G',
            security_council= type == 'S')

    def get_type(self):
        return UNResolutionReference.get_type()