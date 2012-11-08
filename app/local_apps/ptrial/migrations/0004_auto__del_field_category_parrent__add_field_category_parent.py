# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Category.parrent'
        db.delete_column('ptrial_category', 'parrent_id')

        # Adding field 'Category.parent'
        db.add_column('ptrial_category', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ptrial.Category'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Category.parrent'
        db.add_column('ptrial_category', 'parrent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ptrial.Category'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Category.parent'
        db.delete_column('ptrial_category', 'parent_id')


    models = {
        'ptrial.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ptrial.Category']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ptrial.Subject']"}),
            'url_key': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'blank': 'True'})
        },
        'ptrial.example': {
            'Meta': {'object_name': 'Example'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ptrial.Category']"}),
            'entering': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'procedure': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'ptrial.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'url_key': ('django.db.models.fields.SlugField', [], {'max_length': '8', 'blank': 'True'})
        }
    }

    complete_apps = ['ptrial']