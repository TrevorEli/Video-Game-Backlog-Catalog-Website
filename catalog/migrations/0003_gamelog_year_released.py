# Generated by Django 5.1.4 on 2024-12-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_gamelog_delete_logmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamelog',
            name='year_released',
            field=models.IntegerField(default=0),
        ),
    ]
