# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LabTest'
        db.create_table(u'research_labtest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consistency_token', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Episode'], null=True)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_ordered', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('microscopy', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('organism', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sensitive_antibiotics', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('resistant_antibiotics', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('igm', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('igg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('vca_igm', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('vca_igg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ebna_igg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('hbsag', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('anti_hbs', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('anti_hbcore_igm', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('anti_hbcore_igg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rpr', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('tppa', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('viral_load', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('parasitaemia', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('hsv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('vzv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('syphilis', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('c_difficile_antigen', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('c_difficile_toxin', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('species', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('hsv_1', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('hsv_2', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('enterovirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cmv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ebv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('influenza_a', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('influenza_b', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('parainfluenza', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('metapneumovirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rsv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('adenovirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('norovirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rotavirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('giardia', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('entamoeba_histolytica', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cryptosporidium', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('significant_organism', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('retrieved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_retrieved', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('biobanked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('freezer_box_number', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('esbl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('carbapenemase', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('antimicrobial_suceptability_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Antimicrobial_susceptability'], null=True, blank=True)),
            ('antimicrobial_suceptability_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('organism_details_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Organism_details'], null=True, blank=True)),
            ('organism_details_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'research', ['LabTest'])

        # Adding model 'Antimicrobial_susceptability'
        db.create_table(u'research_antimicrobial_susceptability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'research', ['Antimicrobial_susceptability'])


    def backwards(self, orm):
        # Deleting model 'LabTest'
        db.delete_table(u'research_labtest')

        # Deleting model 'Antimicrobial_susceptability'
        db.delete_table(u'research_antimicrobial_susceptability')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'opal.episode': {
            'Meta': {'object_name': 'Episode'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_of_admission': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'discharge_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Patient']"})
        },
        u'opal.patient': {
            'Meta': {'object_name': 'Patient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'opal.synonym': {
            'Meta': {'unique_together': "(('name', 'content_type'),)", 'object_name': 'Synonym'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'research.antimicrobial_susceptability': {
            'Meta': {'ordering': "['name']", 'object_name': 'Antimicrobial_susceptability'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'research.labspecimin': {
            'Meta': {'object_name': 'LabSpecimin'},
            'appearance_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Specimin_appearance']", 'null': 'True', 'blank': 'True'}),
            'appearance_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'biobanking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_biobanked': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_collected': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_tested': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            'epithelial_cell': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specimin_type_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Specimin']", 'null': 'True', 'blank': 'True'}),
            'specimin_type_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume_biobanked': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'white_blood_cells': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'research.labtest': {
            'Meta': {'object_name': 'LabTest'},
            'adenovirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'anti_hbcore_igg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'anti_hbcore_igm': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'anti_hbs': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'antimicrobial_suceptability_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Antimicrobial_susceptability']", 'null': 'True', 'blank': 'True'}),
            'antimicrobial_suceptability_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'biobanked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'c_difficile_antigen': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'c_difficile_toxin': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'carbapenemase': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cmv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'cryptosporidium': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'date_ordered': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_retrieved': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ebna_igg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ebv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'entamoeba_histolytica': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'enterovirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            'esbl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'freezer_box_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'giardia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hbsag': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hsv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hsv_1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hsv_2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'igm': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'influenza_a': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'influenza_b': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'metapneumovirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'microscopy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'norovirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'organism': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'organism_details_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Organism_details']", 'null': 'True', 'blank': 'True'}),
            'organism_details_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parainfluenza': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'parasitaemia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'resistant_antibiotics': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'retrieved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rotavirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rpr': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rsv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'sensitive_antibiotics': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'significant_organism': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'syphilis': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tppa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'vca_igg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'vca_igm': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'viral_load': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'vzv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'research.organism_details': {
            'Meta': {'ordering': "['name']", 'object_name': 'Organism_details'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'research.researchstudy': {
            'Meta': {'object_name': 'ResearchStudy'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clinical_lead': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'clinical_lead_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research_nurse': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'research_nurse_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'researcher': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'researcher_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'scientist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scientist_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'research.specimin': {
            'Meta': {'ordering': "['name']", 'object_name': 'Specimin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'research.specimin_appearance': {
            'Meta': {'ordering': "['name']", 'object_name': 'Specimin_appearance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['research']