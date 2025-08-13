import os, math, random
from PIL import Image, ImageDraw, ImageFont
from .utils import slugify

def _draw_gradient_poster(title: str, subtitle: str, style: str, w=768, h=1152):
    img = Image.new("RGB", (w, h), (10, 10, 20))
    draw = ImageDraw.Draw(img)
    font_title = ImageFont.truetype("arial.ttf", 48)
    font_subtitle = ImageFont.truetype("arial.ttf", 24)

    # simple vertical gradient
    for y in range(h):
        r = int(20 + 80 * (y / h))
        g = int(20 + 30 * (y / h))
        b = int(40 + 120 * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # title box
    margin = 40
    # Try to load a common font, fallback to default
    try:
        font_title = ImageFont.truetype("arial.ttf", 15)
        font_subtitle = ImageFont.truetype("arial.ttf", 10)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()

    # draw central rectangle
    rect_h = int(h * 0.28)
    rect_y = int(h * 0.35)
    draw.rectangle([(margin, rect_y), (w - margin, rect_y + rect_h)], outline=(240,240,240), width=3)
    # text
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]  # text width
    th = bbox[3] - bbox[1]
    draw.text(((w - tw)//2, rect_y + 30), title, fill=(245,245,245), font=font_title)
    bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
    tw = bbox[2] - bbox[0]  # text width
    th = bbox[3] - bbox[1]
    sw = bbox[2] - bbox[0]
    draw.text(((w - sw)//2, rect_y + 40 + th), subtitle, fill=(230,230,230), font=font_subtitle)

    # style tag
    tag = f"Style: {style}"
    bbox_tag = draw.textbbox((0,0), tag, font=font_subtitle)
    tg_w = bbox_tag[2] - bbox_tag[0]
    tg_h = bbox_tag[3] - bbox_tag[1]
    draw.text((w - tg_w - margin, h - tg_h - margin), tag, fill=(230,230,230), font=font_subtitle)

    return img

def generate_poster(idea: str, title: str, style: str, env: dict, out_dir="outputs"):
    import textwrap
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{slugify(title)}-poster.png"
    path = os.path.join(out_dir, filename)

    # prepare subtitle
    subtitle_text = idea[:120] + ("..." if len(idea) > 120 else "")
    
    # Offline poster
    img = _draw_gradient_poster(title=title, subtitle=subtitle_text, style=style)
    img.save(path)
    return path
