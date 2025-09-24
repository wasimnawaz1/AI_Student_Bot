from fastapi import FastAPI, Request
from tasks import process_text, process_video
import uvicorn

app = FastAPI()

@app.post("/enqueue")
async def enqueue(req: Request):
    data = await req.json()
    typ = data.get("type")
    if typ == "text":
        title = data.get("title")
        text = data.get("text")
        process_text(title, text)
    elif typ == "video":
        url = data.get("url")
        process_video(url)
    return {"status":"accepted"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
