# Generated by Django 4.2.1 on 2023-05-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendship_app', '0006_alter_favorite_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]