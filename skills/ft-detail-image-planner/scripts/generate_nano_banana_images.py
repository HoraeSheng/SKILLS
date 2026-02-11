#!/usr/bin/env python3
"""Generate product showcase/creative images with Nano Banana model.

This script reads source image references and prompt requirements, then calls
an image-generation API compatible with OpenAI-style endpoints.

Example:
  python scripts/generate_nano_banana_images.py \
    --reference references/product-original-images.md \
    --prompt "Create a clean ecommerce hero image on white background" \
    --output-dir outputs \
    --dry-run
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate images via Nano Banana model")
    parser.add_argument("--reference", required=True, help="Path to product image reference markdown file")
    parser.add_argument("--prompt", required=True, help="Rendering instruction for showcase/creative image")
    parser.add_argument("--output-dir", default="outputs", help="Directory to save generated images")
    parser.add_argument("--model", default="nano-banana", help="Model name")
    parser.add_argument("--size", default="1536x1024", help="Image size")
    parser.add_argument("--n", type=int, default=1, help="How many images to generate")
    parser.add_argument("--api-base", default=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    parser.add_argument("--api-key", default=os.getenv("OPENAI_API_KEY"))
    parser.add_argument("--dry-run", action="store_true", help="Print request payload without API call")
    return parser.parse_args()


def extract_image_paths(reference_text: str) -> List[str]:
    # Matches markdown table/file paths like assets/original-images/xxx.jpg
    pattern = r"(?:^|\s)(assets/original-images/[^\s|]+\.(?:jpg|jpeg|png|webp))"
    return sorted(set(re.findall(pattern, reference_text, flags=re.IGNORECASE | re.MULTILINE)))


def encode_image(path: Path) -> str:
    data = path.read_bytes()
    return base64.b64encode(data).decode("utf-8")


def build_payload(model: str, prompt: str, images_b64: List[str], size: str, n: int) -> dict:
    # OpenAI-compatible /images/generations payload with optional image conditioning.
    # Some providers may ignore "input_images"; keeping it for Nano-Banana compatibility layers.
    return {
        "model": model,
        "prompt": prompt,
        "size": size,
        "n": n,
        "input_images": images_b64,
    }


def request_generation(api_base: str, api_key: str, payload: dict) -> dict:
    endpoint = api_base.rstrip("/") + "/images/generations"
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"API request failed: {exc.code} {exc.reason}\n{detail}") from exc


def save_results(result: dict, out_dir: Path) -> List[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: List[Path] = []

    for idx, item in enumerate(result.get("data", []), start=1):
        b64 = item.get("b64_json")
        if not b64:
            continue
        img_bytes = base64.b64decode(b64)
        out = out_dir / f"nano-banana-{idx:02d}.png"
        out.write_bytes(img_bytes)
        paths.append(out)

    return paths


def main() -> int:
    args = parse_args()
    ref_path = Path(args.reference)
    if not ref_path.exists():
        print(f"Reference not found: {ref_path}", file=sys.stderr)
        return 2

    ref_text = ref_path.read_text(encoding="utf-8")
    image_paths = [Path(p) for p in extract_image_paths(ref_text)]

    missing = [str(p) for p in image_paths if not p.exists()]
    if missing:
        print("Warning: Some referenced images do not exist yet:")
        for m in missing:
            print(f"- {m}")

    images_b64 = [encode_image(p) for p in image_paths if p.exists()]
    payload = build_payload(args.model, args.prompt, images_b64, args.size, args.n)

    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2)[:4000])
        return 0

    if not args.api_key:
        print("OPENAI_API_KEY is required unless --dry-run is used.", file=sys.stderr)
        return 2

    result = request_generation(args.api_base, args.api_key, payload)
    saved = save_results(result, Path(args.output_dir))
    if not saved:
        print("No images returned by API. Raw response:")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1

    print("Generated images:")
    for p in saved:
        print(f"- {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
