# Generated by Django 2.0.9 on 2018-12-14 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mellitah', '0002_auto_20181214_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commenter',
            new_name='comments',
        ),
    ]
