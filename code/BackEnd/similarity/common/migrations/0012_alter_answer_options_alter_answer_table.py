# Generated by Django 4.0.4 on 2023-01-27 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_answer_questionbank_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='answer',
            table='answer',
        ),
    ]