from harvard.reference_correspondence import CorrespondenceReference
from harvard.edit_reference import EditReference

class EditCorrespondenceReference(EditReference):

    def edit(self, reference: CorrespondenceReference = None):
        values = super().edit(reference)
        return CorrespondenceReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            date= values['date'])

    def get_type(self):
        return CorrespondenceReference.get_type()