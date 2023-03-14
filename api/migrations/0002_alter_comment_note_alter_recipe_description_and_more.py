# Generated by Django 4.1 on 2023-03-14 23:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='note',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), size=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2000), size=None),
        ),
    ]