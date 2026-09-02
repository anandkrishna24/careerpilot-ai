def get_research_prompt(question, context):

    return f"""
You are an AI Research Assistant.

Use ONLY the following context.

Context:

{context}

Question:

{question}

Return a detailed answer.
"""