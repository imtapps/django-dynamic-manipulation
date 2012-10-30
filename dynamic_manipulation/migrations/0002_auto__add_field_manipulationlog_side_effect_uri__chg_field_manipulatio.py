# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    no_dry_run = True

    def forwards(self, orm):
        # Adding field 'ManipulationLog.side_effect_uri'
        db.add_column('dynamic_manipulation_manipulationlog', 'side_effect_uri',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # Changing field 'ManipulationLog.side_effect_content_type'
        db.alter_column('dynamic_manipulation_manipulationlog', 'side_effect_content_type_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['contenttypes.ContentType']))

        # Changing field 'ManipulationLog.side_effect_model_id'
        db.alter_column('dynamic_manipulation_manipulationlog', 'side_effect_model_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

    def backwards(self, orm):
        db.delete_column('dynamic_manipulation_manipulationlog', 'side_effect_uri')
        for record in orm.ManipulationLog.objects.filter(side_effect_model_id=None):
            record.delete()




    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dynamic_manipulation.manipulationlog': {
            'Meta': {'object_name': 'ManipulationLog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'manipulation_logs'", 'to': "orm['dynamic_rules.Rule']"}),
            'side_effect_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'manipulation_side_effects'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'side_effect_model_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'side_effect_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'trigger_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'manipulation_triggers'", 'to': "orm['contenttypes.ContentType']"}),
            'trigger_model_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'dynamic_rules.rule': {
            'Meta': {'object_name': 'Rule'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'dynamic_fields': ('django_fields.fields.PickleField', [], {}),
            'group_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secondary_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        }
    }

    complete_apps = ['dynamic_manipulation']