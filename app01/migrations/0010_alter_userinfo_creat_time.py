# Generated by Django 4.2 on 2024-05-25 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_alter_userinfo_creat_time_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='creat_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 25, 16, 31, 27, 309424), null=True, verbose_name='入职时间'),
        ),
    ]