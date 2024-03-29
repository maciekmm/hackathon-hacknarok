# Generated by Django 2.0.3 on 2018-03-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180310_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room',
            new_name='room_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='building_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='profile',
            name='room_number',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
