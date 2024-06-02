# Generated by Django 3.0.6 on 2024-05-27 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_alter_task_user_alter_userinfo_creat_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumbers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='creat_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 27, 16, 23, 53, 427164), null=True, verbose_name='入职时间'),
        ),
    ]
