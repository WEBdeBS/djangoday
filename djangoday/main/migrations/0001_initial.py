# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CallForPaper'
        db.create_table('main_callforpaper', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cognome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['CallForPaper'])


    def backwards(self, orm):
        
        # Deleting model 'CallForPaper'
        db.delete_table('main_callforpaper')


    models = {
        'main.callforpaper': {
            'Meta': {'object_name': 'CallForPaper'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'cognome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']
