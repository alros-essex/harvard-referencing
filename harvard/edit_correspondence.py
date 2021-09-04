from harvard.reference_correspondence import CorrespondenceReference
from harvard.edit_reference import EditReference

class EditCorrespondenceReference(EditReference):

    def edit(self, reference: CorrespondenceReference = None):
        values = super().edit(reference)
        values['date'] = self.prompt_user_for_input('Date', reference.date if reference is not None else None)
        return CorrespondenceReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            date= values['date'])