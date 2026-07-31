import os
import re
from dotenv import load_dotenv
import pandas as pd

from src.ai.schema import get_database_schema
from src.database import engine
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def create_sql_prompt(user_question: str) -> str:
    database_schema = get_database_schema()

    prompt = f"""
Sen PostgreSQL konusunda uzman bir veri analistisin.

Aşağıda veritabanının şeması bulunmaktadır:

{database_schema}

Kullanıcının sorusu:
{user_question}

Bu soruyu cevaplayacak bir PostgreSQL SELECT sorgusu oluştur.

Kurallar:
- Yalnızca SELECT sorgusu üret.
- INSERT, UPDATE, DELETE, DROP, ALTER veya TRUNCATE kullanma.
- Sadece verilen tablo ve sütunları kullan.
- Gerekli olduğunda tabloları doğru ilişkilerle JOIN et.
- Açıklama yazma.
- Markdown kod bloğu kullanma.
- Yalnızca SQL sorgusunu döndür.
"""

    return prompt






def generate_sql(user_question: str) -> str:
    prompt = create_sql_prompt(user_question)

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text.strip()



def validate_sql(sql: str) -> bool:
    cleaned_sql = sql.strip()

    # Gemini bazen yanlışlıkla kod bloğu döndürürse temizler.
    cleaned_sql = cleaned_sql.replace("```sql", "")
    cleaned_sql = cleaned_sql.replace("```", "")
    cleaned_sql = cleaned_sql.strip()

    normalized_sql = cleaned_sql.lower()

    # Yalnızca SELECT veya WITH ile başlayan sorgulara izin ver.
    if not normalized_sql.startswith(("select", "with")):
        return False

    forbidden_keywords = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "truncate",
        "create",
        "replace",
        "grant",
        "revoke"
    ]

    # Kelimeleri bağımsız SQL komutu olarak kontrol eder.
    for keyword in forbidden_keywords:
        pattern = rf"\b{keyword}\b"

        if re.search(pattern, normalized_sql):
            return False

    # Birden fazla SQL sorgusunu engeller.
    sql_without_last_semicolon = normalized_sql.rstrip(";")

    if ";" in sql_without_last_semicolon:
        return False

    return True


def execute_sql(sql: str):
    if not validate_sql(sql):
        raise ValueError(
            "Güvenlik nedeniyle yalnızca SELECT sorgularına izin veriliyor."
        )

    df = pd.read_sql_query(
        sql,
        con=engine
    )

    return df

