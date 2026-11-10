from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    collection_name="ai_documents",
    embedding_function=embedding_model,
    persist_directory=CHROMA_PATH
)

print("Semantic Document Search System")

query = input("Enter your search query: ")

results = vector_store.similarity_search_with_score(query, k=5)

print("\nTop 5 Relevant Documents:")

for rank, (doc, score) in enumerate(results, 1):
    print(f"\nRank: {rank}")
    print("Document:", doc.page_content)
    print("Distance Score:", round(float(score), 4))