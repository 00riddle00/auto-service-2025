# Generated by Django 5.1.4 on 2024-12-23 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="service",
            old_name="code",
            new_name="name",
        ),
    ]
