# Generated by Django 3.2.3 on 2021-06-01 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductManager',
        ),
    ]