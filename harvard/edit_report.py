from harvard.reference_research import ResearchReportReference
from harvard.edit_reference import EditReference

class EditResearchReportReference(EditReference):
    """Editor for Research Reports"""

    def edit(self, reference: ResearchReportReference = None):
        """Edit or create the reference

        Args:
            reference: optional Reference, if None, the reference is simply created
        Returns:
            None
        """
        values = super().edit(reference)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        return ResearchReportReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            place= values['place'],
            publisher= values['publisher'])

    def get_type(self):
        """Returns the type handled by this editor
        
        Returns:
            ReferenceType
        """
        return ResearchReportReference.get_type()