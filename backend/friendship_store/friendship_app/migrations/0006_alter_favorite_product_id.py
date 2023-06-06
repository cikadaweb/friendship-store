# Generated by Django 4.2.1 on 2023-05-28 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendship_app', '0005_alter_favorite_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='friendship_app.product'),
        ),
    ]
