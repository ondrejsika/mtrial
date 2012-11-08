# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

import random

def rand():
    return random.randint(99,99999999999)

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Example.number'
        db.add_column('ptrial_example', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=rand),
                      keep_default=False)

        # Adding unique constraint on 'Example', fields ['category', 'number']
        db.create_unique('ptrial_example', ['category_id', 'number'])


    def backwards(self, orm):
        # Removing unique constraint on 'Example', fields ['category', 'number']
        db.delete_unique('ptrial_example', ['category_id', 'number'])

        # Deleting field 'Example.number'
        db.delete_column('ptrial_example', 'number')


    models = {
        'ptrial.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ptrial.Category']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ptrial.Subject']"}),
            'uk': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'ptrial.example': {
            'Meta': {'unique_together': "(('number', 'category'),)", 'object_name': 'Example'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ptrial.Category']"}),
            'entering': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'procedure': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'ptrial.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'uk': ('django.db.models.fields.SlugField', [], {'max_length': '8', 'blank': 'True'})
        }
    }

    complete_apps = ['ptrial']
