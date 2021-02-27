# Generated by Django 3.0.8 on 2020-10-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201023_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredteachers',
            name='account_type',
            field=models.CharField(default='Teacher', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='accounts_type',
            field=models.CharField(default='Student', max_length=50),
        ),
    ]
