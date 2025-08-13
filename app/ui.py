import streamlit as st
from moviemake.utils import ensure_dirs, slugify, random_id, load_env, save_text
from moviemake.llm import generate_script
from moviemake.poster import generate_poster
from moviemake.cast import suggest_cast

ensure_dirs()
st.set_page_config(page_title="AI Movie Scene Generator", layout="centered")
st.title("🎬 AI-Powered Movie Scene Generator")

with st.expander("What is this?"):
    st.write("""Type a short idea. You'll get:
- A 3-scene script outline
- A simple movie poster image (offline)
- A suggested cast list (keyword-based)
Optionally enable OpenAI in `.env` for higher quality.""")

col1, col2 = st.columns(2)
with col1:
    genre = st.selectbox("Genre", ["Action","Romance","Sci-Fi","Thriller","Horror","Drama","Comedy","Fantasy"], index=2)
    tone = st.selectbox("Tone", ["Cinematic","Dark","Whimsical","Gritty","Uplifting","Melancholic","Epic"], index=0)
with col2:
    poster_style = st.selectbox("Poster Style", ["Neon", "Vintage", "Minimalist", "Watercolor", "Noir", "Cyberpunk", "Pastel"], index=0)
    cast_n = st.slider("Cast suggestions", 3, 8, 5)

idea = st.text_area("Your movie idea (1–3 sentences)", height=120, placeholder="e.g., A shy student finds a portal in the library leading to alternate realities...")

if st.button("Generate") or (idea and st.session_state.get("auto_run")):
    st.session_state["auto_run"] = True
    if not idea.strip():
        st.error("Please enter an idea.")
        st.stop()

    env = load_env()
    title = idea.strip().split(".")[0]
    if len(title) > 60:
        title = title[:57] + "..."

    with st.spinner("Writing script..."):
        script_text = generate_script(idea=idea, genre=genre, tone=tone, env=env)

    with st.spinner("Designing poster..."):
        poster_path = generate_poster(idea=idea, title=title, style=poster_style, env=env, out_dir="outputs")

    with st.spinner("Casting..."):
        cast = suggest_cast(idea=idea, genre=genre, top_k=cast_n)

    st.subheader("Script (3 scenes)")
    st.code(script_text)

    st.subheader("Poster")
    st.image(poster_path, caption="Auto-generated offline poster", use_column_width=True)
    st.download_button("Download Poster", data=open(poster_path,"rb").read(), file_name=poster_path.split("/")[-1])

    st.subheader("Suggested Cast")
    st.table(cast)

    # Save a mini project bundle
    pid = random_id()
    proj_dir = f"projects/{slugify(title)}-{pid}"
    import os
    os.makedirs(proj_dir, exist_ok=True)
    save_text(f"{proj_dir}/script.txt", script_text)
    os.system(f"cp '{poster_path}' '{proj_dir}/poster.png'")
    st.success(f"Saved project to {proj_dir}")
    st.write("You can commit the `projects/` folder to GitHub as examples.")

st.caption("Tip: Turn on OpenAI via `.env` for fancier outputs. This app works offline too!")
