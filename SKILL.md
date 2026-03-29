---
name: "scientific-pdf-report"
description: "Use when tasks involve creating or polishing leadership-readable scientific or analytical PDF reports with a clean paper-like style, HTML-to-PDF layout, strong charts, and page-by-page visual QA."
---

# Scientific PDF Report

Use this skill when the user wants a clean scientific report aesthetic rather than a slide deck, notebook export, or generic markdown PDF.

## When to use

- applied-science take-homes
- executive analytical reports
- model-readout PDFs
- appendix or addendum PDFs where layout quality matters
- any PDF where the figures look fine in isolation but weak in the rendered report

## Default style

Aim for a restrained pen-and-paper look:

- off-white or beige paper tones
- serif typography
- muted accent colors
- light structure, not decorative clutter
- compact, readable pages
- 4 to 6 strong visuals rather than many weak ones

Match the visual weight to the document's role:

- full reports can carry stronger hierarchy, compact metric panels, and a few deliberate framing motifs
- short addenda, appendices, and verification notes should stay much simpler
- keep branding elements such as logo, footer, and paper tone if useful, but do not force dashboards, stat strips, case cards, or numbered section systems into documents that are basically short memos
- if a page starts feeling busy, remove lines, boxes, and labels before adding new structure

For screen-first PDFs, prefer a full-bleed page treatment:

- set `@page` margin to `0` by default
- let the paper tone run to the edge of the page
- keep internal content padding around `12mm` to `16mm`
- only keep an outer white print margin when the user explicitly wants a print-like document

Read `references/style_guide.md` before making a major report or redesign pass.

For a quick starting point, use the scaffold script or copy the closest template:

- `uv run python scripts/new_report.py --type report --output draft_report.html`
- `uv run python scripts/new_report.py --type addendum --output draft_addendum.html`
- `uv run python scripts/new_report.py --type appendix --output draft_appendix.html`

Template files:

- `assets/report_template.html` for a full scientific or analytical report
- `assets/addendum_template.html` for short addenda, verification notes, and memo-like PDFs
- `assets/appendix_template.html` for technical notes and appendix-heavy documents
- `assets/scientific_report_template.html` as the general-purpose starter

## Workflow

1. First decide what the document actually is: full report, appendix, addendum, memo, or figure-heavy technical note.
2. Prefer HTML/CSS as the composition layer when layout quality matters.
3. Generate figures and metrics first from the final pipeline.
4. Keep one source-of-truth metrics manifest for report numbers.
5. Choose the lightest layout that fits the document's purpose; do not start from a hero-heavy template unless the content really needs it.
6. Use compact tables, metric panels, and case cards only when they genuinely clarify the story.
7. Keep chart titles and axis labels short enough to survive PDF scaling.
8. Lock critical desktop layouts with explicit `@media print` rules when PDF rendering matters.
9. Export the PDF.
10. Render every page to PNG with `pdftoppm`.
11. Inspect both page renders and raw figure assets.
12. After every meaningful layout, styling, or copy-density change, rerender the PDF and inspect the updated PNGs again. Do not rely on the browser HTML view alone.
13. Fix defects at the source figure or layout, then rebuild.

## Print-stability pitfalls

- Do not use real HTML tables for decorative hero stats or summary cards.
- Avoid combining negative margins, `border-spacing`, transparency, and shadows in the same print-critical block.
- Prefer plain `div` grids with opaque backgrounds for metric strips.
- If a block looks correct in HTML but collapses or stacks in PDF, add explicit `@media print` rules instead of fighting it indirectly.
- After fixing one artifact, re-check for layout regressions elsewhere, especially page 1, section starts, and the final page.
- Too many horizontal rules, labels, and framing devices can make a PDF feel synthetic fast. Default to fewer visual separators than you think you need.

## Report-shaping heuristics

- Page 1 should establish the problem, the decision, and the operating recommendation.
- Each later page should carry one clear section idea plus only the visuals needed to support it.
- Diagnostics should support the story, not dominate it.
- Remove provenance language and stitched-draft phrasing from final artifacts.
- Borrow patterns from stronger sibling reports when useful, but transplant motifs rather than copying the whole structure.
- Good low-risk transplants include stat-strip layout, numbered section headers, compact case cards, and tighter caption style.
- Match structure to content density. If the document is short and text-forward, a plain single-column layout is usually better than a mini executive report shell.
- Prefer self-contained wording. Do not assume the reader saw internal notes, earlier drafts, or the report-building process.
- Replace insider shorthand such as "all-row summaries", "lane logic", or "hybrid-priority language" with plain explanations unless the term is immediately explained.
- If a section sounds generic, managerial, or vaguely polished, rewrite it with concrete nouns, decisions, constraints, and tradeoffs.
- For human-verification or reflection addenda, prefer a few clear sections over many micro-sections. A simple three-part structure is often enough: where AI helped, how the human reasoning worked, and what required human expertise.

## Writing quality

Treat report prose as part of the product, not filler around the charts.

- Prefer pragmatic, human-sounding language over grand or inflated phrasing.
- State what was decided, why it was decided, and what tradeoff it implied.
- Keep paragraphs self-sufficient; a reader should not need hidden context to understand them.
- Avoid "AI slop" patterns: repeated framing, empty intensifiers, fake precision, decorative synonyms, and paragraphs that sound polished but say little.
- When a sentence can be simpler, make it simpler.

## Chart rules

- Prefer heatmaps, grouped bars, line charts, and horizontal bars for report-sized visuals.
- Avoid full-sentence axis labels.
- Prefer direct labels over legends when possible.
- If a legend and title collide, shorten one and move the other inside the plot.
- If a scatter wastes space, replace it with a ranked bar or lollipop chart.

## Visual QA loop

Use these commands:

```bash
pdftoppm -png path/to/report.pdf tmp/pdfs/report
pdfinfo path/to/report.pdf
```

Or use the helper:

```bash
uv run python scripts/qa_pdf.py path/to/report.pdf --output-dir tmp/pdfs/report
```

Visual QA is required after each meaningful print-layout change, not just at the end.

Check for:

- clipped text
- cut-off tables
- half-empty pages
- compositing artifacts or border/shadow overlap bands
- unreadable labels after scaling
- title / legend collisions
- duplicated framing between section headers and figure titles
- over-designed pages where visual treatment overwhelms the content
- memo-like documents that were accidentally turned into dashboard-like layouts
- HTML/CSS structures that render differently in print than on screen

## Tooling

- Prefer `uv run python ...` for Python scripts.
- Prefer the `pdftoppm` Poppler workflow for inspection.
- Use HTML-to-PDF when the document needs strong visual hierarchy.
- Headless Chrome may apply responsive behavior unexpectedly in PDF, so protect key multi-column layouts with print-specific rules.

## References

- `references/style_guide.md` for design rules and failure patterns
- `references/writing_checks.md` for prose checks and anti-slop rewrites
- `assets/report_template.html` for a full report starter
- `assets/addendum_template.html` for short memo-like PDFs
- `assets/appendix_template.html` for appendices and technical notes
- `assets/scientific_report_template.html` for the general-purpose starter

## Done standard

Do not ship until the latest rendered PNG review shows no obvious visual defects, and make sure the rendered feel matches the intended document type: report, addendum, appendix, or memo.
