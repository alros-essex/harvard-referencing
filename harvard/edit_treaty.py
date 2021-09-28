from harvard.reference_treaty import TreatyReference
from harvard.edit_reference import EditReference

class EditTreatyResolution(EditReference):
    """Editor for International Treaties, Conventions and accords"""

    def edit(self, reference: TreatyReference = None):
        """Edit or create the reference

        Args:
            reference: optional Reference, if None, the reference is simply created
        Returns:
            None
        """
        values = {}
        values['year'] = self.prompt_user_for_input('Year', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Title', reference.title if reference is not None else None)
        values['treaty_number'] = self.prompt_user_for_input('Treaty number', reference.treaty_number if reference is not None else None)
        values['publication_title'] = self.prompt_user_for_input('Publication title', reference.publication_title if reference is not None else None)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return TreatyReference(
            year= values['year'],
            title= values['title'],
            treaty_number= values['treaty_number'],
            publication_title= values['publication_title'],
            volume = values['volume'],
            pages = values['pages'],
            url= values['url'],
            accessed= values['accessed'])

    def get_type(self):
        """Returns the type handled by this editor
        
        Returns:
            ReferenceType
        """
        return TreatyReference.get_type()