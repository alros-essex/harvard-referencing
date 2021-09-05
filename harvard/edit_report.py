from harvard.reference_research import ResearchReportReference
from harvard.edit_reference import EditReference

class EditResearchReportReference(EditReference):

    def edit(self, reference: ResearchReportReference = None):
        values = super().edit(reference)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        return ResearchReportReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            publisher= values['publisher'],
            place= values['place'])

    def get_type(self):
        return ResearchReportReference.get_type()