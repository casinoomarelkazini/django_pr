# Generated by Django 4.0.2 on 2022-02-25 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_film_film_pic_alter_seen_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='user',
        ),
    ]
