import os
import re
import html

# Root output directory
OUTPUT_DIR = "/Users/arunkumar/.gemini/antigravity-ide/scratch/agastyanadijyotish-site/dist"
BASE_URL = "https://agastyanadijyotish.com"

# Shared Header Component
HEADER_TEMPLATE = """
<a href="#main-content" class="skip-link">Skip to main content</a>
<header class="site-header">
  <div class="container header-container">
    <a href="{lang_prefix}/" class="logo-area" aria-label="Agastya Nadi Jyotish Home">
      <div class="logo-icon">🕉</div>
      <div class="logo-text">
        Agastya Nadi Jyotish
        <span>Vaitheeswaran Koil Palm Leaf Reading</span>
      </div>
    </a>
    
    <button class="mobile-toggle" id="mobile-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
      ☰
    </button>
    
    <nav class="main-nav" id="main-nav" aria-label="Main Navigation">
      <ul class="nav-list">
        <li><a href="{lang_prefix}/" class="nav-link {nav_home_active}">Home</a></li>
        <li><a href="{lang_prefix}/about/" class="nav-link {nav_about_active}">About Nadi</a></li>
        <li><a href="{lang_prefix}/nadi-jyotish-online/" class="nav-link {nav_online_active}">Online Reading</a></li>
        <li><a href="{lang_prefix}/vaitheeswaran-koil/" class="nav-link {nav_koil_active}">Vaitheeswaran Koil</a></li>
        <li><a href="{lang_prefix}/blog/" class="nav-link {nav_blog_active}">Blog</a></li>
        <li><a href="{lang_prefix}/gallery/" class="nav-link {nav_gallery_active}">Gallery</a></li>
        <li><a href="{lang_prefix}/contact/" class="nav-link {nav_contact_active}">Contact</a></li>
      </ul>
      
      <div class="lang-switcher">
        <a href="{en_url}" class="lang-link {lang_en_active}">EN</a>
        <a href="{hi_url}" class="lang-link {lang_hi_active}">हिन्दी</a>
      </div>
      
      <a href="{lang_prefix}/book-consultation/" class="btn btn-primary btn-sm">Book Reading</a>
    </nav>
  </div>
</header>
"""

# Shared Footer Component
FOOTER_TEMPLATE = """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="logo-text" style="color:#ffffff; margin-bottom: 1rem;">
          Agastya Nadi Jyotish
          <span style="color:var(--color-secondary-light);">Vaitheeswaran Koil Legacy</span>
        </div>
        <p style="font-size:0.9rem; line-height:1.6;">Authentic Agastya Nadi Astrology reading center based in Vaitheeswaran Koil, Tamil Nadu. Serving seekers worldwide with online video consultations and in-person leaf search services.</p>
        <p style="font-size:0.85rem; margin-top:1rem; color:#D1D5DB;"><strong>Phone/WhatsApp:</strong> [REPLACE: +91 98765 43210]</p>
        <p style="font-size:0.85rem; color:#D1D5DB;"><strong>Email:</strong> [REPLACE: info@agastyanadijyotish.com]</p>
      </div>
      
      <div>
        <h4 class="footer-title">Nadi Services</h4>
        <ul class="footer-links">
          <li><a href="{lang_prefix}/agastya-nadi-astrology/">Agastya Nadi Astrology</a></li>
          <li><a href="{lang_prefix}/nadi-jyotish-online/">Online Nadi Consultation</a></li>
          <li><a href="{lang_prefix}/how-nadi-reading-works/">How Reading Works</a></li>
          <li><a href="{lang_prefix}/payments/">Pricing & Payment Info</a></li>
          <li><a href="{lang_prefix}/book-consultation/">Book Consultation</a></li>
        </ul>
      </div>
      
      <div>
        <h4 class="footer-title">Vaitheeswaran Koil Guide</h4>
        <ul class="footer-links">
          <li><a href="{lang_prefix}/vaitheeswaran-koil/">Temple Hub Page</a></li>
          <li><a href="{lang_prefix}/vaitheeswaran-koil/vaidyanatha-swamy-temple/">Vaidyanatha Swamy Temple</a></li>
          <li><a href="{lang_prefix}/vaitheeswaran-koil/temples-nearby/">Temples Near Vaitheeswaran Koil</a></li>
          <li><a href="{lang_prefix}/vaitheeswaran-koil/shiva-temples-nearby/">Shiva Temples Nearby</a></li>
          <li><a href="{lang_prefix}/vaitheeswaran-koil/navagraha-temples-route-from-kumbakonam/">Navagraha Route Map</a></li>
        </ul>
      </div>
      
      <div>
        <h4 class="footer-title">City Consultations</h4>
        <ul class="footer-links">
          <li><a href="{lang_prefix}/agastya-nadi-jyotish-pune/">Nadi Jyotish Pune</a></li>
          <li><a href="{lang_prefix}/nadi-jyotish-delhi/">Nadi Jyotish Delhi</a></li>
          <li><a href="{lang_prefix}/nadi-jyotish-mumbai/">Nadi Jyotish Mumbai</a></li>
          <li><a href="{lang_prefix}/nadi-jyotish-bangalore/">Nadi Jyotish Bangalore</a></li>
          <li><a href="{lang_prefix}/nadi-jyotish-hyderabad/">Nadi Jyotish Hyderabad</a></li>
        </ul>
      </div>
    </div>
    
    <div class="disclaimer-box">
      <strong>Important Spiritual Guidance Disclaimer:</strong> Agastya Nadi Jyotish and palm-leaf readings are traditional spiritual, philosophical, and astrological guidance systems based on ancient Tamil palm-leaf manuscripts. Consultations do not constitute professional medical, legal, financial, or psychological advice. Outcomes are not scientifically guaranteed. Visitors are encouraged to exercise personal discretion and free will in all decisions.
    </div>
    
    <div class="footer-bottom">
      <div>© {current_year} Agastya Nadi Jyotish. All rights reserved. Vaitheeswaran Koil, Tamil Nadu, India.</div>
      <div style="display:flex; gap:1rem;">
        <a href="{lang_prefix}/privacy-policy/">Privacy Policy</a> |
        <a href="{lang_prefix}/terms/">Terms of Service</a> |
        <a href="{lang_prefix}/disclaimer/">Disclaimer</a> |
        <a href="{lang_prefix}/faq/">FAQ</a>
      </div>
    </div>
  </div>
</footer>

<!-- Sticky Mobile CTA Bar -->
<div class="sticky-cta-bar">
  <a href="{lang_prefix}/book-consultation/" class="btn btn-primary">Book Consultation</a>
  <a href="https://wa.me/919876543210?text=Hello%2C%20I%20want%20to%20book%20a%20Nadi%20Jyotish%20consultation" class="btn btn-whatsapp" target="_blank" rel="noopener">WhatsApp</a>
</div>

<script src="/assets/js/main.js" defer></script>
"""

