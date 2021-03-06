# Generated by Django 3.0.3 on 2020-05-09 18:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numista', '0010_auto_20200213_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numistaId', models.IntegerField(unique=True)),
                ('lastDownload', models.DateTimeField(auto_now=True)),
                ('numistaCoin', django.contrib.postgres.fields.jsonb.JSONField()),
                ('numistaIssuers', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'db_table': 'numista"."coin_info',
            },
        ),
    ]
