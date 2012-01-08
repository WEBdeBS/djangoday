# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CallForPaper.tipo_intervento'
        db.add_column('main_callforpaper', 'tipo_intervento', self.gf('django.db.models.fields.CharField')(default='Overview', max_length=20), keep_default=False)

        # Adding field 'CallForPaper.livello'
        db.add_column('main_callforpaper', 'livello', self.gf('django.db.models.fields.CharField')(default='Beginner', max_length=20), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CallForPaper.tipo_intervento'
        db.delete_column('main_callforpaper', 'tipo_intervento')

        # Deleting field 'CallForPaper.livello'
        db.delete_column('main_callforpaper', 'livello')


    models = {
        'main.callforpaper': {
            'Meta': {'object_name': 'CallForPaper'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'cognome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'livello': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'tipo_intervento': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']
