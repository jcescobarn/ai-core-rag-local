
import pytest
from app.infrastructure.vector_store import ChromaVectorStore
from app.domain.models import VectorDocument

def test_vector_store_upsert_and_query():
    store = ChromaVectorStore()
    doc = VectorDocument(id="doc1", content="Este es un documento de prueba")
    store.upsert([doc])
    results = store.query("prueba", top_k=1)
    assert isinstance(results, list)
