# Generated by Django 4.2.5 on 2024-04-15 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_house_bathroom_house_bedroom_house_rooms_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='Bathroom',
            new_name='bathroom',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='Bedroom',
            new_name='bedroom',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='Rooms',
            new_name='rooms',
        ),
    ]
