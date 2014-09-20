"""
Models for the OPAL Research study plugin
"""
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

from opal.models import EpisodeSubrecord, Synonym
from opal.utils.fields import ForeignKeyOrFreeText
from opal.utils.models import lookup_list


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
        return self.name.lower().replace(' ', '_').replace('-', '_')


SpeciminLookupList = type(*lookup_list('specimin', module=__name__))
SpeciminAppearanceLookupList = type(*lookup_list('specimin_appearance', module=__name__))
OrganismDetailsLookupList = type(*lookup_list('organism_details', module=__name__))
AntimicrobialSusceptabilityLookupList = type(*lookup_list('antimicrobial_susceptability', module=__name__))
    
class LabSpecimin(EpisodeSubrecord):
    _sort = 'date_collected'

    specimin_type     = ForeignKeyOrFreeText(SpeciminLookupList)
    date_collected    = models.DateField(blank=True, null=True)
    volume            = models.CharField(max_length=200, blank=True, null=True)
    appearance        = ForeignKeyOrFreeText(SpeciminAppearanceLookupList)
    epithelial_cell   = models.CharField(max_length=200, blank=True, null=True)
    white_blood_cells = models.CharField(max_length=200, blank=True, null=True)
    date_tested       = models.DateField(blank=True, null=True)
    external_id       = models.CharField(max_length=200, blank=True, null=True)
    biobanking        = models.BooleanField(default=False)
    date_biobanked    = models.DateField(blank=True, null=True)
    volume_biobanked  = models.CharField(max_length=200, blank=True, null=True)


# This is based on the investigations record type from elCID
class LabTest(EpisodeSubrecord):
    _sort = 'date_ordered'

    """
    Begin elCID.models.investigations fields
    """

    test                  = models.CharField(max_length=255)
    date_ordered          = models.DateField(null=True, blank=True)
    details               = models.CharField(max_length=255, blank=True)
    microscopy            = models.CharField(max_length=255, blank=True)
    organism              = models.CharField(max_length=255, blank=True)
    sensitive_antibiotics = models.CharField(max_length=255, blank=True)
    resistant_antibiotics = models.CharField(max_length=255, blank=True)
    result                = models.CharField(max_length=255, blank=True)
    igm                   = models.CharField(max_length=20, blank=True)
    igg                   = models.CharField(max_length=20, blank=True)
    vca_igm               = models.CharField(max_length=20, blank=True)
    vca_igg               = models.CharField(max_length=20, blank=True)
    ebna_igg              = models.CharField(max_length=20, blank=True)
    hbsag                 = models.CharField(max_length=20, blank=True)
    anti_hbs              = models.CharField(max_length=20, blank=True)
    anti_hbcore_igm       = models.CharField(max_length=20, blank=True)
    anti_hbcore_igg       = models.CharField(max_length=20, blank=True)
    rpr                   = models.CharField(max_length=20, blank=True)
    tppa                  = models.CharField(max_length=20, blank=True)
    viral_load            = models.CharField(max_length=20, blank=True)
    parasitaemia          = models.CharField(max_length=20, blank=True)
    hsv                   = models.CharField(max_length=20, blank=True)
    vzv                   = models.CharField(max_length=20, blank=True)
    syphilis              = models.CharField(max_length=20, blank=True)
    c_difficile_antigen   = models.CharField(max_length=20, blank=True)
    c_difficile_toxin     = models.CharField(max_length=20, blank=True)
    species               = models.CharField(max_length=20, blank=True)
    hsv_1                 = models.CharField(max_length=20, blank=True)
    hsv_2                 = models.CharField(max_length=20, blank=True)
    enterovirus           = models.CharField(max_length=20, blank=True)
    cmv                   = models.CharField(max_length=20, blank=True)
    ebv                   = models.CharField(max_length=20, blank=True)
    influenza_a           = models.CharField(max_length=20, blank=True)
    influenza_b           = models.CharField(max_length=20, blank=True)
    parainfluenza         = models.CharField(max_length=20, blank=True)
    metapneumovirus       = models.CharField(max_length=20, blank=True)
    rsv                   = models.CharField(max_length=20, blank=True)
    adenovirus            = models.CharField(max_length=20, blank=True)
    norovirus             = models.CharField(max_length=20, blank=True)
    rotavirus             = models.CharField(max_length=20, blank=True)
    giardia               = models.CharField(max_length=20, blank=True)
    entamoeba_histolytica = models.CharField(max_length=20, blank=True)
    cryptosporidium       = models.CharField(max_length=20, blank=True)
    """
    End elCID.models.investigations fields
    """
    significant_organism  = models.BooleanField(default=False)
    organism_details      = ForeignKeyOrFreeText(OrganismDetailsLookupList)
    antimicrobial_suceptability = ForeignKeyOrFreeText(AntimicrobialSusceptabilityLookupList)
    retrieved = models.BooleanField(default=False)
    date_retrieved = models.DateField(null=True, blank=True)
    biobanked = models.BooleanField(default=False)
    freezer_box_number = models.CharField(max_length=200, blank=True, null=True)
    esbl = models.BooleanField(default=False)
    carbapenemase = models.BooleanField(default=False)


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
                          restricted=True,
                          title=study.name)
        study_team.save()

        teams = [
            ('Scientist', study.team_name + '_scientist'),
            ('Research Nurse', study.team_name + '_research_nurse')
        ]

        for title, name in teams:
            team = Team(name=name, title=title, 
                        active=True, parent=study_team, restricted=True, 
                        direct_add=False)
            team.save()
    return
