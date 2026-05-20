# This file stores all instructions (prompts) that needed to give the LLM
# {context} - This is where retrieved resume chunks are inserted

SKILL_PROMPT = """
You are an AI Skill Analysis Assistant.

Analyze the resume and identify:

1. Missing technical skills
2. Missing AI/ML skills
3. Industry-relevant skills to learn
4. Important tools missing

Resume:
{context}

Give concise bullet-point answers.
"""


ATS_PROMPT = """
You are an expert ATS Resume Evaluator.

Analyze the following resume and provide:

1. ATS Score out of 100
2. Strengths
3. Areas of Improvement
4. Final Recommendation

Resume:
{context}

Answer in professional bullet points.
"""


IMPROVE_PROMPT = """
You are an expert resume writer.

Improve the resume professionally by:
1. Rewriting weak points
2. Improving project descriptions
3. Adding strong ATS keywords
4. Making the resume more impactful

Resume:
{context}

Provide improved professional content.
"""