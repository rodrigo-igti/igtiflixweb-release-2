# Generated by Django 3.2.3 on 2021-05-29 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='idGenero',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='nome',
        ),
    ]
