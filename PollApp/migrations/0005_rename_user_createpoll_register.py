# Generated by Django 3.2 on 2021-07-14 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PollApp', '0004_createpoll_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createpoll',
            old_name='user',
            new_name='register',
        ),
    ]