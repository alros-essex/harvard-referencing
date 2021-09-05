from harvard.reference_research_online import ResearchReportOnlineReference
from harvard.edit_reference import EditReference

class EditResearchReportOnlineReference(EditReference):

    def edit(self, reference: ResearchReportOnlineReference = None):
        values = super().edit(reference)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return ResearchReportOnlineReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            url= values['url'],
            accessed= values['accessed'])

    def get_type(self):
        return ResearchReportOnlineReference.get_type()