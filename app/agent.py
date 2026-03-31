from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SCHEMA = """
Table: movies
Columns:
- title (text)
- genre (text)
- rating (float)
- year (int)
"""

def nl_to_sql(query: str):
    if not query:
        raise ValueError("query required")

    prompt = f"""
Convert the following natural language query into a PostgreSQL SQL query.
Return ONLY SQL.

Schema:
{SCHEMA}

Query:
{query}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    text = response.text

    if not text:
        raise Exception("empty response")

    return text.replace("```sql", "").replace("```", "").strip()