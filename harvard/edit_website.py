from harvard.reference_website import WebsiteReference
from harvard.edit_reference import EditReference

class EditWebsiteReference(EditReference):

    def edit(self, reference: WebsiteReference = None):
        values = super().edit(reference)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return WebsiteReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            url= values['url'],
            accessed= values['accessed'])

    def get_type(self):
        return WebsiteReference.get_type()