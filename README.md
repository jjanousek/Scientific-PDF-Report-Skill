# Scientific PDF Report Skill

A Codex skill for creating and polishing scientific or analytical PDF reports with:

- HTML-to-PDF composition
- reusable report, addendum, and appendix templates
- page-by-page visual QA with rendered PNGs
- writing guidance for clearer, less generic report prose

## What this skill includes

- `SKILL.md` with workflow and design guidance
- `assets/` with starter HTML templates
- `references/` with style and writing checks
- `scripts/new_report.py` to scaffold a starter template
- `scripts/qa_pdf.py` to render PDF pages and print a QA summary

## Templates

- `assets/report_template.html` for fuller analytical reports
- `assets/addendum_template.html` for short addenda or memo-like PDFs
- `assets/appendix_template.html` for technical appendices
- `assets/scientific_report_template.html` for a strong general-purpose scientific report starter

## Example usage

Create a starter file:

```bash
uv run python scripts/new_report.py --type report --output draft_report.html
uv run python scripts/new_report.py --type addendum --output draft_addendum.html
uv run python scripts/new_report.py --type appendix --output draft_appendix.html
```

Run PDF QA:

```bash
uv run python scripts/qa_pdf.py path/to/report.pdf --output-dir tmp/pdfs/report
```

## Design philosophy

This skill is meant to help produce reports that are:

- visually polished without being overdesigned
- appropriate to the document type
- readable in PDF, not just in HTML
- specific and self-contained in their writing

Full reports can carry stronger hierarchy and visual framing. Short addenda and verification notes should stay much simpler.

## Notes

- The skill assumes a `uv`-based Python workflow.
- Visual QA is part of the workflow, not an optional final check.
- The rendered PDF should match the intended document type: report, addendum, appendix, or memo.
