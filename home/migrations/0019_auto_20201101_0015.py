# Generated by Django 3.0.8 on 2020-10-31 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20201031_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticeboard',
            name='icons',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='reports',
            name='against_id',
            field=models.CharField(max_length=50),
        ),
    ]
