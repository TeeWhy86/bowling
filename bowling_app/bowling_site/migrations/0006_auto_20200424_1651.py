# Generated by Django 3.0.5 on 2020-04-24 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bowling_site', '0005_league_lanes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stats',
            new_name='Stat',
        ),
    ]