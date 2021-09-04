from harvard.reference_journal_online import ArticleOnlineReference
from harvard.edit_reference import EditReference

class EditJournalOnlineReference(EditReference):

    def edit(self, reference: ArticleOnlineReference = None):
        values = super().edit(reference)
        values['journal'] = self.prompt_user_for_input('Journal', reference.journal if reference is not None else None)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['issue'] = self.prompt_user_for_input('Issue', reference.issue if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        values['doi'] = self.prompt_user_for_input('DOI', reference.doi if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return ArticleOnlineReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            journal= values['journal'],
            volume= values['volume'],
            issue= values['issue'],
            pages= values['pages'],
            url= values['url'],
            accessed= values['accessed'],
            doi= values['doi'])