# Generated by Django 3.2.7 on 2021-09-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_work_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='work_files',
            field=models.FileField(blank=True, upload_to='works_folder'),
        ),
    ]
