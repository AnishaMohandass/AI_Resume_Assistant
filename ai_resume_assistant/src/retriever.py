# This file searches the vector database and retrieves the most relevant chunks based on the user’s query

# It calculates similarity between: 1)Query vector and 2)All stored chunk vectors

def get_retriever(vector_db):
    return vector_db.as_retriever(search_kwargs={"k": 3}) #search_kwargs={"k": 3} - Return top 3 most relevant chunks