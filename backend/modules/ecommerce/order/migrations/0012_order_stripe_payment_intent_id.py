# Generated by Django 2.2.28 on 2022-09-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20200801_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_payment_intent_id',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
