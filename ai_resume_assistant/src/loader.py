# This file reads the resume file (PDF) and loads it for further process

from langchain_community.document_loaders import PyPDFLoader

def load_resume(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()