# Generated by Django 4.2.13 on 2024-07-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0032_tablethemeconfigblock"),
    ]

    operations = [
        migrations.AddField(
            model_name="collectionfield",
            name="styles",
            field=models.JSONField(
                default=dict, help_text="The theme overrides for this field", null=True
            ),
        ),
    ]