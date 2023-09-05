# Generated by Django 3.2.5 on 2022-01-15 06:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
