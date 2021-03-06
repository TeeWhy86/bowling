# Generated by Django 3.0.5 on 2020-04-16 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bowling_site', '0002_auto_20200405_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='Bowler',
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('avg', models.FloatField()),
                ('hdcp', models.FloatField()),
                ('bowler1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bowling_site.Bowler')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game1', models.IntegerField()),
                ('game2', models.IntegerField()),
                ('game3', models.IntegerField()),
                ('total', models.IntegerField()),
                ('avg', models.FloatField()),
                ('hdcp', models.FloatField()),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bowling_site.Bowler')),
                ('teamid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bowling_site.Team')),
            ],
        ),
    ]
