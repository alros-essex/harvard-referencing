from harvard.reference_conference import ConferencePapersReference
from harvard.edit_reference import EditReference

class EditConferencePapersReference(EditReference):

    def edit(self, reference: ConferencePapersReference = None):
        values = super().edit(reference)
        values['conference_title'] = self.prompt_user_for_input('Conference title', reference.conference_title if reference is not None else None)
        values['conference_location'] = self.prompt_user_for_input('Conference location', reference.conference_location if reference is not None else None)
        values['conference_date'] = self.prompt_user_for_input('Conference date', reference.conference_date if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        return ConferencePapersReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            conference_title= values['conference_title'],
            conference_date= values['conference_date'],
            place= values['place'],
            publisher= values['conference_location'],
            conference_location= values['conference_location'],
            pages = values['pages'])