from harvard.reference_book import BookReference
from harvard.edit_reference import EditReference

class EditBookReference(EditReference):
    """Editor for Books"""

    def edit(self, reference: BookReference = None):
        """Edit or create the reference

        Args:
            reference: optional Reference, if None, the reference is simply created
        Returns:
            None
        """
        values = super().edit(reference)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        return BookReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            place = values['place'],
            publisher = values['publisher'],
            volume = values['volume'],
            edition = values['edition'])
    
    def get_type(self):
        """Returns the type handled by this editor
        
        Returns:
            ReferenceType
        """
        return BookReference.get_type()