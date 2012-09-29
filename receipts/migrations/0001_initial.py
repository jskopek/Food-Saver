# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Receipt'
        db.create_table('receipts_receipt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('receipts', ['Receipt'])

        # Adding M2M table for field products on 'Receipt'
        db.create_table('receipts_receipt_products', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('receipt', models.ForeignKey(orm['receipts.receipt'], null=False)),
            ('product', models.ForeignKey(orm['products.product'], null=False))
        ))
        db.create_unique('receipts_receipt_products', ['receipt_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'Receipt'
        db.delete_table('receipts_receipt')

        # Removing M2M table for field products on 'Receipt'
        db.delete_table('receipts_receipt_products')


    models = {
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'expires_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'perishable': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'receipts.receipt': {
            'Meta': {'object_name': 'Receipt'},
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Product']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['receipts']