# Generated by Django 2.2.7 on 2020-02-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_save',
            field=models.BooleanField(default=False),
        ),
    ]
