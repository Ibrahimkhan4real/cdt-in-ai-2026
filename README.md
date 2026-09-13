# CDT in AI Annual Conference 2026 — website

Static site for the Coventry University Centre for Doctoral Training in AI annual conference,
**Artificial Intelligence across Domains: Research, Innovation and Impact**, Wednesday 7 October 2026.

Plain HTML/CSS/JS, no build tooling required for hosting. The layout implements the Claude Design file
`CDT in AI Conference 2026.dc.html` (navy / gold / warm off-white, hairline structure, Source Serif 4 + Source Sans 3 from Google Fonts).

## Editing content

All page content lives in `build.py` (one shared header/footer, one block per page).
After editing, regenerate the HTML and commit both. The build stamps a content hash onto the CSS and JS links so browsers never reuse a stale copy after a deploy:

```bash
python3 build.py
```

You can also edit the `.html` files directly, but the nav/footer is duplicated across pages,
so `build.py` is the safer place to change anything shared.

- Styles: `assets/css/site.css` (palette variables at the top)
- Scripts: `assets/js/site.js` (mobile menu, countdowns, programme timeline, calendar download)
- Images: `assets/img/` (`mark.png` square emblem used in header/footer, `poster.png`, `favicon.png`, `logo.png` full lock-up)

### Common edits

- **Keynote portraits**: in `build.py` replace the text inside `<div class="portrait">` with `<img src="assets/img/brusey.jpg" alt="Prof. James Brusey">`.
- **Programme rows**: edit the `SCHEDULE` array at the top of `assets/js/site.js`; both the timeline and table views render from it. On 7 October 2026 the home page shows a "Happening now" bar driven by the same data.
- **Add to calendar**: the buttons generate an `.ics` file in the browser; times are in `addToCalendar` in `site.js`.
- **Countdowns**: the deadline and conference dates are constants at the top of `site.js`.

## Publishing on GitHub Pages

1. Create a repository on GitHub (e.g. `cdt-in-ai-2026`) and push this folder to `main`.
2. Settings → Pages → Source: **Deploy from a branch** → Branch: `main`, folder `/ (root)` → Save.
3. The site appears at `https://<user-or-org>.github.io/<repo>/` within a minute or two.

All links are relative, so the site works at any repository path. `.nojekyll` disables Jekyll processing.

## Previewing locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000/.
