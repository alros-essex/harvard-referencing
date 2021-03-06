from harvard.reference_chapter import ChapterEditedBookReference
from harvard.edit_reference import EditReference

class EditChapterReference(EditReference):
    """Editor for Chapter in an Edited Book"""

    def edit(self, reference: ChapterEditedBookReference = None):
        """Edit or create the reference

        Args:
            reference: optional Reference, if None, the reference is simply created
        Returns:
            None
        """
        values = super().edit(reference)
        values['original_authors'] = self.prompt_user_for_input('Original authors', reference.original_authors if reference is not None else None)
        values['original_title'] = self.prompt_user_for_input('Original title', reference.original_title if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.edition if reference is not None else None)
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        return ChapterEditedBookReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            original_authors = values['original_authors'],
            original_title = values['original_title'],
            place = values['place'],
            publisher = values['publisher'],
            pages = values['pages'],
            edition = values['edition'])

    def get_type(self):
        """Returns the type handled by this editor
        
        Returns:
            ReferenceType
        """
        return ChapterEditedBookReference.get_type()