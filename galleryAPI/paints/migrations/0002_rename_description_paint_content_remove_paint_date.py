# Generated by Django 4.1.1 on 2022-10-01 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("paints", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="paint",
            old_name="description",
            new_name="content",
        ),
        migrations.RemoveField(
            model_name="paint",
            name="date",
        ),
    ]
