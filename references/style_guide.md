# Scientific PDF Report Style Guide

## Visual direction

Use a clean scientific-report look:

- `#2E2A27` ink
- `#766D63` slate
- `#A67C3D` ochre
- `#6B7B69` sage
- `#A66252` brick
- `#F7F1E6` paper
- `#FBF8F0` paper-alt
- `#D6CCBB` line

Typography:

- serif titles and body copy
- strong but restrained hierarchy
- avoid oversized hero styling

## Layout patterns

- for PC-reviewed PDFs, prefer full-bleed beige pages with internal gutters instead of a wide white print border
- short lede plus stat strip on page 1
- bordered sections with 1 to 2 visuals per section
- compact tables with light borders and alternating fills
- case cards instead of oversized operational tables
- short captions that explain the business point

Screen-first default:

- `@page { size: A4; margin: 0; }`
- main content padding around `14mm`
- edge-to-edge paper color

Print-like fallback:

- use a small outer page margin only if the reviewer is likely to print the report
- keep that margin thin; avoid oversized white borders

Document-type defaults:

- full report: stronger hierarchy is fine, but keep it disciplined
- addendum or verification note: use a simple single-column memo layout unless the content clearly needs more
- appendix or technical note: bias toward plain section blocks, compact tables, and minimal ornament
- if the content is mostly text, do not force metric strips, case cards, or dashboard framing onto the page

Anti-clutter rule:

- fewer lines beat more lines
- fewer labels beat more labels
- remove visual separators before shrinking type
- branding can stay light and quiet; it should not become a second layer of content

## Figure guidance

Good report-sized figures:

- heatmaps with short labels
- line charts with direct labels
- grouped bars for comparisons
- horizontal bars for ranking and concentration

Weak report-sized figures:

- sparse scatterplots with lots of empty space
- charts with full-sentence x-axis labels
- plots that need a long title and a long legend

## Common fixes

- overprinted labels: shorten stage names or switch to direct labels
- title / legend collision: remove legend title, move legend inside plot, shorten the chart title
- figure too dense: simplify text inside the graphic and push context to the caption
- table too wide: convert to summary table plus case cards
- page too empty: cut duplicated prose or enlarge the figure
- page too dense: remove weak visuals before shrinking everything
- addendum feels overdesigned: strip stat strips, numbered shells, extra rules, and decorative callouts
- wording assumes hidden context: rewrite so the paragraph stands alone for a new reader
- repeated idea across sections: keep the thought where it belongs and delete the echo elsewhere

## QA checklist

- no clipped or cut-off content
- no stranded headings
- no half-empty pages unless intentional
- no stale or provenance-heavy language
- no visual whose labels disappear at PDF scale
- no chart whose form is working against the page size
- no memo-like document that accidentally reads like a dashboard
- no insider shorthand left unexplained
- rerender and reinspect after each meaningful layout or styling change, not just once at the end
