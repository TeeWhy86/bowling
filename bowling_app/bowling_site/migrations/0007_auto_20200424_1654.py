# Generated by Django 3.0.5 on 2020-04-24 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bowling_site', '0006_auto_20200424_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bowler',
            old_name='birthdate',
            new_name='Birth Date',
        ),
    ]
