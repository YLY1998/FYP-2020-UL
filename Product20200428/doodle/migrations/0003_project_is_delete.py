# Generated by Django 2.2.7 on 2020-02-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0002_project_is_save'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
