# Generated by Django 3.0.8 on 2020-11-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20201108_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionbank',
            old_name='quesID',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='questionbank',
            old_name='subName',
            new_name='chapter',
        ),
        migrations.RenameField(
            model_name='questionbank',
            old_name='subSlug',
            new_name='options',
        ),
        migrations.AddField(
            model_name='questionbank',
            name='ques',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='questionbank',
            name='subject',
            field=models.CharField(default='', max_length=30),
        ),
    ]
