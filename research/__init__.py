"""
Plugin definition
"""
from opal.utils import OpalPlugin

from research.teams import get_study_teams

class ResearchStudyPlugin(OpalPlugin):
    def restricted_teams(self, user):
        return get_study_teams(user)
