from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

CHROMA_PATH = "vectorstore/chroma_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)

questions = [
    "What is maternity leave?",
    "How many sick leave days do employees get?",
    "What is bereavement leave?",
    "Can I work remotely during probation?"
]

for question in questions:

    print("\n" + "=" * 120)
    print(f"QUESTION: {question}")
    print("=" * 120)

    results = db.similarity_search_with_score(question, k=3)

    for idx, (doc, score) in enumerate(results, start=1):

        content = " ".join(doc.page_content.split())

        print(
            f"{idx:<3} | Score: {score:<10.4f} | "
            f"{content[:300]}"
        )