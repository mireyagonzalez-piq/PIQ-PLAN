# PIQ Performance Pulse — full replica

One-file rebuild of `piq-pulse-flow.base44.app`, recovered from the deployed
Base44 bundle (no Base44 account needed). Everything runs in the browser from
this folder — no build step, no backend, no database.

## Run it

```bash
python3 serve.py            # http://127.0.0.1:8899/index.html
```

Or open `index.html` directly in a browser (works from `file://` too — the
two Google Apps Script endpoints allow cross-origin GETs).

To put it online free: drag `index.html` into **Netlify Drop**
(app.netlify.com/drop) or push to a GitHub repo and enable **GitHub Pages**.

## What's inside

| Piece | Source |
|---|---|
| `index.html` | The whole app: React 18 + Recharts + Tailwind (CDN), one Babel script |
| `serve.py` | Tiny local static server (optional) |

## Data sources (unchanged, live)

- Weekly AM data: `...AKfycbzOLFD...cqvac0/exec` (sheet tabs Roberto, Eduardo, Tania, Estefania, Lorena, Maria)
- GlockApps results: `...AKfycbwQKTNW.../exec?type=glockapps` (sheet tab `GA - Results`)

Both endpoints are read-only GETs from the browser — same as the original app.

## Config (top of the `<script type="text/babel">` block in `index.html`)

| Constant | Default | Notes |
|---|---|---|
| `APPS_SCRIPT_URL` | weekly endpoint | swap if you redeploy the Apps Script |
| `GA_APPS_SCRIPT_URL` | GlockApps endpoint | `?type=glockapps` appended automatically |
| `MANAGER_PASSWORD` | `PIQManager2026` | same as production |
| `IN_PROGRESS_MISSING_THRESHOLD` | 10 | GA test with Missing% ≥ this = still running |
| `INBOX_REPLACE_BELOW` | 40 | Critical panel: "Replace domain" |
| `INBOX_HALFVOLUME_BELOW` | 50 | Critical panel: "Half volume 2w" |
| `REFRESH_COOLDOWN_MS` | 600000 | 10-min manual-refresh cooldown |

## Features (1:1 with production)

Team view: Top Performers · summary cards · client spotlight picker + spotlight
card (PNG/CSV export, best/worst week) · AM weekly trend chart (metric tabs +
lead-source filter) · Vertical Breakdown (metric tabs, period-over-period
arrows, per-vertical client table) · Lead Source Comparison (4/8/12w, custom
range, per-AM filter, ZoomInfo focus table) · AM breakdown modal.

Manager view (password `PIQManager2026`, client-side only — same as original):
Manager banner · **Deliverability (GlockApps)** (client table weighted by
mailbox count, Critical/Needs-Action panel, Tests Running chips, per-client
domain drilldown, Affected Domains modal) · Ask the Dashboard · AM Performance
(Team Overview + Client Detail) · Client Risk Alerts (4 categories) · Reply
Rate Buckets · Monthly Rollup.

Time controls: last 1/4/8/12 weeks or custom date range, phase filter
(Active · Retention · Offboarding), 10-min refresh cooldown, current-week
incompleteness warning.

## Known differences from the original

1. **Ask the Dashboard** — Base44's built-in LLM call doesn't exist outside
   Base44. This replica asks for an **OpenAI API key** (stored in your browser
   localStorage only, sent directly to api.openai.com). Without a key the
   panel explains how to add one; everything else works without it.
2. **Hosting** — the original runs on Base44 (login wall, their runtime).
   This version is a static page: the manager password gates the UI only,
   exactly like the original did. Both Apps Script endpoints were already
   public/unauthenticated in production.
3. Charts use the same Recharts library, so visuals match, but fonts/spacing
   come from Tailwind CDN rather than Base44's compiled CSS — cosmetically
   near-identical, not pixel-identical.

## Recovered constants (embedded, verbatim from production bundle)

- AM colors: Maria `#7F77DD`, Eduardo `#2D9E2D`, Estefania `#E8621A`,
  Roberto `#378ADD`, Tania `#D4A017`
- Client→AM override map (mainwall→Estefania, kids venture→Roberto,
  quicktake→Maria, …) and `Brunna→Maria` fallback
- 214-entry vertical grouping map (`Tax management → Accounting & Tax`, …)
- ICP threshold 0.02%, risk-alert vertical threshold 0.015%,
  high-volume flag ≥1,000 emails/wk with <0.1% reply rate, PRs-not-converting
  flag ≥3 PRs with 0 MB, week-label parser (Nov 2025 / 2026 year handling)
