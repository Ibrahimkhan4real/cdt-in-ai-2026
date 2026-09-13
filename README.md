# CDT in AI Annual Conference 2026 — website

Static site for the Coventry University Centre for Doctoral Training in AI annual conference,
**Artificial Intelligence across Domains: Research, Innovation and Impact**, Wednesday 7 October 2026.

Plain HTML/CSS/JS, no build tooling required for hosting. The layout implements the Claude Design file
`CDT in AI Conference 2026.dc.html` (navy / gold / warm off-white, hairline structure, Source Serif 4 + Source Sans 3 from Google Fonts).

## Editing content

All page content lives in `build.py` (one shared header/footer, one block per page).
After editing, regenerate the HTML and commit it together with any CSS/JS change. The build appends a content hash to the CSS and JS links, so a rebuilt page always fetches matching assets (the HTML itself can be cached by browsers for up to 10 minutes):

```bash
python3 build.py
```

You can also edit the `.html` files directly, but the nav/footer is duplicated across pages,
so `build.py` is the safer place to change anything shared.

- Styles: `assets/css/site.css` (palette variables at the top)
- Scripts: `assets/js/site.js` (mobile menu, countdowns, programme timeline, calendar download)
- Images: `assets/img/` (`mark.png` square emblem used in header/footer, `poster.png` full-size with `poster-web.jpg` shown inline, `favicon.ico`)

### Common edits

- **Keynote portraits**: `assets/img/brusey.jpg` is the Coventry University profile photo (Pure portal), cropped 4:5 at 380×475. For the second keynote, replace the placeholder text inside `<div class="portrait">` in `build.py` with an `<img>` the same way.
- **Programme rows**: edit the `SCHEDULE` objects at the top of `assets/js/site.js`; both the timeline and table views render from it. Confirmed presenter names go into the `slot()` calls in `build.py`. On 7 October 2026 the home page shows a "Happening now" bar driven by the same data.
- **Add to calendar**: the buttons generate an `.ics` file in the browser from the conference date constants at the top of `site.js`.
- **Countdowns**: the deadline and conference dates are constants at the top of `site.js`; the header note and the home page Countdown cell tick every second as `24d 13h 05m 42s`, falling back to "Today" / "Closes today" / "Thank you for joining us" / "Submissions closed".

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
