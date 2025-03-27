from app.domain.interfaces import VectorStoreInterface
from app.domain.models import VectorDocument
from typing import List
import chromadb
from chromadb.config import Settings as ChromaSettings
from app.core.config import settings

class ChromaVectorStore(VectorStoreInterface):

    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("knowledge")

    def query(self, query_text: str, top_k: int = 3) -> List[VectorDocument]:
        results = self.collection.query(
            query_texts=[query_text], 
            n_results=top_k
        )
        return [
            VectorDocument(id=id_, content=doc)
            for id_, doc in zip(results["ids"][0], results["documents"][0])
        ]

    def upsert(self, documents: List[VectorDocument]):
        ids = [doc.id for doc in documents]
        contents = [doc.content for doc in documents]
        metadatas = [doc.metadata or {} for doc in documents]

        self.collection.add(
            ids=ids,
            documents=contents,
            metadatas=metadatas
        )
