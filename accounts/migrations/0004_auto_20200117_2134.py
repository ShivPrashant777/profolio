# Generated by Django 3.0.2 on 2020-01-17 16:04

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200110_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='img',
            field=models.FileField(default='null', upload_to=accounts.models.user_dir_path),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(default='noname', max_length=50),
        ),
    ]
