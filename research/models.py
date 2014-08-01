"""
Models for the OPAL Research study plugin
"""
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

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

    @property
    def team_name(self):
        """
        Return the sanitised team name.
        """
        return self.name.lower().replace(' ', '_')

    
@receiver(models.signals.post_save, sender=ResearchStudy)
def create_teams_for_study(sender, **kwargs):
    """
    If we have just created a new study we should now set up the teams
    for that study. 
    """
    if kwargs['created']:
        study = kwargs['instance']
        from opal.models import Team

        study_team = Team(name=study.team_name,
                          title=study.name)
        study_team.save()

        teams = [
            ('Scientist', 'scientist'),
            ('Research Nurse', 'research_nurse')
        ]

        for title, name in teams:
            team = Team(name=name, title=title, active=True, parent=study_team, restricted=True)
            team.save()
    return
