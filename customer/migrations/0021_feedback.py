# Generated by Django 3.1.6 on 2021-02-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.CharField(max_length=150)),
                ('serviceman_email', models.CharField(default='none', max_length=150)),
                ('feedback', models.CharField(default='None', max_length=1000)),
                ('work', models.CharField(default='', max_length=50)),
                ('request_date', models.DateField()),
                ('feedback_date', models.DateField()),
                ('w_done_date', models.DateField()),
                ('rating', models.IntegerField(default=3)),
            ],
        ),
    ]
