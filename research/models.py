"""
Models for the OPAL Research study plugin
"""
from django.contrib.auth.models import User
from django.db import models

class ResearchStudy(models.Model):
    """
    An individul research study being conducted.

    We store some metadata and study personnel by role. 
    """
    name           = models.CharField(max_length=200)
    active         = models.BooleanField(default=False)
    clinical_lead  = models.ManyToManyField(User, blank=True, null=True, 
                                            related_name='clinical_lead_user')
    researcher     = models.ManyToManyField(User, blank=True, null=True,
                                            related_name='researcher_user')
    research_nurse = models.ManyToManyField(User, blank=True, null=True,
                                            related_name='research_nurse_user')
    scientist      = models.ManyToManyField(User, blank=True, null=True,
                                            related_name='scientist_user')

    def __unicode__(self):
        return unicode(self.name)
