# Generated by Django 3.2.21 on 2023-09-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0129_add_unique_constraint_viewfieldoptions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulafield",
            name="array_formula_type",
            field=models.TextField(
                choices=[
                    ("invalid", "invalid"),
                    ("text", "text"),
                    ("char", "char"),
                    ("link", "link"),
                    ("date_interval", "date_interval"),
                    ("date", "date"),
                    ("boolean", "boolean"),
                    ("number", "number"),
                    ("single_select", "single_select"),
                    ("single_file", "single_file"),
                ],
                default=None,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="formulafield",
            name="formula_type",
            field=models.TextField(
                choices=[
                    ("invalid", "invalid"),
                    ("text", "text"),
                    ("char", "char"),
                    ("link", "link"),
                    ("date_interval", "date_interval"),
                    ("date", "date"),
                    ("boolean", "boolean"),
                    ("number", "number"),
                    ("array", "array"),
                    ("single_select", "single_select"),
                    ("single_file", "single_file"),
                ],
                default="invalid",
            ),
        ),
    ]