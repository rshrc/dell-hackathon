# Generated by Django 2.2.6 on 2019-10-13 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
    ]
