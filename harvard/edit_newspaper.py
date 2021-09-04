from harvard.reference_newspaper import ArticleNewpaperReference
from harvard.edit_reference import EditReference

class EditNewspaperReference(EditReference):

    def edit(self, reference: ArticleNewpaperReference = None):
        values = super().edit(reference)
        values['newspaper'] = self.prompt_user_for_input('Newspaper', reference.newspaper if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        return ArticleNewpaperReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            newspaper= values['newspaper'],
            pages= values['pages'])