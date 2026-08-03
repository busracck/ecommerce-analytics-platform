import json

from sqlalchemy import text

from src.database import engine


def save_query_history(
    question: str,
    generated_sql: str | None,
    result_data: list | None,
    analysis: str | None,
    status: str,
    error_message: str | None = None,
):
    query = text("""
        INSERT INTO ai_query_history (
            question,
            generated_sql,
            result_json,
            analysis,
            status,
            error_message
        )
        VALUES (
            :question,
            :generated_sql,
            CAST(:result_json AS JSONB),
            :analysis,
            :status,
            :error_message
        )
    """)

    result_json = (
        json.dumps(result_data, ensure_ascii=False, default=str)
        if result_data is not None
        else None
    )

    with engine.begin() as connection:
        connection.execute(
            query,
            {
                "question": question,
                "generated_sql": generated_sql,
                "result_json": result_json,
                "analysis": analysis,
                "status": status,
                "error_message": error_message,
            }
        )