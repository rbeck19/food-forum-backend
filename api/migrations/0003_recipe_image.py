# Generated by Django 4.1 on 2023-03-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_comment_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]