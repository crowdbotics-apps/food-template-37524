# Generated by Django 2.2.28 on 2022-09-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_auto_20181115_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
