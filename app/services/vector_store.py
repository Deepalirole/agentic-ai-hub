from typing import List, Dict

import chromadb
from chromadb.config import Settings as ChromaSettings

from app.services.data_loader import load_sample_faqs


class FAQVectorStore:
    def __init__(self, collection_name: str = "faqs") -> None:
        self.client = chromadb.Client(
            ChromaSettings(
                persist_directory=".chroma",
            )
        )
        self.collection = self.client.get_or_create_collection(name=collection_name)
        self._ensure_seed_data()

    def _ensure_seed_data(self) -> None:
        if self.collection.count() > 0:
            return
        faqs = load_sample_faqs()
        self.collection.add(
            ids=[f["id"] for f in faqs],
            documents=[f["question"] + "\n" + f["answer"] for f in faqs],
            metadatas=[{"question": f["question"], "answer": f["answer"]} for f in faqs],
        )

    def search_faq(self, query: str, top_k: int = 3) -> List[Dict]:
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
        )
        docs = results.get("metadatas", [[]])[0]
        return docs
