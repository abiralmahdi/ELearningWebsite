# Generated by Django 3.0.8 on 2020-10-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_allcontent_chapslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcontent',
            name='topic',
            field=models.CharField(default='', max_length=100),
        ),
    ]
