# This file is the main entry point that executes the full GenAI workflow from resume loading to final AI response

# To suppress warnings
import warnings
warnings.filterwarnings("ignore")

from src.loader import load_resume
from src.splitter import split_docs
from src.embeddings import create_vector_db
from src.retriever import get_retriever
from src.llm import get_llm
from src.graph.workflow import build_graph

def main():
    # 1. Load resume
    docs = load_resume("data/resume.pdf")

    # 2. Split text
    chunks = split_docs(docs)

    # 3. Create vector DB
    vector_db = create_vector_db(chunks)

    # 4. Create retriever
    retriever = get_retriever(vector_db)

    # 5. Initialize LLM
    llm = get_llm()

    # 6. Build workflow graph
    app = build_graph(retriever, llm)

    # 7. Run
    while True: # User Interaction Loop - Keeps chatbot running continuously
        query = input("\nAsk something about your resume: ") # Get User Query
        response = app.invoke({"query": query}) # Execute Graph
        print("\nAnswer:\n", response["output"]) # Print Output


if __name__ == "__main__":
    main()