# This file rewrite resume content professionally

from utlis.prompts import IMPROVE_PROMPT

def improve_agent(query, retriever, llm):
    docs = retriever.invoke(query)
    context = " ".join([d.page_content for d in docs])

    prompt = IMPROVE_PROMPT.format(context=context)
    return llm.invoke(prompt)