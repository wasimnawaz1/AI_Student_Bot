import requests
import os

WORKER_URL = os.environ.get("WORKER_URL", "http://worker:9000/enqueue")

def enqueue_text(title, text):
    try:
        r = requests.post(WORKER_URL, json={"type":"text","title":title,"text":text}, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}
