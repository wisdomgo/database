# Generated by Django 4.2 on 2024-05-25 18:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_alter_userinfo_creat_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.userinfo', verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='creat_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 26, 2, 46, 33, 949767), null=True, verbose_name='入职时间'),
        ),
    ]