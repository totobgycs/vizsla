# Generated by Django 3.0.3 on 2020-05-09 20:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('numista', '0011_coininfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coininfo',
            name='numistaIssuers',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
