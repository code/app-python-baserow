# Generated by Django 3.2.21 on 2023-09-19 08:11

from django.db import connection, migrations

from baserow.core.psycopg import sql


def remove_duplicates(model, view):
    with connection.cursor() as cursor:
        cursor.execute(
            sql.SQL(
                """
DELETE FROM {table_name}
    WHERE id IN (
        SELECT
            UNNEST(ARRAY_REMOVE(dupe_ids, min_id))
        FROM (
            SELECT
                field_id, {view},
                MIN(t.id) AS min_id,
                ARRAY_AGG(t.id) AS dupe_ids
            FROM
                {table_name} t
            GROUP BY
                field_id, {view}
            HAVING
                COUNT(t.id) > 1
        ) a
    )
    """
            ).format(
                table_name=sql.Identifier(model._meta.db_table),
                view=sql.Identifier(view),
            )
        )


def forward(apps, schema_editor):
    CalendarViewFieldOptions = apps.get_model(
        "baserow_premium", "CalendarViewFieldOptions"
    )
    KanbanViewFieldOptions = apps.get_model("baserow_premium", "KanbanViewFieldOptions")

    for ViewFieldOptions, view_fk_field_name in (
        (KanbanViewFieldOptions, "kanban_view_id"),
        (CalendarViewFieldOptions, "calendar_view_id"),
    ):
        remove_duplicates(ViewFieldOptions, view_fk_field_name)


class Migration(migrations.Migration):
    dependencies = [
        ("baserow_premium", "0012_migrate_old_comment_to_tiptap_message"),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop),
    ]
