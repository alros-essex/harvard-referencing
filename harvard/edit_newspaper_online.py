from harvard.reference_electronic_newspaper import ArticleElectronicNewpaperReference
from harvard.edit_reference import EditReference

class EditNewspaperOnlineReference(EditReference):

    def edit(self, reference: ArticleElectronicNewpaperReference = None):
        values = super().edit(reference)
        values['newspaper'] = self.prompt_user_for_input('Newspaper', reference.newspaper if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return ArticleElectronicNewpaperReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            newspaper= values['newspaper'],
            pages= values['pages'],
            url= values['url'],
            accessed= values['accessed'])