from harvard.reference_journal import ArticleReference
from harvard.edit_reference import EditReference

class EditJournalReference(EditReference):
    """Editor for Journal Articles"""

    def edit(self, reference: ArticleReference = None):
        """Edit or create the reference

        Args:
            reference: optional Reference, if None, the reference is simply created
        Returns:
            None
        """
        values = super().edit(reference)
        values['journal'] = self.prompt_user_for_input('Journal', reference.journal if reference is not None else None)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['issue'] = self.prompt_user_for_input('Issue', reference.issue if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        return ArticleReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            issue= values['issue'],
            journal = values['journal'],
            volume = values['volume'],
            pages = values['pages'])

    def get_type(self):
        """Returns the type handled by this editor
        
        Returns:
            ReferenceType
        """
        return ArticleReference.get_type()