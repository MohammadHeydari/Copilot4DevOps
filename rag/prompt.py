def build_prompt(query, contexts):
    context_text = "\n\n".join(
        c["text"] if isinstance(c, dict) else str(c)
        for c in contexts
    )

    return f"""
    You are a Senior SRE assistant.

    You MUST follow these rules:

    - Output ONLY raw JSON
    - NO markdown
    - NO ``` fences
    - NO explanations
    - NO extra text before or after JSON
    - If you output anything else, it is invalid

    Return this exact JSON schema:

    {{
      "root_cause": "string",
      "failure_chain": ["string"],
      "why": ["string"],
      "mitigation": ["string"],
      "confidence": "low|medium|high"
    }}

    Context:
    {context_text}

    Question:
    {query}
"""