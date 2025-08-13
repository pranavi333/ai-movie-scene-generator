import os
from .prompts import script_prompt
from .utils import extract_keywords

# Offline fallback generator (simple template-based outline)
def _offline_script(idea: str, genre: str, tone: str):
    kws = extract_keywords(idea, top_k=8)
    kstr = ", ".join(kws[:5]) if kws else "mystery"
    return f"""TITLE: {genre} concept

SCENE 1 — Setup
We meet the protagonist and the world. The idea revolves around {kstr}. A small but curious event hints at a bigger story. The tone is {tone}.

SCENE 2 — Rising Tension
Complications escalate. Allies and obstacles appear, shaped by the idea: {', '.join(kws)}. The stakes grow as a secret is revealed.

SCENE 3 — Cliffhanger
A tough choice sets up the next act. The genre beats of {genre} intensify. End on a visual cliffhanger that leaves the audience wanting more.
"""

def generate_script(idea: str, genre: str, tone: str, env: dict) -> str:
    if env.get("USE_OPENAI") and env.get("OPENAI_API_KEY"):
        try:
            from openai import OpenAI
            client = OpenAI(api_key=env["OPENAI_API_KEY"])
            prompt = script_prompt(idea, genre, tone)
            # Use Chat Completions-like API (new SDK uses client.chat.completions)
            resp = client.chat.completions.create(
                model=env.get("OPENAI_TEXT_MODEL", "gpt-4o-mini"),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.9,
                max_tokens=700,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return _offline_script(idea, genre, tone) + f"\n\n[Note: OpenAI fallback due to error: {e}]"
    else:
        return _offline_script(idea, genre, tone)
