# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Subject.url_key'
        db.delete_column('mtrial_subject', 'url_key')

        # Adding field 'Subject.uk'
        db.add_column('mtrial_subject', 'uk',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=8, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Subject.url_key'
        db.add_column('mtrial_subject', 'url_key',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=8, blank=True),
                      keep_default=False)

        # Deleting field 'Subject.uk'
        db.delete_column('mtrial_subject', 'uk')


    models = {
        'mtrial.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mtrial.Category']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mtrial.Subject']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url_key': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'blank': 'True'})
        },
        'mtrial.example': {
            'Meta': {'object_name': 'Example'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mtrial.Category']"}),
            'entering': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'procedure': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'mtrial.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'uk': ('django.db.models.fields.SlugField', [], {'max_length': '8', 'blank': 'True'})
        }
    }

    complete_apps = ['mtrial']