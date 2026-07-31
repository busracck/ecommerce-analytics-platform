from sqlalchemy import inspect

from src.database import engine


def get_database_schema() -> str:
    inspector = inspect(engine)
    schema_lines = []

    for table_name in inspector.get_table_names():
        schema_lines.append(f"Tablo: {table_name}")

        columns = inspector.get_columns(table_name)

        for column in columns:
            column_name = column["name"]
            column_type = column["type"]

            schema_lines.append(
                f"  - {column_name}: {column_type}"
            )

        foreign_keys = inspector.get_foreign_keys(table_name)

        for foreign_key in foreign_keys:
            source_columns = ", ".join(
                foreign_key["constrained_columns"]
            )

            target_table = foreign_key["referred_table"]

            target_columns = ", ".join(
                foreign_key["referred_columns"]
            )

            schema_lines.append(
                f"  İlişki: {source_columns} -> "
                f"{target_table}.{target_columns}"
            )

        schema_lines.append("")

    return "\n".join(schema_lines)


