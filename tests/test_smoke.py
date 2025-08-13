from moviemake.utils import load_env
from moviemake.llm import generate_script
from moviemake.poster import generate_poster
from moviemake.cast import suggest_cast
import os

def test_offline_pipeline(tmp_path):
    env = {"USE_OPENAI": False, "OPENAI_API_KEY": ""}
    idea = "A courier in a neon city finds a mysterious package that everyone wants."
    script_text = generate_script(idea, genre="Sci-Fi", tone="Cinematic", env=env)
    assert "SCENE" in script_text or "SCENE 1" in script_text or "TITLE:" in script_text

    poster = generate_poster(idea, title="Neon Courier", style="Neon", env=env, out_dir=str(tmp_path))
    assert os.path.exists(poster)

    cast = suggest_cast(idea, genre="Sci-Fi", top_k=3)
    assert len(cast) == 3
