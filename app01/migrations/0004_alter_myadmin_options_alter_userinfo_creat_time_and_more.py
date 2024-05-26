# Generated by Django 4.2 on 2023-05-03 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0003_alter_userinfo_creat_time"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="myadmin",
            options={"verbose_name": "管理员"},
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="creat_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 5, 3, 9, 3, 59, 204882),
                null=True,
                verbose_name="入职时间",
            ),
        ),
        migrations.AlterModelTable(
            name="myadmin",
            table="管理员表",
        ),
    ]
