# Generated by Django 3.0.8 on 2020-10-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20201027_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='topic',
        ),
        migrations.AddField(
            model_name='reports',
            name='against_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
