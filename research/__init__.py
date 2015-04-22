"""
Plugin definition
"""
from opal.core.plugins import OpalPlugin

from research.flow import get_study_flows
from research.roles import get_study_roles
from research.schema import get_study_schemas
from research.teams import get_study_teams
from research.urls import urlpatterns

class ResearchStudyPlugin(OpalPlugin):
    urls        = urlpatterns
    javascripts = {
        'opal.controllers': [
            'js/research/controllers/research_hospital_number.js',
            'js/research/controllers/discharge.js'
        ]
    }
    def restricted_teams(self, user):
        return get_study_teams(user)

    def list_schemas(self):
        return get_study_schemas()

    def flows(self):
        return get_study_flows()

    def roles(self, user):
        return get_study_roles(user)
