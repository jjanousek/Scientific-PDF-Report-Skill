#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import struct
import subprocess
from pathlib import Path


def run_command(args: list[str]) -> str:
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required command: {args[0]}") from exc
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip() or exc.stdout.strip()
        raise SystemExit(stderr or f"Command failed: {' '.join(args)}") from exc
    return result.stdout


def parse_pdfinfo(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a valid PNG")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a PDF to PNG pages and print a simple QA summary.")
    parser.add_argument("pdf", type=Path, help="Path to the PDF file.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Directory for rendered PNG pages. Defaults to tmp/pdfs/<pdf-stem> beside the PDF.",
    )
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    output_dir = args.output_dir.expanduser().resolve() if args.output_dir else pdf_path.parent / "tmp" / "pdfs" / pdf_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    output_prefix = output_dir / "page"

    pdfinfo_text = run_command(["pdfinfo", str(pdf_path)])
    info = parse_pdfinfo(pdfinfo_text)

    run_command(["pdftoppm", "-png", str(pdf_path), str(output_prefix)])
    png_pages = sorted(output_dir.glob("page-*.png"))

    print(f"PDF: {pdf_path}")
    if "Pages" in info:
        print(f"Pages (pdfinfo): {info['Pages']}")
    if "Page size" in info:
        print(f"Page size: {info['Page size']}")
    if "File size" in info:
        print(f"File size: {info['File size']}")
    print(f"Rendered PNGs: {len(png_pages)}")
    print(f"Output dir: {output_dir}")

    for page in png_pages:
        width, height = png_dimensions(page)
        size_kb = page.stat().st_size / 1024
        page_num_match = re.search(r"page-(\d+)\.png$", page.name)
        page_num = page_num_match.group(1) if page_num_match else page.name
        print(f"- page {page_num}: {width}x{height}px, {size_kb:.1f} KB")


if __name__ == "__main__":
    main()
