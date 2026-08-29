# Tokoroa Kart Club Website

A simple, static website for the Tokoroa Kart Club (KartSport Tokoroa), built
around the Karting New Zealand brand system.

## Structure

```
index.html            Home
membership.html        Membership
race-days.html         Race Days
practice.html          Practice
getting-started.html   Getting Started
css/style.css          Shared styles / design system
js/main.js             Mobile nav toggle, footer year
assets/logo/           Club logo files + favicons
render.yaml            Render static site config
```

No build step, no framework, no database — just plain HTML/CSS/JS, so it's
easy to hand-edit later and cheap to host.

## Brand notes

- **Headings** use **Coda** (Google Font) in place of Karting New Zealand's
  proprietary **Coanda** typeface.
- **Bold / UI text** (nav, buttons, labels, strong text) uses **Rubik**.
- **Body copy** uses **Inter**, standing in for Replica Pro Light/Regular.
- **Colours:** club orange `#f6993f` is the primary accent, with KNZ's
  black/white base palette and cobalt blue `#005fdc` used sparingly for
  secondary accents (matching the June 2026 KNZ Brand Guidelines).
- The angled "image container" blocks and skewed accent bars echo the KNZ
  design system's line/angle motif, taken from the shape of the K device.

## Known placeholders to fill in later

1. **Photos** — every `.img-box` block is a placeholder for a real photo.
   Replace by swapping the `<div class="img-box ...">` for an `<img>` tag
   (keep the class for the angled clip-path, or drop it for a plain image).
2. **Google Calendar embed** — on `race-days.html`, replace the
   `.calendar-embed` placeholder block with a live `<iframe>` once you have
   the public calendar's embed URL from Google Calendar's sharing settings.
3. **Race day dates / entry links** — update `race-days.html` each season.

## Deploying on Render

1. Push this folder to a GitHub/GitLab repo.
2. In Render, choose **New > Static Site** and connect the repo.
3. Build command: leave blank. Publish directory: `.` (repo root).
4. The included `render.yaml` (Render "Blueprint") will configure this
   automatically if you use **New > Blueprint** instead and point it at the
   repo — it sets a single-page rewrite to `index.html` and basic caching
   headers.
5. Once deployed, point your domain (e.g. `kartsporttokoroa.co.nz`) at the
   Render static site via a custom domain in the Render dashboard.

No environment variables or secrets are required.
