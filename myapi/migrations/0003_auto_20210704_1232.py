# Generated by Django 3.2.5 on 2021-07-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20210704_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='name',
        ),
        migrations.AddField(
            model_name='hero',
            name='Bed_Count',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='hero',
            name='City',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='hero',
            name='County',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='hero',
            name='Founded',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='hero',
            name='Hospital',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='hero',
            name='Trauma_Center',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
