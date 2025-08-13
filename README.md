# 🎬 AI-Powered Movie Scene Generator (Beginner Friendly)

Create a mini "movie pitch" from a single idea:
- **Script outline** (3 short scenes)
- **Auto-generated poster** (offline fallback that works without any API)
- **Suggested cast** (based on idea + genre keywords)

> Designed so a *super beginner* can run it locally in minutes, then grow it into a standout GitHub project.

---

## 🧰 Tech Stack
- **Python 3.10+**
- **Streamlit** (simple web UI)
- **Pillow** (poster image generation in offline mode)
- Optional: **OpenAI** for text, image, and embeddings (if you have an API key)

---

## 🚀 Quick Start (No API needed)
### 1) Install Python
- Windows/macOS: install from the official Python site. During install on Windows, check **"Add Python to PATH"**.

### 2) Open a terminal in this project folder
You should see files like `app/ui.py`, `moviemake/` etc.

### 3) Create & activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 4) Install dependencies
```bash
pip install -r requirements.txt
```

### 5) Run the app
```bash
streamlit run app/ui.py
```
Your browser will open to a local URL. Type a movie idea and click **Generate**.
- You'll get a **3-part script**, a **poster image** (made with Pillow), and **cast suggestions**.

> This works **offline**. No API required.

---

## 🔑 (Optional) Use OpenAI for higher quality
1. Copy `.env.example` → `.env`
2. Put your key in `OPENAI_API_KEY=` and set `USE_OPENAI=1`
3. Restart the app

### Change models (optional):
- `OPENAI_TEXT_MODEL`, `OPENAI_IMAGE_MODEL`, `OPENAI_EMBED_MODEL` in `.env`.

> If you don't have an API key, skip this step. The app still works.

---

## 🗂 Project Structure
```
ai-movie-scene-generator-starter/
├── app/
│   └── ui.py              # Streamlit UI
├── moviemake/
│   ├── __init__.py
│   ├── utils.py           # helpers: keywords, file saving, dotenv
│   ├── prompts.py         # text prompt templates
│   ├── llm.py             # offline + OpenAI text generation
│   ├── poster.py          # offline poster w/ Pillow + optional OpenAI image
│   └── cast.py            # simple cast recommender (keyword overlap)
├── data/
│   ├── cast_db.csv        # small starter database of actors + tags
│   └── sample_ideas.txt
├── tests/
│   └── test_smoke.py      # quick offline smoke test
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📸 What you'll see
- A clean UI with an idea box, genre/style options
- Generated **script (3 scenes)** with titles
- A **poster image** (PNG) saved to `outputs/` you can open or download
- A **top-5 cast** list with reasons

---

## 🧪 Run tests
```bash
pytest -q
```

---

## 🧠 How it works (short)
- **Offline mode**: simple templated generator creates a 3-beat scene outline; Pillow draws a vertical poster with gradient and your title; cast is matched by keyword overlap against `data/cast_db.csv`.

- **OpenAI mode**: if enabled, text + image + embeddings come from the API for higher quality. Fallbacks are always available so the app never breaks.

---

## 📤 Publish to GitHub (beginner)
```bash
# if this is a new repo
git init
git add .
git commit -m "feat: movie scene generator (starter)"
# create an empty repo on GitHub named ai-movie-scene-generator
git branch -M main
git remote add origin https://github.com/<your-username>/ai-movie-scene-generator.git
git push -u origin main
```

Add screenshots and a short demo video to your README to stand out 🚀

---

## ✨ Ideas to Extend
- Add multiple poster styles (neon, vintage, watercolor)
- Support **storyboard**: 3–6 shot descriptions per scene
- Use a small vector DB (e.g., FAISS) for cast embeddings
- Add **“random director”** and **“soundtrack style”** pickers
- Export a **PDF pitch one-pager**

Enjoy building! 🎥
