# Generated by Django 2.2.11 on 2020-04-08 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickshare', '0002_card_fil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='fil',
        ),
    ]
