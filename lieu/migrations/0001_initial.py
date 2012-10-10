# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Geohash'
        db.create_table('lieu_geohash', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Hash', self.gf('django.db.models.fields.TextField')(max_length=2048, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Geohash'])

        # Adding model 'GPS'
        db.create_table('lieu_gps', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Coord', self.gf('django.db.models.fields.TextField')(max_length=2048, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['GPS'])

        # Adding model 'Rue'
        db.create_table('lieu_rue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('GeoHash', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Geohash'], null=True, blank=True)),
            ('GPS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.GPS'], null=True, blank=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Rue'])

        # Adding model 'Adresse'
        db.create_table('lieu_adresse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Numero', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
            ('GeoHash', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Geohash'], null=True, blank=True)),
            ('GPS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.GPS'], null=True, blank=True)),
            ('Rue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Rue'], null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Adresse'])

        # Adding model 'CP'
        db.create_table('lieu_cp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('GeoHash', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Geohash'], null=True, blank=True)),
            ('GPS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.GPS'], null=True, blank=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['CP'])

        # Adding model 'Pays'
        db.create_table('lieu_pays', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Pays'])

        # Adding model 'TypeTransport'
        db.create_table('lieu_typetransport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['TypeTransport'])

        # Adding model 'Ligne'
        db.create_table('lieu_ligne', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('TypeTransport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.TypeTransport'], null=True, blank=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Ligne'])

        # Adding model 'Region'
        db.create_table('lieu_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Region'])

        # Adding model 'Station'
        db.create_table('lieu_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Station'])

        # Adding M2M table for field Ligne on 'Station'
        db.create_table('lieu_station_Ligne', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('station', models.ForeignKey(orm['lieu.station'], null=False)),
            ('ligne', models.ForeignKey(orm['lieu.ligne'], null=False))
        ))
        db.create_unique('lieu_station_Ligne', ['station_id', 'ligne_id'])

        # Adding model 'Ville'
        db.create_table('lieu_ville', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('GeoHash', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Geohash'], null=True, blank=True)),
            ('GPS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.GPS'], null=True, blank=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Ville'])

        # Adding model 'Lieu'
        db.create_table('lieu_lieu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('GeoHash', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Geohash'], null=True, blank=True)),
            ('GPS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.GPS'], null=True, blank=True)),
            ('Ville', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Ville'], null=True, blank=True)),
            ('CP', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.CP'], null=True, blank=True)),
            ('Region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Region'], null=True, blank=True)),
            ('Pays', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lieu.Pays'], null=True, blank=True)),
        ))
        db.send_create_signal('lieu', ['Lieu'])

        # Adding M2M table for field Adresse on 'Lieu'
        db.create_table('lieu_lieu_Adresse', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lieu', models.ForeignKey(orm['lieu.lieu'], null=False)),
            ('adresse', models.ForeignKey(orm['lieu.adresse'], null=False))
        ))
        db.create_unique('lieu_lieu_Adresse', ['lieu_id', 'adresse_id'])

        # Adding M2M table for field Station on 'Lieu'
        db.create_table('lieu_lieu_Station', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lieu', models.ForeignKey(orm['lieu.lieu'], null=False)),
            ('station', models.ForeignKey(orm['lieu.station'], null=False))
        ))
        db.create_unique('lieu_lieu_Station', ['lieu_id', 'station_id'])


    def backwards(self, orm):
        # Deleting model 'Geohash'
        db.delete_table('lieu_geohash')

        # Deleting model 'GPS'
        db.delete_table('lieu_gps')

        # Deleting model 'Rue'
        db.delete_table('lieu_rue')

        # Deleting model 'Adresse'
        db.delete_table('lieu_adresse')

        # Deleting model 'CP'
        db.delete_table('lieu_cp')

        # Deleting model 'Pays'
        db.delete_table('lieu_pays')

        # Deleting model 'TypeTransport'
        db.delete_table('lieu_typetransport')

        # Deleting model 'Ligne'
        db.delete_table('lieu_ligne')

        # Deleting model 'Region'
        db.delete_table('lieu_region')

        # Deleting model 'Station'
        db.delete_table('lieu_station')

        # Removing M2M table for field Ligne on 'Station'
        db.delete_table('lieu_station_Ligne')

        # Deleting model 'Ville'
        db.delete_table('lieu_ville')

        # Deleting model 'Lieu'
        db.delete_table('lieu_lieu')

        # Removing M2M table for field Adresse on 'Lieu'
        db.delete_table('lieu_lieu_Adresse')

        # Removing M2M table for field Station on 'Lieu'
        db.delete_table('lieu_lieu_Station')


    models = {
        'lieu.adresse': {
            'GPS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.GPS']", 'null': 'True', 'blank': 'True'}),
            'GeoHash': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Geohash']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Adresse'},
            'Numero': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'Rue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Rue']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.cp': {
            'GPS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.GPS']", 'null': 'True', 'blank': 'True'}),
            'GeoHash': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Geohash']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'CP'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.geohash': {
            'Hash': ('django.db.models.fields.TextField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Geohash'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.gps': {
            'Coord': ('django.db.models.fields.TextField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'GPS'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.lieu': {
            'Adresse': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lieu.Adresse']", 'null': 'True', 'blank': 'True'}),
            'CP': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.CP']", 'null': 'True', 'blank': 'True'}),
            'GPS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.GPS']", 'null': 'True', 'blank': 'True'}),
            'GeoHash': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Geohash']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Lieu'},
            'Pays': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Pays']", 'null': 'True', 'blank': 'True'}),
            'Region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Region']", 'null': 'True', 'blank': 'True'}),
            'Station': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lieu.Station']", 'null': 'True', 'blank': 'True'}),
            'Ville': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Ville']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.ligne': {
            'Meta': {'object_name': 'Ligne'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'TypeTransport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.TypeTransport']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.pays': {
            'Meta': {'object_name': 'Pays'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.region': {
            'Meta': {'object_name': 'Region'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.rue': {
            'GPS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.GPS']", 'null': 'True', 'blank': 'True'}),
            'GeoHash': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Geohash']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rue'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.station': {
            'Ligne': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lieu.Ligne']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Station'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.typetransport': {
            'Meta': {'object_name': 'TypeTransport'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieu.ville': {
            'GPS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.GPS']", 'null': 'True', 'blank': 'True'}),
            'GeoHash': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lieu.Geohash']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Ville'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['lieu']