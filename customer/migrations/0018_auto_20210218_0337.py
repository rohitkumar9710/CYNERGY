# Generated by Django 3.1.6 on 2021-02-17 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_auto_20210217_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_order',
            name='work_description',
            field=models.CharField(default='None', max_length=1000),
        ),
    ]