def render_page(path, title, description, h1, body_content, json_ld="", hreflang_en="", hreflang_hi="", is_hindi=False, nav_active=""):
  # Normalise path
  canonical_url = f"{BASE_URL}{path}"
  
  lang_prefix = "/hi" if is_hindi else ""
  lang_en_active = "active" if not is_hindi else ""
  lang_hi_active = "active" if is_hindi else ""
  
  # Calculate counterpart URLs
  if is_hindi:
    en_url = path.replace("/hi", "") or "/"
    hi_url = path
  else:
    en_url = path
    hi_url = f"/hi{path}" if path != "/" else "/hi/"
    
  if not hreflang_en:
    hreflang_en = f"{BASE_URL}{en_url}"
  if not hreflang_hi:
    hreflang_hi = f"{BASE_URL}{hi_url}"
    
  header_rendered = HEADER_TEMPLATE.format(
    lang_prefix=lang_prefix,
    nav_home_active="active" if nav_active == "home" else "",
    nav_about_active="active" if nav_active == "about" else "",
    nav_online_active="active" if nav_active == "online" else "",
    nav_koil_active="active" if nav_active == "koil" else "",
    nav_blog_active="active" if nav_active == "blog" else "",
    nav_gallery_active="active" if nav_active == "gallery" else "",
    nav_contact_active="active" if nav_active == "contact" else "",
    en_url=en_url,
    hi_url=hi_url,
    lang_en_active=lang_en_active,
    lang_hi_active=lang_hi_active
  )
  
  footer_rendered = FOOTER_TEMPLATE.format(
    lang_prefix=lang_prefix,
    current_year="2026"
  )
  
  html_doc = f"""<!DOCTYPE html>
<html lang="{'hi' if is_hindi else 'en'}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{canonical_url}">
  
  <!-- Hreflang Tags -->
  <link rel="alternate" hreflang="en" href="{hreflang_en}">
  <link rel="alternate" hreflang="hi" href="{hreflang_hi}">
  <link rel="alternate" hreflang="x-default" href="{hreflang_en}">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:image" content="{BASE_URL}/assets/images/og-default.jpg">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{canonical_url}">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(description)}">
  <meta name="twitter:image" content="{BASE_URL}/assets/images/og-default.jpg">
  
  <!-- Google Fonts Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="/assets/css/styles.css">
  
  {f'<script type="application/ld+json">{json_ld}</script>' if json_ld else ''}
</head>
<body>
  {header_rendered}
  
  <main id="main-content">
    {body_content}
  </main>
  
  {footer_rendered}
</body>
</html>
"""
  
  # Write file
  rel_filepath = path.lstrip('/')
  if not rel_filepath or rel_filepath.endswith('/'):
    rel_filepath = os.path.join(rel_filepath, 'index.html')
  
  full_out_path = os.path.join(OUTPUT_DIR, rel_filepath)
  os.makedirs(os.path.dirname(full_out_path), exist_ok=True)
  
  with open(full_out_path, 'w', encoding='utf-8') as f:
    f.write(html_doc)
  print(f"Generated: {path} -> {full_out_path}")

print("Build script framework ready.")
