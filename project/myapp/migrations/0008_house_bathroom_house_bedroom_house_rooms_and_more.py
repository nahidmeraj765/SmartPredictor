# Generated by Django 4.2.5 on 2024-04-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='Bathroom',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='Bedroom',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='Rooms',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='carPark',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]