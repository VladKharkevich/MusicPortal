# Generated by Django 3.0.7 on 2020-07-10 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_portal', '0005_auto_20200710_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='date_of_breakup',
        ),
        migrations.RemoveField(
            model_name='band',
            name='date_of_creation',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='song',
            name='year_of_creation',
        ),
    ]
