# Generated by Django 4.2 on 2023-05-03 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0004_alter_myadmin_options_alter_userinfo_creat_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, verbose_name="标题")),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(1, "紧急"), (2, "一般"), (3, "不紧急")],
                        default=2,
                        verbose_name="级别",
                    ),
                ),
                (
                    "detail",
                    models.TextField(blank=True, null=True, verbose_name="详细信息"),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="creat_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 5, 3, 20, 57, 43, 494242),
                null=True,
                verbose_name="入职时间",
            ),
        ),
    ]
