# Generated by Django 3.2.5 on 2021-07-04 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_rename_hero_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='Bed_Count',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Founded',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Trauma_Center',
        ),
    ]
