# Generated by Django 3.2 on 2022-08-21 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_catogery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catogery',
            new_name='Category',
        ),
    ]
