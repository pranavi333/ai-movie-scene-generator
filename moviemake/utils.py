import os, re, random, string, json
from datetime import datetime
from dotenv import load_dotenv

STOPWORDS = set("""a an the and or but if is it to for of in on with from as by be are was were this that those these you your our their his her its they them he she we i my me""".split())

def ensure_dirs():
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("projects", exist_ok=True)

def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return text or "project"

def extract_keywords(text: str, top_k: int = 12):
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text.lower())
    tokens = [t for t in text.split() if t and t not in STOPWORDS and len(t) > 2]
    # frequency-based simple keywords
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    # sort by freq then alphabetically
    ranked = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return [w for w,_ in ranked[:top_k]]

def random_id(n=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

def load_env():
    load_dotenv()
    use_openai = os.getenv("USE_OPENAI", "0").strip() == "1"
    return {
        "USE_OPENAI": use_openai,
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
        "OPENAI_TEXT_MODEL": os.getenv("OPENAI_TEXT_MODEL", "gpt-4o-mini"),
        "OPENAI_IMAGE_MODEL": os.getenv("OPENAI_IMAGE_MODEL", "gpt-image-1"),
        "OPENAI_EMBED_MODEL": os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small"),
    }

def save_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def read_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        header = None
        for line in f:
            line = line.strip()
            if not line: 
                continue
            if header is None:
                header = [h.strip() for h in line.split(",")]
                continue
            parts = [p.strip() for p in line.split(",")]
            rows.append(dict(zip(header, parts)))
    return rows
