from harvard.reference_newspaper import ArticleNewpaperReference
from harvard.edit_reference import EditReference

class EditNewspaperReference(EditReference):
    """Editor for Newspaper Article"""

    def edit(self, reference: ArticleNewpaperReference = None):
        """Edit or create the reference

        Args:
            reference: optional Reference, if None, the reference is simply created
        Returns:
            None
        """
        values = super().edit(reference)
        values['newspaper'] = self.prompt_user_for_input('Newspaper', reference.newspaper if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        return ArticleNewpaperReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            newspaper= values['newspaper'],
            pages= values['pages'])
    
    def get_type(self):
        """Returns the type handled by this editor
        
        Returns:
            ReferenceType
        """
        return ArticleNewpaperReference.get_type()