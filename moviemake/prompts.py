def script_prompt(idea: str, genre: str, tone: str):
    return f"""You are a creative screenwriter. Based on the brief idea below, write a very short script outline with 3 scenes.
- Keep it concise (3-5 sentences per scene).
- Include scene titles as: SCENE 1, SCENE 2, SCENE 3.
- Genre: {genre}. Tone: {tone}.
- Make it cinematic and end with a small cliffhanger.

Idea: "{idea}"
"""

def poster_prompt(idea: str, title: str, style: str):
    return f"""Create a cinematic movie poster concept for the film titled '{title}'.
The style should be {style}. The core idea is: {idea}.
Focus on strong composition, clear focal subject, and mood matching the genre.
"""
