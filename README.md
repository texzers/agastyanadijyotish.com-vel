# Agastya Nadi Jyotish - Production Static Website

A complete, production-ready, highly SEO-optimized static HTML website for `agastyanadijyotish.com` (Agastya Nadi Jyotish service & Vaitheeswaran Koil travel guide).

## Project Features
- **Zero Client Frameworks**: Pure HTML5, CSS3, Vanilla JS.
- **Python Static Builder (`build_site.py`)**: Assembles shared headers, footers, breadcrumbs, JSON-LD schemata, and per-page SEO metadata into standalone static HTML files.
- **Complete Architecture**: 40 generated static pages (Core services, City landing pages, Vaitheeswaran Koil travel guide, Navagraha route map, Blog index with 8 seed posts, legal pages, and Hindi track).
- **Core Web Vitals & Accessibility**: WCAG AA color contrast (Saffron/Maroon/Cream palette), tap targets >= 48px, sticky mobile CTA bar, skip-to-content links.
- **Technical SEO**: Absolute HTTPS production canonicals, bi-directional `en`/`hi` `hreflang` tags, `sitemap.xml`, `robots.txt`, and zero `localhost` references.

## Folder Structure
```
agastyanadijyotish-site/
├── assets/
│   ├── css/
│   │   └── styles.css          # Design system stylesheet
│   ├── js/
│   │   └── main.js            # Vanilla JS (nav, accordion, form validation, analytics)
│   └── images/                # Gallery & OG image assets
├── dist/                      # SHIPPED PRODUCTION FILES (HTML, sitemap.xml, robots.txt)
├── build_site.py              # Python SSG generator script
├── keywords.md                # Keyword map & SEO launch checklist
├── PLACEHOLDERS.md            # List of placeholders to replace before launch
└── README.md                  # Instructions
```

## How to Preview Locally
You can preview the production website using Python's built-in HTTP server:

```bash
cd /Users/arunkumar/.gemini/antigravity-ide/scratch/agastyanadijyotish-site/dist
python3 -m http.server 8080
```
Then open `http://localhost:8080/` in your browser.

## How to Re-build
If you update `build_site.py` or `assets/`, run:
```bash
python3 build_site.py
python3 -c "import os; os.system('cp assets/css/styles.css dist/assets/css/styles.css'); os.system('cp assets/js/main.js dist/assets/js/main.js')"
```

## Deployment Instructions
The entire contents of the `dist/` directory can be uploaded directly to any static web host:
- **Netlify / Vercel**: Drag and drop the `dist/` folder or link to your Git repository with `dist` as the publish directory.
- **GitHub Pages**: Deploy the `dist/` folder to your `gh-pages` branch.
- **Apache / Shared Hosting (cPanel)**: Upload the contents of `dist/` into `public_html/`.
