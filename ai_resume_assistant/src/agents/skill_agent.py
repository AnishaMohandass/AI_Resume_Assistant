# This file find missing or weak skills in the resume

from utlis.prompts import SKILL_PROMPT

def skill_agent(query, retriever, llm):
    docs = retriever.invoke(query)
    context = " ".join([d.page_content for d in docs])

    prompt = SKILL_PROMPT.format(context=context)
    return llm.invoke(prompt)