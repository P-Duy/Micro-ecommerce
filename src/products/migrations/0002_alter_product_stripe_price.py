# Generated by Django 4.1.9 on 2023-06-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stripe_price',
            field=models.IntegerField(default=999),
        ),
    ]
