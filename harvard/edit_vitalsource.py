from harvard.reference_vitalsource import VitalsourceReference
from harvard.edit_reference import EditReference

class EditVitalsourceReference(EditReference):

    def edit(self, reference: VitalsourceReference = None):
        values = super().edit(reference)
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['last_access'] = self.prompt_user_for_input('Last accessed', reference.last_access if reference is not None else None)
        return VitalsourceReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            place = values['place'],
            publisher = values['publisher'],
            last_access = values['last_access'],
            edition = values['edition'])

    def get_type(self):
        return VitalsourceReference.get_type()