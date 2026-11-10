# Dashboards and data-dense screens

A dashboard exists to answer a few recurring questions quickly. Design from the questions, not
from the widgets available.

## Start with the questions

Before layout, list the 3–5 questions this screen must answer (e.g. "Are we on track this month?",
"What broke since yesterday?", "Which accounts need attention?"). Each question gets one
region. Anything that does not serve a question goes to a detail page.

## Layout order

1. **Context bar**: title, scope (workspace, environment), time range, filters. Time range and
   filters are reflected in the URL.
2. **Headline numbers**: 3–5 key metrics, not 12. The most important one may be larger.
3. **Trends**: the charts that explain the headline numbers.
4. **Detail**: tables or lists people act on (rows that need attention, recent events).

Avoid equal-weight layouts where every tile has the same size and emphasis. Importance should be
visible in size, position and weight.

## Metric tiles

- Label (what), value (how much, with unit), comparison (change versus a stated period), and
  optionally a sparkline. Example structure: "Net revenue · $48,210 · +6.2% vs last month".
- State the comparison period. "+12%" with no baseline is meaningless.
- Color the delta by meaning, not by sign: a rising error rate is bad even though it went up.
  Pair color with an arrow or sign for color-blind users.
- `tabular-nums`, consistent decimal places, abbreviated large numbers (48.2k) with the exact
  value available on hover or in a detail view.
- Never invent numbers. With no real data, use obviously sample data and say so.

## Charts

- Choose the chart by the question:
  - change over time: line (or bar for few, discrete periods)
  - comparison across categories: horizontal bar, sorted
  - part of a whole: stacked bar, or a pie/donut only with 2–4 slices
  - distribution: histogram or box plot
  - relationship: scatter
- Label lines and series directly instead of relying on a distant legend. Start bar axes at zero.
- Remove chart junk: no 3D, no heavy gridlines (light horizontal ones at most), no drop shadows,
  no gradient fills that suggest data that is not there.
- Use a color-blind-safe categorical palette with at most 5–7 hues; use one hue for one series
  and gray for context. Highlight the series that matters, mute the rest.
- Tooltips show exact values and dates; charts have a text alternative (a summary sentence or
  an accessible data table).
- Each widget handles its own loading, empty ("No events in this period") and error states
  independently; one failed widget never blanks the whole page.

## Density

- Data-heavy tools can be denser than marketing pages: 14px UI text, 32–40px rows, 12–16px
  gaps. Keep a clear section rhythm (24–32px between regions) so density does not become noise.
- Offer a compact/comfortable density toggle for tables used all day.
- Use whitespace and alignment for grouping; reserve borders for table structure.

## Interaction

- Filters and time range apply to the whole page and are always visible; the active filters
  are shown as removable chips.
- Every number and chart segment that represents a set of things links to that set.
- Refreshing data does not reset scroll, selection or expanded rows. Show "Updated 2 min ago"
  and a manual refresh.
- Real-time data animates changes subtly (brief highlight), not with constant motion.
