# Generated by Django 4.0.5 on 2022-07-02 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0009_alter_bounty_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bounty',
            name='image',
        ),
    ]