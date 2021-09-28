from harvard.reference_correspondence import CorrespondenceReference
from harvard.edit_reference import EditReference

class EditCorrespondenceReference(EditReference):
    """Editor for Personal Correspondence"""

    def edit(self, reference: CorrespondenceReference = None):
        """Edit or create the reference

        Args:
            reference: optional Reference, if None, the reference is simply created
        Returns:
            None
        """
        values = super().edit(reference)
        values['date'] = self.prompt_user_for_input('on (day)', reference.date if reference is not None else None)
        return CorrespondenceReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            date= values['date'])

    def get_type(self):
        """Returns the type handled by this editor
        
        Returns:
            ReferenceType
        """
        return CorrespondenceReference.get_type()