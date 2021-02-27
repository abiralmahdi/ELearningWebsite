# Generated by Django 3.0.8 on 2020-10-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201022_1833'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HSCChem1st',
        ),
        migrations.DeleteModel(
            name='HSCChem2nd',
        ),
        migrations.DeleteModel(
            name='HSCMath1st',
        ),
        migrations.DeleteModel(
            name='HSCMath2nd',
        ),
        migrations.DeleteModel(
            name='HSCPhysics1st',
        ),
        migrations.DeleteModel(
            name='HSCPhysics2nd',
        ),
        migrations.DeleteModel(
            name='JSCMath',
        ),
        migrations.DeleteModel(
            name='JSCScience',
        ),
        migrations.DeleteModel(
            name='SSCBiology',
        ),
        migrations.DeleteModel(
            name='SSCChemistry',
        ),
        migrations.DeleteModel(
            name='SSCHMath',
        ),
        migrations.DeleteModel(
            name='SSCMath',
        ),
        migrations.DeleteModel(
            name='SSCPhysics',
        ),
        migrations.AlterField(
            model_name='allcontent',
            name='subjSlug',
            field=models.CharField(max_length=50),
        ),
    ]
