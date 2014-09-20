"""
Create/fetch schemas for our studies.
"""
import collections

from django.conf import settings

from opal.utils import stringport

from research.models import ResearchStudy

research_nurse_schema = stringport(settings.LIST_SCHEMA_RESEARCH_NURSE)
scientist_schema = stringport(settings.LIST_SCHEMA_SCIENTIST)

def get_study_schemas():
    """
    Return a dict of schemas to be used with our research studies.
    """
    schemas = collections.defaultdict(dict)
    for study in ResearchStudy.objects.filter(active=True):
        schemas[study.team_name][study.team_name + '_research_nurse'] = research_nurse_schema
        schemas[study.team_name][study.team_name + '_scientist'] = scientist_schema
    return schemas
