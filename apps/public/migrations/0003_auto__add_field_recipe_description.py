# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.description'
        db.add_column(u'public_recipe', 'description',
                      self.gf('django.db.models.fields.TextField')(default='old stuff...', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recipe.description'
        db.delete_column(u'public_recipe', 'description')


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'glycemic_index': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cook_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cook_time': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']