#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Copy a starter HTML template for a scientific PDF document.")
    parser.add_argument(
        "--type",
        choices=["report", "addendum", "appendix"],
        required=True,
        help="Template type to copy.",
    )
    parser.add_argument("--output", required=True, type=Path, help="Destination HTML path.")
    parser.add_argument("--force", action="store_true", help="Overwrite the destination if it exists.")
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    assets_dir = skill_dir / "assets"
    template_map = {
        "report": assets_dir / "report_template.html",
        "addendum": assets_dir / "addendum_template.html",
        "appendix": assets_dir / "appendix_template.html",
    }

    source = template_map[args.type]
    destination = args.output.expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {destination}")

    shutil.copyfile(source, destination)
    print(f"Copied {source.name} -> {destination}")


if __name__ == "__main__":
    main()
