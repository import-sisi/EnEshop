# Generated by Django 3.2.3 on 2021-06-20 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Cart',
            new_name='cart',
        ),
    ]
