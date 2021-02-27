# Generated by Django 3.0.8 on 2020-11-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subName', models.CharField(default='', max_length=30)),
                ('subSlug', models.CharField(default='', max_length=30)),
                ('quesID', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='cv',
            name='img',
            field=models.FileField(upload_to='static/images'),
        ),
    ]
