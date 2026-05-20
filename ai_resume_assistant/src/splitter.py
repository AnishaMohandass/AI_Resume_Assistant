# This file breaks large resume text into smaller chunks so the AI can process and search it efficiently

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )
    return splitter.split_documents(docs)