# Generated by Django 4.2.4 on 2023-08-07 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_connection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connection',
            old_name='user1',
            new_name='from_user',
        ),
        migrations.RenameField(
            model_name='connection',
            old_name='user1_relationship',
            new_name='relationship1',
        ),
        migrations.RenameField(
            model_name='connection',
            old_name='user2_relationship',
            new_name='relationship2',
        ),
        migrations.RenameField(
            model_name='connection',
            old_name='user2',
            new_name='to_user',
        ),
    ]
