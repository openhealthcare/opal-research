# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Antimicrobial_susceptability'
        db.delete_table(u'research_antimicrobial_susceptability')

        # Deleting model 'LabTest'
        db.delete_table(u'research_labtest')

        # Deleting model 'LabSpecimin'
        db.delete_table(u'research_labspecimin')

        # Deleting model 'Organism_details'
        db.delete_table(u'research_organism_details')

        # Deleting model 'Specimin'
        db.delete_table(u'research_specimin')

        # Deleting model 'Specimin_appearance'
        db.delete_table(u'research_specimin_appearance')


    def backwards(self, orm):
        # Adding model 'Antimicrobial_susceptability'
        db.create_table(u'research_antimicrobial_susceptability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
        ))
        db.send_create_signal(u'research', ['Antimicrobial_susceptability'])

        # Adding model 'LabTest'
        db.create_table(u'research_labtest', (
            ('consistency_token', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('significant_organism', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vca_igm', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('parainfluenza', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rpr', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('date_retrieved', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('anti_hbs', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rotavirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('norovirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('date_ordered', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('carbapenemase', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adenovirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('parasitaemia', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('metapneumovirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('syphilis', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rsv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cryptosporidium', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('vca_igg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('c_difficile_antigen', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('retrieved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('microscopy', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('vzv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('biobanked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entamoeba_histolytica', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cmv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('viral_load', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('enterovirus', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('freezer_box_number', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('ebv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('c_difficile_toxin', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('giardia', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('resistant_antibiotics', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('organism_details_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Organism_details'], null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('igg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('organism_details_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('ebna_igg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('anti_hbcore_igm', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tppa', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('igm', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('anti_hbcore_igg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('antimicrobial_suceptability_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Antimicrobial_susceptability'], null=True, blank=True)),
            ('esbl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hsv', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('antimicrobial_suceptability_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('hbsag', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Episode'], null=True)),
            ('influenza_a', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('influenza_b', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('species', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('hsv_2', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('hsv_1', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('organism', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sensitive_antibiotics', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'research', ['LabTest'])

        # Adding model 'LabSpecimin'
        db.create_table(u'research_labspecimin', (
            ('volume_biobanked', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('biobanking', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('consistency_token', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('date_biobanked', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('appearance_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Specimin_appearance'], null=True, blank=True)),
            ('specimin_type_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('date_tested', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_collected', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('epithelial_cell', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('specimin_type_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Specimin'], null=True, blank=True)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Episode'], null=True)),
            ('appearance_ft', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('external_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('white_blood_cells', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'research', ['LabSpecimin'])

        # Adding model 'Organism_details'
        db.create_table(u'research_organism_details', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
        ))
        db.send_create_signal(u'research', ['Organism_details'])

        # Adding model 'Specimin'
        db.create_table(u'research_specimin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
        ))
        db.send_create_signal(u'research', ['Specimin'])

        # Adding model 'Specimin_appearance'
        db.create_table(u'research_specimin_appearance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
        ))
        db.send_create_signal(u'research', ['Specimin_appearance'])


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
        u'research.researchstudy': {
            'Meta': {'object_name': 'ResearchStudy'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clinical_lead': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'clinical_lead_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research_nurse': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'research_nurse_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'researcher': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'researcher_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'scientist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scientist_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['research']