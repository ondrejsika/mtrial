# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Category.url_key'
        db.alter_column('ptrial_category', 'url_key', self.gf('django.db.models.fields.SlugField')(max_length=32))

        # Changing field 'Category.name'
        db.alter_column('ptrial_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=32))

    def backwards(self, orm):

        # Changing field 'Category.url_key'
        db.alter_column('ptrial_category', 'url_key', self.gf('django.db.models.fields.SlugField')(max_length=8))

        # Changing field 'Category.name'
        db.alter_column('ptrial_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=8))

    models = {
        'ptrial.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'parrent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ptrial.Category']", 'null': 'True', 'blank': 'True'}),
            'url_key': ('django.db.models.fields.SlugField', [], {'max_length': '32'})
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
            'url_key': ('django.db.models.fields.SlugField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['ptrial']