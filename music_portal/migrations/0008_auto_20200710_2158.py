# Generated by Django 3.0.7 on 2020-07-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_portal', '0007_auto_20200710_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='date_of_breakup',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='date_of_creation',
            field=models.PositiveSmallIntegerField(default=2020),
        ),
        migrations.AddField(
            model_name='song',
            name='year_of_creation',
            field=models.PositiveSmallIntegerField(default=2020),
        ),
    ]
