# Generated by Django 3.2.7 on 2021-09-13 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_work_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='work_files',
        ),
    ]
