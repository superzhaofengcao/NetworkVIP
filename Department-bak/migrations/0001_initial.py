# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department_level_one'
        db.create_table(u'Department_department_level_one', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Department', ['Department_level_one'])

        # Adding model 'Department_level_two'
        db.create_table(u'Department_department_level_two', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('top_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Department.Department_level_one'])),
        ))
        db.send_create_signal(u'Department', ['Department_level_two'])

        # Adding model 'WorkArea'
        db.create_table(u'Department_workarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workspace', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Department', ['WorkArea'])

        # Adding model 'Service'
        db.create_table(u'Department_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num_port', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('service_type', self.gf('django.db.models.fields.CharField')(default='TCP', max_length=10)),
            ('service_descr', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Department', ['Service'])

        # Adding model 'PrivateIPAddress'
        db.create_table(u'Department_privateipaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ipaddress', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('ip_workspace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Department.WorkArea'])),
        ))
        db.send_create_signal(u'Department', ['PrivateIPAddress'])

        # Adding model 'Users'
        db.create_table(u'Department_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=11)),
        ))
        db.send_create_signal(u'Department', ['Users'])

        # Adding model 'PublicIPAddress'
        db.create_table(u'Department_publicipaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ipaddress', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('ip_workspace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Department.WorkArea'])),
            ('ip_private', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Department.PrivateIPAddress'])),
        ))
        db.send_create_signal(u'Department', ['PublicIPAddress'])

        # Adding M2M table for field ip_service_public on 'PublicIPAddress'
        m2m_table_name = db.shorten_name(u'Department_publicipaddress_ip_service_public')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publicipaddress', models.ForeignKey(orm[u'Department.publicipaddress'], null=False)),
            ('service', models.ForeignKey(orm[u'Department.service'], null=False))
        ))
        db.create_unique(m2m_table_name, ['publicipaddress_id', 'service_id'])

        # Adding M2M table for field ip_user on 'PublicIPAddress'
        m2m_table_name = db.shorten_name(u'Department_publicipaddress_ip_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publicipaddress', models.ForeignKey(orm[u'Department.publicipaddress'], null=False)),
            ('users', models.ForeignKey(orm[u'Department.users'], null=False))
        ))
        db.create_unique(m2m_table_name, ['publicipaddress_id', 'users_id'])


    def backwards(self, orm):
        # Deleting model 'Department_level_one'
        db.delete_table(u'Department_department_level_one')

        # Deleting model 'Department_level_two'
        db.delete_table(u'Department_department_level_two')

        # Deleting model 'WorkArea'
        db.delete_table(u'Department_workarea')

        # Deleting model 'Service'
        db.delete_table(u'Department_service')

        # Deleting model 'PrivateIPAddress'
        db.delete_table(u'Department_privateipaddress')

        # Deleting model 'Users'
        db.delete_table(u'Department_users')

        # Deleting model 'PublicIPAddress'
        db.delete_table(u'Department_publicipaddress')

        # Removing M2M table for field ip_service_public on 'PublicIPAddress'
        db.delete_table(db.shorten_name(u'Department_publicipaddress_ip_service_public'))

        # Removing M2M table for field ip_user on 'PublicIPAddress'
        db.delete_table(db.shorten_name(u'Department_publicipaddress_ip_user'))


    models = {
        u'Department.department_level_one': {
            'Meta': {'object_name': 'Department_level_one'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Department.department_level_two': {
            'Meta': {'object_name': 'Department_level_two'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'top_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Department.Department_level_one']"})
        },
        u'Department.privateipaddress': {
            'Meta': {'object_name': 'PrivateIPAddress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_workspace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Department.WorkArea']"}),
            'ipaddress': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
        },
        u'Department.publicipaddress': {
            'Meta': {'object_name': 'PublicIPAddress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_private': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Department.PrivateIPAddress']"}),
            'ip_service_public': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Department.Service']", 'symmetrical': 'False'}),
            'ip_user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Department.Users']", 'symmetrical': 'False'}),
            'ip_workspace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Department.WorkArea']"}),
            'ipaddress': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
        },
        u'Department.service': {
            'Meta': {'object_name': 'Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_port': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'service_descr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'service_type': ('django.db.models.fields.CharField', [], {'default': "'TCP'", 'max_length': '10'})
        },
        u'Department.users': {
            'Meta': {'object_name': 'Users'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'Department.workarea': {
            'Meta': {'object_name': 'WorkArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workspace': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['Department']