# Generated by Django 3.0.7 on 2020-07-09 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_portal', '0003_auto_20200709_2204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mucisian',
            new_name='Musician',
        ),
    ]