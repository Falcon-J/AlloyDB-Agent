import psycopg2
import os

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port="5432"
    )

def run_sql(sql: str):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(sql)
    rows = cur.fetchall()

    colnames = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    return [dict(zip(colnames, row)) for row in rows]