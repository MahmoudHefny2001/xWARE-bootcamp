# Generated by Django 4.1 on 2022-08-19 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_rename_boards_board'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='message',
            new_name='essay',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='subject',
            new_name='topic',
        ),
    ]
