# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ManipulationLog'
        db.create_table('dynamic_manipulation_manipulationlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rule', self.gf('django.db.models.fields.related.ForeignKey')(related_name='manipulation_logs', to=orm['dynamic_rules.Rule'])),
            ('trigger_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='manipulation_triggers', to=orm['contenttypes.ContentType'])),
            ('trigger_model_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('side_effect_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='manipulation_side_effects', to=orm['contenttypes.ContentType'])),
            ('side_effect_model_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('dynamic_manipulation', ['ManipulationLog'])


    def backwards(self, orm):
        
        # Deleting model 'ManipulationLog'
        db.delete_table('dynamic_manipulation_manipulationlog')


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
            'side_effect_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'manipulation_side_effects'", 'to': "orm['contenttypes.ContentType']"}),
            'side_effect_model_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['dynamic_manipulation']
