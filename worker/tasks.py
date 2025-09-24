from sentence_transformers import SentenceTransformer
import chromadb
import requests
import tempfile
import os

client = chromadb.Client()
col = client.get_or_create_collection("student_qna")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def process_text(title, text):
    emb = embedder.encode(text).tolist()
    # use title as id but in production ensure unique ids
    col.add(documents=[text], metadatas=[{"title":title}], ids=[title], embeddings=[emb])

def process_video(url):
    r = requests.get(url, stream=True, timeout=60)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    with open(tmp.name, "wb") as f:
        for chunk in r.iter_content(1024*1024):
            if chunk:
                f.write(chunk)
    import whisper
    model = whisper.load_model("small")
    res = model.transcribe(tmp.name)
    text = res.get("text","")
    process_text(os.path.basename(tmp.name), text)
    os.unlink(tmp.name)
