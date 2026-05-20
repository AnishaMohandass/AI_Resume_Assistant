# This file initializes and configures the language model that generates the final answer

from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

def get_llm():

    pipe = pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-0.5B-Instruct",
        max_new_tokens=300,
        temperature=0.1,
        do_sample=True,
        return_full_text=False,
        clean_up_tokenization_spaces=False
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    return llm
