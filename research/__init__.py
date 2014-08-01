"""
Plugin definition
"""
from opal.utils import OpalPlugin

from research.teams import get_study_teams
from research.schema import get_study_schemas

class ResearchStudyPlugin(OpalPlugin):
    def restricted_teams(self, user):
        return get_study_teams(user)

    def list_schemas(self):
        return get_study_schemas()
