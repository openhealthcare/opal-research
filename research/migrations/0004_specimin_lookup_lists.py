# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        specimins = [
            ('Broncho-alveolar lavage', ('BAL',)),
            ('Induced sputum', None),
            ('Sputum', None),
            ('Tracheal aspirate', ('TA',)), 
            ('Endotracheal secretions', ('ET secretions', 'ETT')),
            ('Non-directed bronchoalveolar lavage', ('NBL')),
            ('Bronchial aspirates', None)
        ]

        content_type, _ = orm['contenttypes.ContentType'].objects.get_or_create(app_label='research', 
                                                                             model='specimin')
        for specimin, synonyms in specimins:
            specimin = orm.Specimin(name=specimin)
            specimin.save()
            if not synonyms:
                continue
            for synonym in synonyms:
                s = orm['opal.Synonym']
                s = s(name=synonym, content_type=content_type, object_id=specimin.id)
                s.save()


        appearances = [
            'Salivary',
            'Mucosalivary',
            'Mucoid',
            'Mucopurulent',
            'Purulent'
        ]
         
        for appearance in appearances:
            ap = orm.Specimin_appearance(name=appearance)
            ap.save()
   
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

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
        u'research.labspecimin': {
            'Meta': {'object_name': 'LabSpecimin'},
            'appearance_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Specimin_appearance']", 'null': 'True', 'blank': 'True'}),
            'appearance_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'biobanking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_biobanked': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_collected': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_shipped': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            'epithelial_cell': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specimin_type_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Specimin']", 'null': 'True', 'blank': 'True'}),
            'specimin_type_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume_biobanked': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'white_blood_cells': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
    symmetrical = True
