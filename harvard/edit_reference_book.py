from harvard.reference_book import BookReference
from harvard.edit_reference import EditReference

class EditBookReference(EditReference):

    def edit(self, reference: BookReference = None):
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