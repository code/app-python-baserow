# Generated by Django 5.0.13 on 2025-03-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0185_alter_ratingfield_style"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formviewfieldoptionscondition",
            name="value",
            field=models.TextField(
                blank=True,
                help_text="The filter value that must be compared to the field's value.",
            ),
        ),
        migrations.AlterField(
            model_name="viewfilter",
            name="value",
            field=models.TextField(
                blank=True,
                help_text="The filter value that must be compared to the field's value.",
            ),
        ),
    ]
