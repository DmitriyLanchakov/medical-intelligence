# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Discussion'
        db.create_table(u'messaging_discussion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
        ))
        db.send_create_signal(u'messaging', ['Discussion'])

        # Adding M2M table for field members on 'Discussion'
        db.create_table(u'messaging_discussion_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('discussion', models.ForeignKey(orm[u'messaging.discussion'], null=False)),
            ('medintuser', models.ForeignKey(orm[u'common.medintuser'], null=False))
        ))
        db.create_unique(u'messaging_discussion_members', ['discussion_id', 'medintuser_id'])

        # Deleting field 'Message.deleted_by_recipient'
        db.delete_column(u'messaging_message', 'deleted_by_recipient')

        # Deleting field 'Message.deleted_by_sender'
        db.delete_column(u'messaging_message', 'deleted_by_sender')

        # Deleting field 'Message.send_at'
        db.delete_column(u'messaging_message', 'send_at')

        # Deleting field 'Message.read_at'
        db.delete_column(u'messaging_message', 'read_at')

        # Deleting field 'Message.subject'
        db.delete_column(u'messaging_message', 'subject')

        # Deleting field 'Message.recipient'
        db.delete_column(u'messaging_message', 'recipient_id')

        # Adding field 'Message.sent'
        db.add_column(u'messaging_message', 'sent',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 3, 21, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Discussion'
        db.delete_table(u'messaging_discussion')

        # Removing M2M table for field members on 'Discussion'
        db.delete_table('messaging_discussion_members')

        # Adding field 'Message.deleted_by_recipient'
        db.add_column(u'messaging_message', 'deleted_by_recipient',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Message.deleted_by_sender'
        db.add_column(u'messaging_message', 'deleted_by_sender',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Message.send_at'
        raise RuntimeError("Cannot reverse this migration. 'Message.send_at' and its values cannot be restored.")
        # Adding field 'Message.read_at'
        db.add_column(u'messaging_message', 'read_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Message.subject'
        db.add_column(u'messaging_message', 'subject',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Message.recipient'
        raise RuntimeError("Cannot reverse this migration. 'Message.recipient' and its values cannot be restored.")
        # Deleting field 'Message.sent'
        db.delete_column(u'messaging_message', 'sent')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'common.medintuser': {
            'Meta': {'object_name': 'MedintUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.IntegerField', [], {}),
            'user_info': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'user'", 'unique': 'True', 'null': 'True', 'to': u"orm['common.UserInfo']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'common.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'messaging.discussion': {
            'Meta': {'object_name': 'Discussion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['common.MedintUser']", 'symmetrical': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'messaging.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_messages'", 'to': u"orm['common.MedintUser']"}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['messaging']