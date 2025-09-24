from typing import List
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection("student_qna")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def search_query(q:str, k=5):
    q_emb = embedder.encode(q).tolist()
    results = collection.query(query_embeddings=[q_emb], n_results=k)
    hits = []
    for i, ids in enumerate(results.get("ids", [])):
        for j, _id in enumerate(ids):
            hits.append({
                "id": _id,
                "document": results.get("documents", [])[i][j] if results.get("documents") else None,
                "distance": results.get("distances", [])[i][j] if results.get("distances") else None
            })
    return {"query": q, "results": hits}

def health():
    return {"status":"ok"}
