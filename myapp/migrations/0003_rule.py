# Generated by Django 2.2 on 2020-11-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201125_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun', models.CharField(blank=True, max_length=10, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('timeframe', models.IntegerField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('total_value', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
