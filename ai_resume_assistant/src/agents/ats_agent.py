#This file evaluate resume like an Applicant Tracking System

from utlis.prompts import ATS_PROMPT

def ats_agent(query, retriever, llm):
    docs = retriever.invoke(query)
    context = " ".join([d.page_content for d in docs])

    prompt = ATS_PROMPT.format(context=context)
    return llm.invoke(prompt)