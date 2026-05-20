import faiss
import numpy as np

# ⚠️ DO NOT LOAD MODEL AT IMPORT TIME
_model = None
_index = None
_memory_store = []


def _get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def _get_index():
    global _index
    if _index is None:
        _index = faiss.IndexFlatL2(384)
    return _index


def add_memory(text):
    model = _get_model()
    index = _get_index()

    vec = model.encode([text])
    index.add(np.array(vec).astype("float32"))
    _memory_store.append(text)


def search_memory(query, k=5):
    model = _get_model()
    index = _get_index()

    if len(_memory_store) == 0:
        return []

    vec = model.encode([query])
    D, I = index.search(np.array(vec).astype("float32"), k)

    return [ _memory_store[i] for i in I[0] if i < len(_memory_store) ]