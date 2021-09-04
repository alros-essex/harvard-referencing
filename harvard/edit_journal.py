from harvard.reference_journal import ArticleReference
from harvard.edit_reference import EditReference

class EditJournalReference(EditReference):

    def edit(self, reference: ArticleReference = None):
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