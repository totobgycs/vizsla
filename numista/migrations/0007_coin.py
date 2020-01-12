# Generated by Django 3.0 on 2020-01-11 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('numista', '0006_auto_20200105_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numistaId', models.IntegerField(unique=True)),
                ('url', models.TextField()),
                ('title', models.TextField()),
                ('minYear', models.IntegerField(null=True)),
                ('maxYear', models.IntegerField(null=True)),
                ('coinType', models.CharField(max_length=200)),
                ('valueText', models.CharField(max_length=200)),
                ('shape', models.CharField(max_length=200)),
                ('composition', models.CharField(max_length=200)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=7)),
                ('size', models.DecimalField(decimal_places=3, max_digits=7)),
                ('thickness', models.DecimalField(decimal_places=3, max_digits=7)),
                ('obverse_picture', models.TextField()),
                ('obverse_thumbnail', models.TextField()),
                ('reverse_picture', models.TextField()),
                ('reverse_thumbnail', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='numista.Country')),
                ('valueCurrency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='numista.Currency')),
            ],
            options={
                'db_table': 'numista"."coin',
            },
        ),
    ]