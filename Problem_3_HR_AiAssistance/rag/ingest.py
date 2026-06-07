from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

PDF_PATH = "/Users/atharvabhalerao/Desktop/Eminent-AI-ML-Assessment/Problem_3_HR_AiAssistance/data/hr_policy.pdf"
CHROMA_PATH = "vectorstore/chroma_db"


def load_documents():
    """
    Load PDF document and clean text
    """

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    for doc in documents:

        text = doc.page_content

        # Remove line breaks
        text = text.replace("\n", " ")

        # Remove multiple spaces
        text = " ".join(text.split())

        doc.page_content = text

    print(f"Loaded {len(documents)} pages")

    print("\n" + "=" * 80)
    print("FIRST PAGE AFTER CLEANING")
    print("=" * 80)
    print(documents[0].page_content[:1000])
    print("=" * 80)

    return documents


def split_documents(documents):
    """
    Split documents into chunks
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks


def create_vector_store(chunks):
    """
    Generate embeddings and store in ChromaDB
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    print("Vector database created successfully!")

    return vectorstore


def main():

    print("Loading PDF...")

    documents = load_documents()

    print("Splitting documents...")

    chunks = split_documents(documents)

    print("Creating embeddings and vector database...")

    create_vector_store(chunks)

    print("Done!")


if __name__ == "__main__":
    main()