from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import nl_to_sql
from app.db import run_sql

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask(q: Query):
    if not q.query:
        raise HTTPException(status_code=400, detail="query required")

    try:
        sql = nl_to_sql(q.query)
        data = run_sql(sql)

        return {
            "query": q.query,
            "sql": sql,
            "results": data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))