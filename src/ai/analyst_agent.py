import os
import pandas as pd

from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def create_analysis_prompt(
    user_question: str,
    df: pd.DataFrame
) -> str:

    data_text = df.to_string(index=False)

    prompt = f"""
Sen deneyimli bir e-ticaret veri analistisin.

Kullanıcının sorusu:
{user_question}

SQL sorgusundan gelen veriler:
{data_text}

Kurallar:
- Cevabı Türkçe ver.
- Yalnızca verilen verilere dayan.
- Veride olmayan bilgiler hakkında tahmin yapma.
- En önemli bulguları açıkça belirt.
- Sayısal değerleri kullan.
- Cevabı kısa ve anlaşılır yaz.
"""

    return prompt



def analyze_data(
    user_question: str,
    df: pd.DataFrame
) -> str:

    prompt = create_analysis_prompt(
        user_question,
        df
    )

    response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt,
)

    return response.text.strip()

   