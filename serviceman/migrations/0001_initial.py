# Generated by Django 3.1.6 on 2021-02-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serviceinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('phone_no', models.IntegerField()),
                ('password', models.CharField(max_length=150)),
                ('sign_up_date', models.DateField()),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=50)),
                ('addres', models.CharField(default='', max_length=200)),
                ('activestate', models.CharField(default='active', max_length=20)),
                ('primary_work', models.CharField(max_length=50)),
                ('secondary_word', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
