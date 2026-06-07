from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

CHROMA_PATH = "vectorstore/chroma_db"


class HRRetriever:

    def __init__(self):

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embeddings
        )

    def retrieve(self, question: str, k: int = 5):

        results = self.db.similarity_search_with_score(
        question,
        k=k
    )
        return results