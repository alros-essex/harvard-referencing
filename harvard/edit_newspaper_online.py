from harvard.reference_electronic_newspaper import ArticleElectronicNewpaperReference
from harvard.edit_reference import EditReference

class EditNewspaperOnlineReference(EditReference):
    """Editor for Electronic Newspaper Articles"""

    def edit(self, reference: ArticleElectronicNewpaperReference = None):
        """Edit or create the reference

        Args:
            reference: optional Reference, if None, the reference is simply created
        Returns:
            None
        """
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

    def get_type(self):
        """Returns the type handled by this editor
        
        Returns:
            ReferenceType
        """
        return ArticleElectronicNewpaperReference.get_type()