# Generated by Django 4.1.4 on 2022-12-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="DateTime",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
