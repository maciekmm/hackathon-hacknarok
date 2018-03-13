# Generated by Django 2.0.3 on 2018-03-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180310_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='buildingName',
            new_name='building_name',
        ),
        migrations.AddField(
            model_name='room',
            name='room',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lon',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='duration',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='room',
            name='limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='lon',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='room',
            name='storey',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
