# This file converts text chunks into numerical vectors and stores them in a vector database for semantic search

# Embeddings convert text into dense vector representations that capture semantic meaning, 
# enabling similarity-based retrieval in vector databases like FAISS.

from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS

def create_vector_db(chunks):
    embedding = HuggingFaceEmbeddings()
    vector_db = FAISS.from_documents(chunks, embedding)
    return vector_db