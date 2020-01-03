# Generated by Django 3.0 on 2019-12-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('numista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numista_country_id', models.CharField(max_length=30, unique=True)),
                ('numista_country_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'numista"."country',
            },
        ),
    ]
