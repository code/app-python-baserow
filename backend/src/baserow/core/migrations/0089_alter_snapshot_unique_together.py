# Generated by Django 4.2.13 on 2024-09-05 06:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0088_remove_blacklistedtoken_user"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="snapshot",
            unique_together=set(),
        ),
    ]
