from .utils import read_csv, extract_keywords

def _overlap(a, b):
    return len(a & b)

def suggest_cast(idea: str, genre: str, cast_db_path: str = "data/cast_db.csv", top_k: int = 5):
    rows = read_csv(cast_db_path)
    idea_kws = set(extract_keywords(idea, top_k=12) + extract_keywords(genre, top_k=5))
    ranked = []
    for r in rows:
        tags = set([t.strip().lower() for t in r["tags"].split(";") if t.strip()])
        score = _overlap(idea_kws, tags)
        ranked.append((r["name"], score, tags & idea_kws))
    ranked.sort(key=lambda x: (-x[1], x[0]))
    out = []
    for name, score, matched in ranked[:top_k]:
        out.append({"name": name, "score": int(score), "matched": ", ".join(sorted(matched))})
    return out
