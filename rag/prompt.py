def build_prompt(query, contexts):
    context_text = "\n\n".join(
        c["text"] if isinstance(c, dict) else str(c)
        for c in contexts
    )

    return f"""
You are a Senior SRE.

Analyze the incident step by step:
1. Identify possible failure chain
2. Explain why it happened
3. Suggest mitigation
4. If context is limited, infer cautiously

Context:
{context_text}

Question:
{query}

Answer:
"""