# Generated by Django 2.0.3 on 2018-03-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180310_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AlterModelManagers(
            name='profile',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='building_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='room_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]