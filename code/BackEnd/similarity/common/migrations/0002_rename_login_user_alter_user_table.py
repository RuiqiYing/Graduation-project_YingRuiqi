# Generated by Django 4.0.4 on 2023-01-22 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
