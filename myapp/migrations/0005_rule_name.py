# Generated by Django 2.2 on 2020-11-26 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_event_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='name',
            field=models.CharField(default='hello world', max_length=30),
            preserve_default=False,
        ),
    ]