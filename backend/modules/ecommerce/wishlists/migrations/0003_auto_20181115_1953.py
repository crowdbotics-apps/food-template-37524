# Generated by Django 2.0.7 on 2018-11-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0002_auto_20160111_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date created'),
        ),
    ]
