# CDT in AI Annual Conference 2026 — website

Static site for the Coventry University Centre for Doctoral Training in AI annual conference,
**Artificial Intelligence across Domains: Research, Innovation and Impact**, Wednesday 7 October 2026.

Plain HTML/CSS/JS, no build tooling required for hosting.

## Editing content

All page content lives in `build.py` (one shared header/footer, one block per page).
After editing, regenerate the HTML and commit both:

```bash
python3 build.py
```

You can also edit the `.html` files directly, but the nav/footer is duplicated across pages,
so `build.py` is the safer place to change anything shared.

- Styles: `assets/css/style.css` (palette variables at the top)
- Scripts: `assets/js/main.js` (mobile menu, countdown, past-date greying)
- Images: `assets/img/` (`logo.png`, `poster.png`, `favicon.png`)

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
