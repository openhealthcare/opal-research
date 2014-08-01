# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ResearchStudy'
        db.create_table(u'research_researchstudy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'research', ['ResearchStudy'])

        # Adding M2M table for field clinical_lead on 'ResearchStudy'
        m2m_table_name = db.shorten_name(u'research_researchstudy_clinical_lead')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('researchstudy', models.ForeignKey(orm[u'research.researchstudy'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['researchstudy_id', 'user_id'])

        # Adding M2M table for field researcher on 'ResearchStudy'
        m2m_table_name = db.shorten_name(u'research_researchstudy_researcher')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('researchstudy', models.ForeignKey(orm[u'research.researchstudy'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['researchstudy_id', 'user_id'])

        # Adding M2M table for field research_nurse on 'ResearchStudy'
        m2m_table_name = db.shorten_name(u'research_researchstudy_research_nurse')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('researchstudy', models.ForeignKey(orm[u'research.researchstudy'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['researchstudy_id', 'user_id'])

        # Adding M2M table for field scientist on 'ResearchStudy'
        m2m_table_name = db.shorten_name(u'research_researchstudy_scientist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('researchstudy', models.ForeignKey(orm[u'research.researchstudy'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['researchstudy_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'ResearchStudy'
        db.delete_table(u'research_researchstudy')

        # Removing M2M table for field clinical_lead on 'ResearchStudy'
        db.delete_table(db.shorten_name(u'research_researchstudy_clinical_lead'))

        # Removing M2M table for field researcher on 'ResearchStudy'
        db.delete_table(db.shorten_name(u'research_researchstudy_researcher'))

        # Removing M2M table for field research_nurse on 'ResearchStudy'
        db.delete_table(db.shorten_name(u'research_researchstudy_research_nurse'))

        # Removing M2M table for field scientist on 'ResearchStudy'
        db.delete_table(db.shorten_name(u'research_researchstudy_scientist'))


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
            'clinical_lead': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'clinical_lead_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research_nurse': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'research_nurse_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'researcher': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'researcher_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'scientist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scientist_user'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['research']