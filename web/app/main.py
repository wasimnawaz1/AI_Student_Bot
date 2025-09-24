from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from api import search_query, health

app = FastAPI(title="AI Student Bot")

@app.get("/health")
def _health():
    return health()

@app.post("/query")
async def query(q: str = Form(...)):
    resp = search_query(q)
    return JSONResponse(resp)

@app.post("/ingest/text")
async def ingest_text(title: str = Form(...), text: str = Form(...)):
    from ingest import enqueue_text
    job = enqueue_text(title, text)
    return {"status":"enqueued", "job": job}
