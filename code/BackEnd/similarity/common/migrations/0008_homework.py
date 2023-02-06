# Generated by Django 4.0.4 on 2023-01-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='homework',
            fields=[
                ('homeworkid', models.AutoField(primary_key=True, serialize=False)),
                ('homeworkname', models.CharField(max_length=255)),
                ('courseid', models.CharField(max_length=255)),
                ('ctime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'homework',
                'managed': True,
            },
        ),
    ]