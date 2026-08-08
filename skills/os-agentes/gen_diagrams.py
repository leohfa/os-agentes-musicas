#!/usr/bin/env python3
"""Schematic diagrams for the /os-agentes README.

Editorial blueprint style: warm off-white paper, hand-drawn pen line work,
coral (#E07A4F) and teal (#2A9D8F) accents. Minimal text so labels render
cleanly (single-word layer names plus a short title).

Reads GOOGLE_API_KEY from the environment (or ~/.env if present).
Images are written next to this script.

Usage:
  python3 gen_diagrams.py                 # generate everything
  python3 gen_diagrams.py os-layers       # one diagram by key
"""
import os, sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.expanduser("~/.env"))
except Exception:
    pass

from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# Tried in order; first model that returns an image wins.
MODELS = ["gemini-3-pro-image-preview", "gemini-3.1-pro-image-preview", "gemini-3.1-flash-image"]

ROOT = Path(__file__).resolve().parent

STYLE = (
    "A premium hand-drawn editorial SCHEMATIC on warm off-white paper (#F4EEE2), the look of a beautiful "
    "architect's blueprint sketched by hand. Confident ink line work with light cross-hatching, The New Yorker "
    "quality, gently imperfect hand-drawn strokes (no ruler-straight lines, no gradients, no photorealism, no drop "
    "shadows). The palette is monochrome ink PLUS two restrained accents: a warm coral (#E07A4F) and a deep teal "
    "(#2A9D8F), used only to highlight key elements. Clean, airy, balanced composition with generous margins."
)

BAN = (
    "BANNED: no URL, website, dot-com, social handle, signature, brand logo, copyright text, QR code, watermark, "
    "no 'AI generated' tag, no author name, no fake UI chrome, no random numbers. Keep ALL text to ONLY the labels "
    "explicitly listed in this prompt, spelled exactly as written, and nothing else. No misspelled or invented words."
)

DIAGRAMS = {
    # key: (aspect_ratio, prompt)
    "os-layers": (
        "16:9",
        STYLE + "\n\n"
        "Subject: a schematic of an 'Agentic OS' drawn as a clean stack of SIX horizontal layered slabs, like a "
        "cross-section of a well-built structure, viewed straight on with a slight hand-drawn isometric tilt. "
        "From BOTTOM (the foundation) to TOP, the six slabs are labelled exactly: "
        "1) IDENTITY (the bottom foundation slab, small and solid, the soul), "
        "2) SUBSTRATE (drawn as the LARGEST, thickest slab, clearly the biggest layer, the back of house), "
        "3) RULES (a medium slab with a tiny guardrail motif), "
        "4) SKILLS (a slab with a small gear or recipe-card motif), "
        "5) TOOLS (a slab with little one-way pipe/plug motifs on its edge), "
        "6) AGENTS (the top slab with a small round-headed doodle figure standing on it). "
        "On the right, a single slim hand-drawn upward arrow labelled 'BUILD ORDER' shows you build from Identity up to Agents. "
        "Render IDENTITY's foundation and the SUBSTRATE slab outline in coral, and the BUILD ORDER arrow in teal; everything else monochrome ink. "
        "Title in bold hand-drawn capitals at the very top: 'THE AGENTIC OS'. "
        "The only readable text in the whole image: the title, the six layer words, and 'BUILD ORDER'. " + BAN
    ),
    "agentes-loop": (
        "16:9",
        STYLE + "\n\n"
        "Subject: a schematic of a repeating coaching cycle, drawn as a clean circular flow with four labelled "
        "stations connected by hand-drawn curved arrows moving clockwise. The four stations, clockwise from the top: "
        "ASK (a small speech bubble holding two or three question marks), BUILD (a hand placing a small file-and-folder), "
        "PERSIST (a small notebook with a pen writing a line in it), NEXT (a forward step arrow nudging a small stack of slabs up by one). "
        "In the exact CENTER of the loop sits one small open notebook labelled 'memory.md' that every station connects to with thin lines, "
        "the shared memory the cycle reads and writes. Off to the right, slightly apart from the ring, a fifth station labelled AUDIT, "
        "drawn as a magnifying glass held over a small six-row scorecard, with a gentle dashed feedback arrow curving from AUDIT back into the ring. "
        "Render the central 'memory.md' notebook and the four clockwise loop arrows in coral, and the AUDIT magnifier and its dashed feedback arrow in teal; everything else monochrome ink. "
        "Title in bold hand-drawn capitals at the very top: 'ONE SMALL STEP AT A TIME'. "
        "The only readable text in the whole image: the title, ASK, BUILD, PERSIST, NEXT, AUDIT, and memory.md. " + BAN
    ),
}


def generate(key, aspect, prompt):
    out = ROOT / f"{key}.png"
    last_err = None
    for model in MODELS:
        try:
            print(f"[{key}] trying {model} ...", flush=True)
            resp = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(aspect_ratio=aspect),
                ),
            )
            for part in resp.parts:
                if hasattr(part, "inline_data") and part.inline_data:
                    part.as_image().save(str(out))
                    print(f"  saved {out.name} via {model} ({out.stat().st_size/1024:.0f} KB)", flush=True)
                    return True
            print(f"  no image from {model}", file=sys.stderr, flush=True)
        except Exception as e:
            last_err = e
            print(f"  {model} failed: {e}", file=sys.stderr, flush=True)
    print(f"  ERROR {key}: all models failed. last: {last_err}", file=sys.stderr, flush=True)
    return False


def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    ok = total = 0
    for key, (aspect, prompt) in DIAGRAMS.items():
        if only and key not in only:
            continue
        total += 1
        ok += 1 if generate(key, aspect, prompt) else 0
    print(f"\nDONE: {ok}/{total} diagrams", flush=True)


if __name__ == "__main__":
    main()
