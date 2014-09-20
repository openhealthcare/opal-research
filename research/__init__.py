"""
Plugin definition
"""
from opal.utils import OpalPlugin

from research.flow import get_study_flows
from research.schema import get_study_schemas
from research.teams import get_study_teams

class ResearchStudyPlugin(OpalPlugin):
    javascripts = {
        'opal.controllers': [
            'js/research/controllers/research_hospital_number.js'
        ]
    }
    def restricted_teams(self, user):
        return get_study_teams(user)

    def list_schemas(self):
        return get_study_schemas()

    def flows(self):
        return get_study_flows()
