# Generated by Django 3.0.1 on 2020-02-17 17:14

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200117_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='file_user_css',
            field=models.FileField(default='null', upload_to=accounts.models.user_dir_path),
        ),
    ]
