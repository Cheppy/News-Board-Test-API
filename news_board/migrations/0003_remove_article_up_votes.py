# Generated by Django 3.2.2 on 2021-05-08 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news_board", "0002_auto_20210508_1754"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="up_votes",
        ),
    ]
