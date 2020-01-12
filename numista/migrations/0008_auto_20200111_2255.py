# Generated by Django 3.0 on 2020-01-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numista', '0007_coin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='size',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='thickness',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True),
        ),
    ]
