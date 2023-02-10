# Generated by Django 4.1.4 on 2023-02-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_entry_datetime_entry_date_entry_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="Status",
            field=models.CharField(
                choices=[("Late", " Late"), ("On Time", " Ontime")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="entry",
            name="Date",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="entry",
            name="Time",
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
