# Generated by Django 5.1.4 on 2024-12-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0002_rename_code_service_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("N", "New"),
                    ("D", "Declined"),
                    ("A", "Accepted"),
                    ("P", "In Progress"),
                    ("C", "Completed"),
                ],
                default="N",
                max_length=1,
            ),
        ),
    ]
