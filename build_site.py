import os
import html
import json

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

<div class="sticky-cta-bar">
  <a href="{lang_prefix}/book-consultation/" class="btn btn-primary">Book Consultation</a>
  <a href="https://wa.me/919876543210?text=Hello%2C%20I%20want%20to%20book%20a%20Nadi%20Jyotish%20consultation" class="btn btn-whatsapp" target="_blank" rel="noopener">WhatsApp</a>
</div>

<script src="/assets/js/main.js" defer></script>
"""

pages_generated = []

def render_page(path, title, description, body_content, json_ld="", is_hindi=False, nav_active=""):
  canonical_url = f"{BASE_URL}{path}"
  
  lang_prefix = "/hi" if is_hindi else ""
  lang_en_active = "active" if not is_hindi else ""
  lang_hi_active = "active" if is_hindi else ""
  
  if is_hindi:
    en_url = path.replace("/hi", "") or "/"
    hi_url = path
  else:
    en_url = path
    hi_url = f"/hi{path}" if path != "/" else "/hi/"
    
  hreflang_en = f"{BASE_URL}{en_url}"
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
  
  rel_filepath = path.lstrip('/')
  if not rel_filepath or rel_filepath.endswith('/'):
    rel_filepath = os.path.join(rel_filepath, 'index.html')
  
  full_out_path = os.path.join(OUTPUT_DIR, rel_filepath)
  os.makedirs(os.path.dirname(full_out_path), exist_ok=True)
  
  with open(full_out_path, 'w', encoding='utf-8') as f:
    f.write(html_doc)
  pages_generated.append(canonical_url)

print("Starting full site generation...")

# Helper for Breadcrumbs HTML
def make_breadcrumbs(items):
  lis = ""
  for i, (name, link) in enumerate(items):
    if i == len(items) - 1:
      lis += f'<li class="breadcrumb-item active" aria-current="page">{html.escape(name)}</li>'
    else:
      lis += f'<li class="breadcrumb-item"><a href="{link}">{html.escape(name)}</a></li>'
  return f"""
  <nav class="breadcrumb-nav" aria-label="Breadcrumb">
    <div class="container">
      <ol class="breadcrumb-list">
        {lis}
      </ol>
    </div>
  </nav>
  """

# Helper for FAQ Component
def make_faq_section(faqs):
  items = ""
  for q, a in faqs:
    items += f"""
    <div class="faq-item">
      <button class="faq-question">{html.escape(q)}</button>
      <div class="faq-answer">
        <p>{a}</p>
      </div>
    </div>
    """
  return f"""
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="badge">Frequently Asked Questions</span>
        <h2>Answers to Your Nadi Astrology Questions</h2>
      </div>
      <div class="faq-list">
        {items}
      </div>
    </div>
  </section>
  """

# ---------------------------------------------------------
# 1. HOME PAGE (index.html)
# ---------------------------------------------------------
home_body = f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-content">
      <span class="badge">Authentic Vaitheeswaran Koil Tradition</span>
      <h1>Agastya Nadi Jyotish – Sacred Palm Leaf Reading Online</h1>
      <p>Discover your destiny recorded thousands of years ago by Maharishi Agastya. Authentic Nadi astrology readings delivered online via video call or in-person at Vaitheeswaran Koil.</p>
      <div class="hero-actions">
        <a href="/book-consultation/" class="btn btn-primary">Book Consultation</a>
        <a href="/nadi-jyotish-online/" class="btn btn-outline">Explore Online Reading</a>
      </div>
      <div class="hero-features">
        <div class="hero-feature-item">✓ Unique Thumb Impression Search</div>
        <div class="hero-feature-item">✓ Ancient Tamil Manuscript Decoding</div>
        <div class="hero-feature-item">✓ 100% Confidential Consultation</div>
        <div class="hero-feature-item">✓ Live Audio & Video Call Options</div>
      </div>
    </div>
    <div class="hero-card">
      <h3 style="margin-top:0;">Quick Consultation Request</h3>
      <p style="font-size:0.9rem; color:var(--color-text-muted);">Submit your thumb impression and details to locate your sacred palm leaf manuscript.</p>
      <form id="hero-quick-form" action="/book-consultation/" method="GET">
        <div class="form-group">
          <label class="form-label" for="quick-name">Your Full Name</label>
          <input type="text" id="quick-name" name="name" class="form-control" placeholder="e.g. Ramesh Kumar" required>
        </div>
        <div class="form-group">
          <label class="form-label" for="quick-phone">WhatsApp Number</label>
          <input type="tel" id="quick-phone" name="phone" class="form-control" placeholder="+91 98765 43210" required>
        </div>
        <button type="submit" class="btn btn-secondary" style="width:100%;">Start Leaf Identification</button>
      </form>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Spiritual Legacy</span>
      <h2>What is Agastya Nadi Jyotish?</h2>
      <p>Agastya Nadi Jyotish is an ancient system of astrology preserved on dried palm leaves (Olai Chuvadi) written by Maharishi Agastya in Vaitheeswaran Koil, Tamil Nadu.</p>
    </div>
    
    <div class="grid-3">
      <div class="card">
        <div class="card-icon">📜</div>
        <h3 class="card-title">Ancient Tamil Manuscripts</h3>
        <p class="card-text">Written in poetic ancient Tamil, the manuscripts contain detailed insights into past karmas, present obstacles, and future destiny predictions.</p>
      </div>
      <div class="card">
        <div class="card-icon">👍</div>
        <h3 class="card-title">Thumb Impression Matching</h3>
        <p class="card-text">Every human thumb impression is categorized into 108 micro-patterns. Your right (male) or left (female) thumb impression locates your bundle.</p>
      </div>
      <div class="card">
        <div class="card-icon">🌐</div>
        <h3 class="card-title">Global Online Consultation</h3>
        <p class="card-text">Connect directly from Mumbai, Delhi, Pune, Bangalore, Hyderabad, or overseas. High-definition video call with real-time translation.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-header">
      <span class="badge">Process Overview</span>
      <h2>How Your Nadi Reading Unfolds</h2>
    </div>
    <div class="grid-4">
      <div class="card">
        <div style="font-size:2rem; font-weight:700; color:var(--color-secondary);">01</div>
        <h4>Submit Thumb Print</h4>
        <p style="font-size:0.9rem; color:var(--color-text-muted);">Send a clear photo of your thumb impression via WhatsApp or online form.</p>
      </div>
      <div class="card">
        <div style="font-size:2rem; font-weight:700; color:var(--color-secondary);">02</div>
        <h4>Bundle Search</h4>
        <p style="font-size:0.9rem; color:var(--color-text-muted);">Our reader searches through thousands of palm leaf bundles in Vaitheeswaran Koil.</p>
      </div>
      <div class="card">
        <div style="font-size:2rem; font-weight:700; color:var(--color-secondary);">03</div>
        <h4>Leaf Verification</h4>
        <p style="font-size:0.9rem; color:var(--color-text-muted);">Yes/No verification questions confirm your parents' names, birth details, and key facts.</p>
      </div>
      <div class="card">
        <div style="font-size:2rem; font-weight:700; color:var(--color-secondary);">04</div>
        <h4>Full Audio Reading</h4>
        <p style="font-size:0.9rem; color:var(--color-text-muted);">Complete decoding of Kandams (chapters) with audio recording and translation.</p>
      </div>
    </div>
  </div>
</section>

{make_faq_section([
  ("What is Agastya Nadi Jyotish?", "Agastya Nadi Jyotish (also written as Agasthiya Nadi Jyothisham) is an ancient predictive science authored by Sage Agastya. The predictions are inscribed on palm leaves stored predominantly at Vaitheeswaran Koil in Tamil Nadu."),
  ("How does online Nadi reading work without traveling to Tamil Nadu?", "You send your thumb impression digitally. Our Nadi readers in Vaitheeswaran Koil search the physical leaf bundles. Once matched, the reading and verification session is conducted live via video call."),
  ("Is Nadi Jyotish genuine and accurate?", "Authentic Nadi readings are remarkably precise when the exact leaf manuscript written for your soul is located. Verification questions confirm identity before any predictions are read."),
  ("What information is required for leaf search?", "Only your thumb impression (Right thumb for males, Left thumb for females). Your exact birth time or horoscope is not mandatory, as the leaf reveals your birth details."),
  ("What are Kandams in Nadi astrology?", "Kandams are specialized chapters covering different life aspects such as General Future (Kandam 1), Education & Wealth (Kandam 2), Marriage (Kandam 7), Profession (Kandam 10), and Remedial Measures (Kandams 13 & 14).")
])}
"""

home_json_ld = json.dumps({
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": f"{BASE_URL}/#website",
      "url": BASE_URL,
      "name": "Agastya Nadi Jyotish",
      "description": "Authentic Agastya Nadi Astrology reading center and Vaitheeswaran Koil travel guide."
    },
    {
      "@type": "ProfessionalService",
      "@id": f"{BASE_URL}/#organization",
      "name": "Agastya Nadi Jyotish Center",
      "url": BASE_URL,
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "[REPLACE: Sannathi Street]",
        "addressLocality": "Vaitheeswaran Koil",
        "addressRegion": "Tamil Nadu",
        "postalCode": "609117",
        "addressCountry": "IN"
      },
      "telephone": "[REPLACE: +91 98765 43210]"
    }
  ]
})

render_page("/", "Agastya Nadi Jyotish | Online Nadi Astrology Reading Vaitheeswaran Koil", "Authentic Agastya Nadi Jyotish palm-leaf readings online & at Vaitheeswaran Koil. Discover your past karma, future predictions, and remedial guidance today.", home_body, home_json_ld, nav_active="home")

# ---------------------------------------------------------
# 2. PILLAR & SERVICE PAGES
# ---------------------------------------------------------

# Agastya Nadi Astrology Pillar
agastya_body = f"""
{make_breadcrumbs([("Home", "/"), ("Agastya Nadi Astrology", "/agastya-nadi-astrology/")])}
<section class="section">
  <div class="container">
    <h1>Agastya Nadi Astrology: Sacred Wisdom of Maharishi Agastya</h1>
    <p class="badge">Comprehensive Guide & Historical Legacy</p>
    <p style="font-size:1.15rem; line-height:1.8;"><strong>Short Answer:</strong> Agastya Nadi Astrology (also spelled Agasthiya Nadi Jyothisham) is a thousands-year-old Tamil palm-leaf reading system. Preserved by generations of traditional astrologers in Vaitheeswaran Koil, these sacred manuscripts record the soul journey, karmic patterns, and detailed future predictions for individuals predestined to seek them.</p>
    
    <h2>Origin and Spiritual Roots of Agastya Nadi</h2>
    <p>Maharishi Agastya, one of the primary Saptarishis and a pillar of Siddha medicine and Tamil literature, composed these prophecies through divine intuition (Divya Drishti). The predictions were written in poetic ancient Tamil on specially prepared palm leaves (Olai Chuvadi) and stored in royal archives and temple libraries, particularly at the Vaidyanatha Swamy Temple in Vaitheeswaran Koil.</p>

    <h2>Spelling Variants: Agastya vs Agasthya Nadi Jyotish</h2>
    <p>Across India and internationally, seekers search for this sacred art using various phonetic spellings including <em>agastya nadi astrology</em>, <em>agasthya nadi jyothisham</em>, <em>agasthiya nadi</em>, and <em>nadi agastya astrologer</em>. Regardless of regional transliteration, all refer to the authentic palm-leaf readings originating from Sage Agastya's ancient Tamil heritage.</p>

    <h2>The 14 Key Chapters (Kandams)</h2>
    <p>An Agastya Nadi reading is organized into structured chapters known as Kandams:</p>
    <ul style="line-height:1.8;">
      <li><strong>General Kandam (Chapter 1):</strong> Complete overview of life span, major events, parents' details, and general predictions.</li>
      <li><strong>Education & Wealth (Chapter 2):</strong> Financial prospects, family life, eye sight, and speech.</li>
      <li><strong>Brothers & Sisters (Chapter 3):</strong> Relationships with siblings and courage.</li>
      <li><strong>Mother, Assets & Vehicles (Chapter 4):</strong> Property acquisition, house ownership, and mother's well-being.</li>
      <li><strong>Children & Progeny (Chapter 5):</strong> Birth of children, reasons for delay, and lineage remedies.</li>
      <li><strong>Health & Enemies (Chapter 6):</strong> Diseases, court cases, debts, and litigation.</li>
      <li><strong>Matrimony & Marriage (Chapter 7):</strong> Timing of marriage, spouse profile, and marital harmony.</li>
      <li><strong>Longevity & Danger (Chapter 8):</strong> Lifespan, accidents, and critical planetary periods.</li>
      <li><strong>Father & Fortune (Chapter 9):</strong> Ancestral property, spiritual inclinations, and father's lifespan.</li>
      <li><strong>Career & Business (Chapter 10):</strong> Job changes, business success, promotions, and status.</li>
      <li><strong>Gain & Second Marriage (Chapter 11):</strong> Business profits and secondary unions if applicable.</li>
      <li><strong>Expenditure & Foreign Travel (Chapter 12):</strong> Foreign trips, next birth, and spiritual salvation (Moksha).</li>
      <li><strong>Shanthi Kandam (Chapter 13):</strong> Past-life sins (Karma) and prescribed temple remedies.</li>
      <li><strong>Deeksha Kandam (Chapter 14):</strong> Sacred mantras and protective talismanic guidance.</li>
    </ul>

    <div style="margin-top:2rem; padding:1.5rem; background:var(--color-bg-alt); border-radius:var(--radius-md);">
      <h3>Ready to locate your personal leaf bundle?</h3>
      <p>Submit your thumb impression today for an authentic live online consultation with our Vaitheeswaran Koil experts.</p>
      <a href="/book-consultation/" class="btn btn-primary">Book Consultation Now</a>
    </div>
  </div>
</section>
"""
render_page("/agastya-nadi-astrology/", "Agastya Nadi Astrology | Sacred Palm Leaf Reading Explained", "Comprehensive guide to Agastya Nadi Astrology. Learn how Maharishi Agastya's palm leaves record your past karma, 14 Kandams, and future destiny.", agastya_body, nav_active="about")

# Agastya Nadi Jyothisham (South Indian target)
jyothisham_body = f"""
{make_breadcrumbs([("Home", "/"), ("Agastya Nadi Jyothisham", "/agastya-nadi-jyothisham/")])}
<section class="section">
  <div class="container">
    <h1>Agastya Nadi Jyothisham – Authentic Vaitheeswaran Koil Reading</h1>
    <p class="badge">Tamil & Telugu Audience Explainer</p>
    <p style="font-size:1.15rem; line-height:1.8;"><strong>Overview:</strong> Agastya Nadi Jyothisham (also termed Agasthya Jyothisham or Agasthiya Nadi) represents the ancient South Indian tradition of leaf reading. Based in Vaitheeswaran Koil, our hereditary readers decode ancient Tamil inscriptions for devotees across Tamil Nadu, Andhra Pradesh, Telangana, Karnataka, and globally.</p>
    
    <h2>Key Distinctions of Agastya Nadi Jyothisham</h2>
    <p>Unlike standard horoscopes calculated from birth time, Agastya Nadi Jyothisham relies on pre-recorded palm leaf manuscripts. Sage Agastya inscribed these poetic lines thousands of years ago in Tamil. The leaf search starts purely with your thumb impression.</p>
    
    <div class="grid-2" style="margin-top:2rem;">
      <div class="card">
        <h3>Male Seekers</h3>
        <p>Right thumb impression required. The thumb lines are classified into 108 categories (e.g. Chakram, Sankhu, Ring, Crown patterns).</p>
      </div>
      <div class="card">
        <h3>Female Seekers</h3>
        <p>Left thumb impression required. The unique whorls lead the astrologer to specific leaf bundles stored in Vaitheeswaran Koil.</p>
      </div>
    </div>
    
    <h2 style="margin-top:2.5rem;">Why Seekers Choose Online Agastya Jyothisham</h2>
    <p>Devotees who cannot travel directly to Mayiladuthurai district in Tamil Nadu can now avail authentic online video consultations. Audio recordings of the Tamil chants along with line-by-line English, Hindi, or Telugu translations are provided immediately after the session.</p>
    
    <div style="margin-top:2rem; text-align:center;">
      <a href="/nadi-jyotish-online/" class="btn btn-secondary">Explore Online Reading Services</a>
    </div>
  </div>
</section>
"""
render_page("/agastya-nadi-jyothisham/", "Agastya Nadi Jyothisham | Vaitheeswaran Koil Leaf Astrology", "Explore Agastya Nadi Jyothisham (Agasthya Nadi). Authentic palm leaf readings from Vaitheeswaran Koil with complete English & Telugu translations.", jyothisham_body, nav_active="about")

# Generic Nadi Jyotish Page
nadi_generic_body = f"""
{make_breadcrumbs([("Home", "/"), ("Nadi Jyotish", "/nadi-jyotish/")])}
<section class="section">
  <div class="container">
    <h1>Nadi Jyotish: The Ancient Science of Palm Leaf Prediction</h1>
    <p class="badge">Core Explainer & Astrological Comparison</p>
    <p style="font-size:1.15rem; line-height:1.8;"><strong>Nadi Jyotish</strong> (Nadi Astrology) is a form of Hindu astrology practiced in Tamil Nadu, Kerala, and adjacent regions in India. It is based on the belief that the past, present, and future lives of all human beings were foreseen by ancient Siddhas and Maharishis.</p>
    
    <h2>Different Nadi Schools: Agastya, Bhrigu, and Kausika</h2>
    <p>While Sage Agastya is the most famous author of Nadi manuscripts, other revered sages also authored specialized Nadi collections:</p>
    <ul>
      <li><strong>Agastya Nadi:</strong> The most widely sought and comprehensive Nadi manuscript, centered around Vaitheeswaran Koil.</li>
      <li><strong>Bhrigu Nadi:</strong> Popular in Northern India, focused heavily on horoscopic chart configurations.</li>
      <li><strong>Kausika & Bohar Nadi:</strong> Specialized medical, remedy, and alchemical predictions.</li>
    </ul>

    <h2>How Nadi Astrology Differs from Vedic Astrology</h2>
    <div class="table-responsive">
      <table class="table">
        <thead>
          <tr>
            <th>Feature</th>
            <th>Nadi Jyotish</th>
            <th>Standard Vedic Astrology</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Primary Input</strong></td>
            <td>Thumb Impression (Right/Left)</td>
            <td>Exact Date, Time & Place of Birth</td>
          </tr>
          <tr>
            <td><strong>Source Material</strong></td>
            <td>Ancient Palm Leaf Manuscripts (Olai Chuvadi)</td>
            <td>Ephemeris calculations (Panchangam)</td>
          </tr>
          <tr>
            <td><strong>Verification</strong></td>
            <td>Matching identity via leaf Q&A</td>
            <td>Rasi & Navamsa Chart drawing</td>
          </tr>
          <tr>
            <td><strong>Remedies</strong></td>
            <td>Specific Temple visits & Pariharas (Kandam 13)</td>
            <td>Gemstones, Mantras, Fasting</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
"""
render_page("/nadi-jyotish/", "Nadi Jyotish & Nadi Astrology | Ancient Palm Leaf Predictions", "Understand Nadi Jyotish (Nadi Astrology). Discover how thumb print categorization matches ancient palm leaf predictions written by Maharishis.", nadi_generic_body, nav_active="about")

# Online Consultation Money Page
online_body = f"""
{make_breadcrumbs([("Home", "/"), ("Online Nadi Reading", "/nadi-jyotish-online/")])}
<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Money Page & Direct Booking</span>
      <h1>Nadi Jyotish Online Consultation</h1>
      <p>Get your authentic Agastya Nadi palm leaf reading online from anywhere in the world. Live video call with expert translators based in Vaitheeswaran Koil.</p>
    </div>
    
    <div class="grid-2">
      <div>
        <h2>Why Opt for Online Nadi Reading?</h2>
        <p>You no longer need to travel to Vaitheeswaran Koil in Tamil Nadu to discover your palm leaf manuscript. Our online consultation process mirrors the exact traditional in-person procedure with total transparency.</p>
        <ul style="line-height:1.8;">
          <li><strong>Digital Impression Submission:</strong> High-resolution photo of your thumb impression via WhatsApp or online form.</li>
          <li><strong>Live Identification Session:</strong> Interactive video call where the astrologer reads verification index leaves.</li>
          <li><strong>Multilingual Translators:</strong> Live translation in English, Hindi, Telugu, Kannada, or Tamil.</li>
          <li><strong>Complete Audio Recording:</strong> Receive high-quality MP3 audio of your entire reading session.</li>
        </ul>
        <a href="/book-consultation/" class="btn btn-primary" style="margin-top:1rem;">Book Online Session Now</a>
      </div>
      
      <div class="card" style="background:var(--color-bg-alt);">
        <h3>Online Service Guarantee</h3>
        <p>We follow strict ethical standards for all online Nadi consultations:</p>
        <ul style="line-height:1.7; font-size:0.95rem;">
          <li>✓ No advance reading fee until your leaf bundle is located.</li>
          <li>✓ 100% privacy of your thumb impression & personal details.</li>
          <li>✓ Transparent pricing structure with no hidden fees.</li>
          <li>✓ Authentic Tamil palm leaf chanting directly from Vaitheeswaran Koil.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""
render_page("/nadi-jyotish-online/", "Nadi Jyotish Online | Authentic Palm Leaf Reading via Video Call", "Book Nadi Jyotish online video consultation directly from Vaitheeswaran Koil. Authentic Agastya palm leaf identification, audio recording & live translation.", online_body, nav_active="online")

# How Nadi Reading Works
works_body = f"""
{make_breadcrumbs([("Home", "/"), ("How Nadi Reading Works", "/how-nadi-reading-works/")])}
<section class="section">
  <div class="container">
    <h1>Step-by-Step Guide: How Agastya Nadi Reading Works</h1>
    <p class="badge">Transparent Process Breakdown</p>
    
    <div style="max-width:800px; margin:0 auto; line-height:1.8;">
      <h2>Step 1: Taking & Sending Your Thumb Impression</h2>
      <p>For males, the right-hand thumb impression is taken; for females, the left-hand thumb. You can press your thumb onto an ink pad and press it firmly on white paper, or take a clear high-resolution photograph under good lighting.</p>
      
      <h2>Step 2: Micro-Pattern Classification</h2>
      <p>Our experienced Nadi readers analyze the lines and whorls on your thumb. Thumb impressions are classified into 108 distinct categories such as Chakram (wheel), Shankhu (conch), Tower, or Loop configurations. This pattern narrows down the search to specific leaf bundles.</p>
      
      <h2>Step 3: Searching the Palm Leaf Bundles (Kattu)</h2>
      <p>Using your classification code, the astrologer retrieves matching bundles of palm leaves (Olai Chuvadi) stored in our Vaitheeswaran Koil repository. Each leaf in a bundle contains verses written in ancient poetic Tamil script.</p>
      
      <h2>Step 4: Live Verification Q&A</h2>
      <p>During the live session, the reader reads statement lines from potential leaves. You answer only with 'YES' or 'NO'. For instance: <em>"Your father's name begins with a vowel sound?"</em> or <em>"You have two elder brothers?"</em> When a leaf gets 100% 'YES' answers to all personal details (including your exact name, parents' names, and current career), your true manuscript is confirmed!</p>
      
      <h2>Step 5: Decoding & Audio Recording</h2>
      <p>Once identified, the reader recites the original poetic Tamil verses from your leaf, decodes their meaning, and provides a clear sentence-by-sentence translation in your preferred language. You receive the full audio recording for future reference.</p>
    </div>
  </div>
</section>
"""
render_page("/how-nadi-reading-works/", "How Agastya Nadi Reading Works | Step-by-Step Process", "Learn how Agastya Nadi leaf reading works: thumb impression classification, bundle search in Vaitheeswaran Koil, verification Q&A, and full decoding.", works_body, nav_active="about")

# Book Consultation Page
book_body = f"""
{make_breadcrumbs([("Home", "/"), ("Book Consultation", "/book-consultation/")])}
<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Book Your Session</span>
      <h1>Schedule Your Agastya Nadi Consultation</h1>
      <p>Fill out the form below to initiate your palm leaf identification search. Our team at Vaitheeswaran Koil will contact you via WhatsApp or Email.</p>
    </div>
    
    <form class="booking-form" id="booking-form" action="/book-consultation/thank-you/" method="GET">
      <div class="form-group">
        <label class="form-label" for="full-name">Full Name *</label>
        <input type="text" id="full-name" name="full_name" class="form-control" required placeholder="Enter your full name">
      </div>
      
      <div class="grid-2">
        <div class="form-group">
          <label class="form-label" for="phone-number">WhatsApp / Phone Number *</label>
          <input type="tel" id="phone-number" name="phone" class="form-control" required placeholder="+91 98765 43210">
        </div>
        <div class="form-group">
          <label class="form-label" for="email-address">Email Address *</label>
          <input type="email" id="email-address" name="email" class="form-control" required placeholder="your.email@example.com">
        </div>
      </div>
      
      <div class="grid-2">
        <div class="form-group">
          <label class="form-label" for="pref-language">Preferred Language</label>
          <select id="pref-language" name="language" class="form-control">
            <option value="English">English</option>
            <option value="Hindi">Hindi (हिन्दी)</option>
            <option value="Tamil">Tamil (தமிழ்)</option>
            <option value="Telugu">Telugu (తెలుగు)</option>
            <option value="Kannada">Kannada (கன்னடம்)</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label" for="consult-mode">Consultation Mode</label>
          <select id="consult-mode" name="mode" class="form-control">
            <option value="Online Video Call">Online Video Call (Zoom/WhatsApp)</option>
            <option value="In-Person Vaitheeswaran Koil">In-Person at Vaitheeswaran Koil</option>
          </select>
        </div>
      </div>
      
      <div class="form-group">
        <label class="form-label" for="preferred-date">Preferred Date & Time</label>
        <input type="date" id="preferred-date" name="date" class="form-control">
      </div>
      
      <div class="form-group form-checkbox">
        <input type="checkbox" id="consent-check" name="consent" required>
        <label for="consent-check">I consent to sharing my thumb impression and contact details for the sole purpose of Nadi leaf identification and consultation. (Read our <a href="/privacy-policy/">Privacy Policy</a>)</label>
      </div>
      
      <button type="submit" class="btn btn-primary" style="width:100%; margin-top:1rem;">Submit Consultation Request</button>
    </form>
  </div>
</section>
"""
render_page("/book-consultation/", "Book Agastya Nadi Reading | Vaitheeswaran Koil Consultation", "Book an authentic Agastya Nadi Jyotish reading online or in-person. Submit your details and thumb impression to locate your palm leaf bundle.", book_body, nav_active="online")

# Payments & Transparent Pricing
payments_body = f"""
{make_breadcrumbs([("Home", "/"), ("Payments & Pricing", "/payments/")])}
<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Transparent Pricing</span>
      <h1>Nadi Jyotish Reading Fees & Payment Info</h1>
      <p>We maintain 100% price transparency. Below is our standard fee schedule for various Kandams (chapters) and online video consultation services.</p>
    </div>
    
    <div class="table-responsive" style="max-width:850px; margin:0 auto;">
      <table class="table">
        <thead>
          <tr>
            <th>Consultation Package</th>
            <th>Chapters Included</th>
            <th>Fee (INR)</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>General Reading (Kandam 1)</strong></td>
            <td>General life overview, parents, career, longevity overview</td>
            <td>₹[REPLACE: 1,500]</td>
            <td>45 mins</td>
          </tr>
          <tr>
            <td><strong>Kandam 1 + Shanthi (13) & Deeksha (14)</strong></td>
            <td>General future + Past life remedies & Protective mantras</td>
            <td>₹[REPLACE: 3,500]</td>
            <td>90 mins</td>
          </tr>
          <tr>
            <td><strong>Comprehensive Full Package</strong></td>
            <td>All 14 Kandams (Career, Marriage, Wealth, Health, Children)</td>
            <td>₹[REPLACE: 7,500]</td>
            <td>2-3 Hours</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="max-width:850px; margin:2.5rem auto 0 auto; text-align:center;">
      <h2>Accepted Payment Methods</h2>
      <p>We accept UPI (GPay, PhonePe, Paytm), Net Banking, International Credit/Debit Cards, and PayPal.</p>
      <div style="margin-top:1.5rem; display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
        <a href="/book-consultation/" class="btn btn-primary">Book Consultation First</a>
        <a href="https://wa.me/919876543210" class="btn btn-whatsapp" target="_blank" rel="noopener">Pay via WhatsApp Link</a>
      </div>
    </div>
  </div>
</section>
"""
render_page("/payments/", "Nadi Jyotish Pricing & Fees | Agastya Nadi Payment Info", "Transparent pricing for Agastya Nadi Jyotish readings. Detailed fee structure for Kandam 1, Shanthi remedies, and full 14-chapter consultations.", payments_body, nav_active="online")

# Gallery Page
gallery_body = f"""
{make_breadcrumbs([("Home", "/"), ("Gallery", "/gallery/")])}
<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Real Photos</span>
      <h1>Our Center, Manuscripts & Consultation Gallery</h1>
      <p>Explore real images of our Vaitheeswaran Koil Nadi center, ancient palm-leaf manuscripts (Olai Chuvadi), and consultation atmosphere.</p>
    </div>
    
    <div class="grid-3">
      <div class="card" style="padding:1rem;">
        <img src="/assets/images/gallery-palm-leaves.jpg" alt="Ancient Agastya Nadi palm leaf manuscript bundle in Vaitheeswaran Koil" width="600" height="400" loading="lazy" style="border-radius:var(--radius-sm); margin-bottom:1rem;">
        <h3 style="font-size:1.1rem; margin-bottom:0.4rem;">Ancient Palm Leaf Bundles</h3>
        <p style="font-size:0.875rem; color:var(--color-text-muted);">Preserved ancient Tamil manuscripts inscribed by Maharishi Agastya.</p>
      </div>
      <div class="card" style="padding:1rem;">
        <img src="/assets/images/gallery-center.jpg" alt="Agastya Nadi Jyotish consultation room in Vaitheeswaran Koil" width="600" height="400" loading="lazy" style="border-radius:var(--radius-sm); margin-bottom:1rem;">
        <h3 style="font-size:1.1rem; margin-bottom:0.4rem;">Vaitheeswaran Koil Center</h3>
        <p style="font-size:0.875rem; color:var(--color-text-muted);">Traditional & serene atmosphere for in-person reading sessions.</p>
      </div>
      <div class="card" style="padding:1rem;">
        <img src="/assets/images/gallery-astrologer.jpg" alt="Hereditary Nadi astrologer reading palm leaf text" width="600" height="400" loading="lazy" style="border-radius:var(--radius-sm); margin-bottom:1rem;">
        <h3 style="font-size:1.1rem; margin-bottom:0.4rem;">Hereditary Nadi Readers</h3>
        <p style="font-size:0.875rem; color:var(--color-text-muted);">Decades of experience in ancient Tamil script decoding.</p>
      </div>
    </div>
  </div>
</section>
"""
render_page("/gallery/", "Agastya Nadi Gallery | Real Palm Leaf Photos & Center Images", "Browse real photos of authentic Agastya Nadi palm leaves, our Vaitheeswaran Koil reading center, and hereditary astrologers.", gallery_body, nav_active="gallery")

# ---------------------------------------------------------
# 3. CITY PAGES (Pune, Delhi, Mumbai, Bangalore, Hyderabad)
# ---------------------------------------------------------

cities = [
  ("agastya-nadi-jyotish-pune", "Pune", "agastya nadi jyotish pune", "Seekers in Pune can now access authentic Vaitheeswaran Koil Agastya Nadi Jyotish through our dedicated online consultation platform. Connect with expert Tamil readers directly from Kothrud, Baner, Viman Nagar, or Wakad."),
  ("nadi-jyotish-delhi", "Delhi NCR", "nadi jyotish delhi", "Residents of Delhi, Gurgaon, and Noida can receive genuine Agastya Nadi astrology predictions online directly from Vaitheeswaran Koil without traveling to South India."),
  ("nadi-jyotish-mumbai", "Mumbai", "nadi jyotish mumbai", "Get accurate Nadi Jyotish online readings in Mumbai (Andheri, Dadar, Thane, Navi Mumbai). Discover your ancient palm leaf predictions via live video call with Hindi & English translation."),
  ("nadi-jyotish-bangalore", "Bangalore", "nadi jyotish bangalore", "Serving Bangalore seekers in Indiranagar, Koramangala, Whitefield, and Jayanagar with authentic Vaitheeswaran Koil Agastya Nadi palm leaf consultations online."),
  ("nadi-jyotish-hyderabad", "Hyderabad", "nadi jyotish hyderabad", "Discover your pre-written fate with online Nadi Jyotish in Hyderabad (Banjara Hills, Jubilee Hills, Gachibowli). Live Telugu and English translation available.")
]

for slug, city_name, kw, intro in cities:
  city_body = f"""
  {make_breadcrumbs([("Home", "/"), (f"Nadi Jyotish {city_name}", f"/{slug}/")])}
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge">Online Service for {city_name}</span>
        <h1>Agastya Nadi Jyotish in {city_name}</h1>
        <p>{intro}</p>
      </div>
      
      <div class="grid-2">
        <div>
          <h2>How Seekers in {city_name} Access Authentic Nadi Reading</h2>
          <p>While our central repository of sacred palm leaves (Olai Chuvadi) is physically situated at Vaitheeswaran Koil in Tamil Nadu, you do not need to travel down south. We deliver 100% authentic online video consultations tailored for clients residing in {city_name}.</p>
          <ul style="line-height:1.8;">
            <li><strong>Step 1:</strong> Take a clear photo of your thumb impression (Right for male, Left for female) at home in {city_name}.</li>
            <li><strong>Step 2:</strong> Send it via WhatsApp or submit online.</li>
            <li><strong>Step 3:</strong> Join a live video call for leaf identification and verification.</li>
            <li><strong>Step 4:</strong> Receive your complete decoded reading in English or Hindi with audio recording.</li>
          </ul>
          <a href="/book-consultation/" class="btn btn-primary" style="margin-top:1rem;">Book {city_name} Consultation</a>
        </div>
        
        <div class="card" style="background:var(--color-bg-alt);">
          <h3>City FAQ: {city_name}</h3>
          <p><strong>Q: Do you have a physical branch office in {city_name}?</strong></p>
          <p style="font-size:0.9rem; color:var(--color-text-muted);">A: To maintain absolute authenticity, all physical leaf bundles are preserved exclusively at our Vaitheeswaran Koil center. We serve {city_name} residents digitally via live video call, avoiding middle-man inaccuracies.</p>
          
          <p style="margin-top:1rem;"><strong>Q: In which languages is the reading provided for {city_name} clients?</strong></p>
          <p style="font-size:0.9rem; color:var(--color-text-muted);">A: Readings are translated live into English, Hindi, Tamil, or Telugu based on your preference.</p>
        </div>
      </div>
    </div>
  </section>
  """
  render_page(f"/{slug}/", f"Agastya Nadi Jyotish in {city_name} | Online Palm Leaf Reading", f"Authentic Agastya Nadi Jyotish for seekers in {city_name}. Get live video consultation directly from Vaitheeswaran Koil with complete audio recording.", city_body, nav_active="online")

# ---------------------------------------------------------
# 4. VAITHEESWARAN KOIL TRAVEL GUIDE
# ---------------------------------------------------------

# Vaitheeswaran Koil Hub Page
koil_hub_body = f"""
{make_breadcrumbs([("Home", "/"), ("Vaitheeswaran Koil", "/vaitheeswaran-koil/")])}
<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Pilgrimage & Heritage Hub</span>
      <h1>Vaitheeswaran Koil: Sacred Land of Healing & Nadi Astrology</h1>
      <p>Vaitheeswaran Koil is a famous temple town located in Mayiladuthurai district, Tamil Nadu. Renowned as the cure-center of Lord Shiva (Vaidyanatha Swamy) and the Angaraka (Mars) Navagraha Sthalam, it is also the world center for Agastya Nadi Jyotish.</p>
    </div>
    
    <div class="grid-3">
      <div class="card">
        <h3>Vaidyanatha Swamy Temple</h3>
        <p>The primary temple dedicated to Lord Shiva as the Divine Healer and Goddess Thaiyalnayaki. Features the sacred Siddhamirtham tank.</p>
        <a href="/vaitheeswaran-koil/vaidyanatha-swamy-temple/" class="btn btn-outline btn-sm" style="margin-top:1rem;">Explore Temple Details</a>
      </div>
      <div class="card">
        <h3>Temples Nearby</h3>
        <p>Discover famous Shiva, Navagraha, and Murugan temples within 10 to 40 km of Vaitheeswaran Koil.</p>
        <a href="/vaitheeswaran-koil/temples-nearby/" class="btn btn-outline btn-sm" style="margin-top:1rem;">View Nearby Temples</a>
      </div>
      <div class="card">
        <h3>Navagraha Route Map</h3>
        <p>Complete 1-day Navagraha temple tour itinerary starting from Kumbakonam and covering all 9 planetary temples.</p>
        <a href="/vaitheeswaran-koil/navagraha-temples-route-from-kumbakonam/" class="btn btn-outline btn-sm" style="margin-top:1rem;">View Navagraha Route</a>
      </div>
    </div>
    
    <div style="margin-top:3rem;">
      <h2>Key Information for Visitors</h2>
      <div class="grid-2">
        <div>
          <h4>Location & Accessibility</h4>
          <p>Vaitheeswaran Koil is located on the Chennai-Thanjavur highway (NH-45A), approximately 240 km from Chennai, 14 km from Mayiladuthurai, and 50 km from Kumbakonam.</p>
        </div>
        <div>
          <h4>Nearest Transit Points</h4>
          <p><strong>Railway Station:</strong> Vaitheeswaran Koil (VDL) station.<br><strong>Airport:</strong> Tiruchirappalli (TRZ) Airport ~135 km.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""
render_page("/vaitheeswaran-koil/", "Vaitheeswaran Koil Guide | Temples, Timings & Nadi Astrology", "Complete guide to Vaitheeswaran Koil temple, Angaraka Navagraha sthalam, nearby temples, travel itinerary, and Agastya Nadi reading centers.", koil_hub_body, nav_active="koil")

# Temples Nearby
nearby_body = f"""
{make_breadcrumbs([("Home", "/"), ("Vaitheeswaran Koil", "/vaitheeswaran-koil/"), ("Temples Nearby", "/vaitheeswaran-koil/temples-nearby/")])}
<section class="section">
  <div class="container">
    <h1>Famous Temples Near Vaitheeswaran Koil</h1>
    <p class="badge">Pilgrimage Guide</p>
    <p>Explore prominent ancient temples located within a short drive from Vaitheeswaran Koil in Mayiladuthurai, Sirkazhi, and Chidambaram regions.</p>
    
    <div class="grid-3" style="margin-top:2rem;">
      <div class="card">
        <h3>Chidambaram Nataraja Temple</h3>
        <p><strong>Distance:</strong> ~26 km (35 mins drive)<br>Famous cosmic dancer Shiva temple representing the Space (Akasha) element.</p>
      </div>
      <div class="card">
        <h3>Sirkazhi Bhramapureeswarar Temple</h3>
        <p><strong>Distance:</strong> ~6 km (10 mins drive)<br>Birthplace of Saint Thirugnana Sambandar with Thoniappar shrine.</p>
      </div>
      <div class="card">
        <h3>Thirunageswaram Rahu Temple</h3>
        <p><strong>Distance:</strong> ~45 km (1 hour drive)<br>Major Navagraha temple dedicated to Rahu Lord.</p>
      </div>
    </div>
  </div>
</section>
"""
render_page("/vaitheeswaran-koil/temples-nearby/", "Temples Near Vaitheeswaran Koil | Famous Pilgrimage Sites", "Discover famous temples near Vaitheeswaran Koil: Chidambaram Nataraja, Sirkazhi, Thirunageswaram, and Navagraha temples with distance and travel times.", nearby_body, nav_active="koil")

# Shiva Temples Nearby
shiva_body = f"""
{make_breadcrumbs([("Home", "/"), ("Vaitheeswaran Koil", "/vaitheeswaran-koil/"), ("Shiva Temples Nearby", "/vaitheeswaran-koil/shiva-temples-nearby/")])}
<section class="section">
  <div class="container">
    <h1>Shiva Temples Near Vaitheeswaran Koil</h1>
    <p class="badge">Paadal Petra Sthalangal</p>
    <p>The Mayiladuthurai-Kumbakonam belt houses the world's highest concentration of ancient Paadal Petra Shiva Sthalams praised by Nayanmars.</p>
    <ul>
      <li><strong>Vaidyanatha Swamy Temple:</strong> Located right at Vaitheeswaran Koil.</li>
      <li><strong>Mayuranathaswamy Temple (Mayiladuthurai):</strong> 14 km south of Vaitheeswaran Koil.</li>
      <li><strong>Amritaghateswarar Abhirami Temple (Thirukadaiyur):</strong> 30 km east, famous for 60th/80th marriage milestone prayers.</li>
    </ul>
  </div>
</section>
"""
render_page("/vaitheeswaran-koil/shiva-temples-nearby/", "Shiva Temples Near Vaitheeswaran Koil | Ancient Paadal Petra Sthalangal", "Explore sacred Shiva temples near Vaitheeswaran Koil including Thirukadaiyur, Mayiladuthurai Mayuranathar, and Sirkazhi Thoniappar temple.", shiva_body, nav_active="koil")

# Places to Visit
places_body = f"""
{make_breadcrumbs([("Home", "/"), ("Vaitheeswaran Koil", "/vaitheeswaran-koil/"), ("Places to Visit", "/vaitheeswaran-koil/places-to-visit/")])}
<section class="section">
  <div class="container">
    <h1>Tourist Places to Visit Near Vaitheeswaran Koil</h1>
    <p class="badge">Travel & Cultural Sightseeing</p>
    <p>Beyond temples, the coastal region around Vaitheeswaran Koil offers rich heritage, beaches, and nature sanctuaries.</p>
    <div class="grid-2" style="margin-top:1.5rem;">
      <div class="card">
        <h3>Poompuhar Beach & Heritage Museum</h3>
        <p><strong>Distance:</strong> ~22 km<br>Ancient Chola port city mentioned in Silappatikaram epic. Features coastal views and art gallery museum.</p>
      </div>
      <div class="card">
        <h3>Pichavaram Mangrove Forest</h3>
        <p><strong>Distance:</strong> ~40 km<br>Second largest mangrove forest in the world. Ideal for serene boat rides through green canopy canals.</p>
      </div>
    </div>
  </div>
</section>
"""
render_page("/vaitheeswaran-koil/places-to-visit/", "Places to Visit Near Vaitheeswaran Koil | Tourist Attractions", "Top places to visit near Vaitheeswaran Koil: Pichavaram mangrove forest, Poompuhar coastal beach, Chidambaram, and Tarangambadi fort.", places_body, nav_active="koil")

# Navagraha Route Map
navagraha_body = f"""
{make_breadcrumbs([("Home", "/"), ("Vaitheeswaran Koil", "/vaitheeswaran-koil/"), ("Navagraha Route", "/vaitheeswaran-koil/navagraha-temples-route-from-kumbakonam/")])}
<section class="section">
  <div class="container">
    <h1>Navagraha Temple Route Map from Kumbakonam</h1>
    <p class="badge">1-Day Pilgrimage Itinerary</p>
    <p>Complete guide to covering all 9 Navagraha planetary temples in Tamil Nadu efficiently in one or two days starting from Kumbakonam or Vaitheeswaran Koil.</p>
    
    <div class="table-responsive" style="margin-top:2rem;">
      <table class="table">
        <thead>
          <tr>
            <th>Stop #</th>
            <th>Planet (Graha)</th>
            <th>Temple Name</th>
            <th>Location</th>
            <th>Distance from Kumbakonam</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Sun (Suriyan)</td>
            <td>Suriyanar Koil</td>
            <td>Suriyanarkoil</td>
            <td>15 km</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Moon (Chandran)</td>
            <td>Kailasanathar Temple</td>
            <td>Thingalur</td>
            <td>33 km</td>
          </tr>
          <tr>
            <td>3</td>
            <td>Mars (Angaraka)</td>
            <td>Vaidyanatha Swamy Temple</td>
            <td>Vaitheeswaran Koil</td>
            <td>50 km</td>
          </tr>
          <tr>
            <td>4</td>
            <td>Mercury (Budhan)</td>
            <td>Swetharanyeswarar Temple</td>
            <td>Thiruvengadu</td>
            <td>60 km</td>
          </tr>
          <tr>
            <td>5</td>
            <td>Jupiter (Guru)</td>
            <td>Apatsahayesvarar Temple</td>
            <td>Alangudi</td>
            <td>18 km</td>
          </tr>
          <tr>
            <td>6</td>
            <td>Venus (Sukran)</td>
            <td>Agniswarar Temple</td>
            <td>Kanjanoor</td>
            <td>18 km</td>
          </tr>
          <tr>
            <td>7</td>
            <td>Saturn (Sani)</td>
            <td>Dharbaranyeswarar Temple</td>
            <td>Thirunallar</td>
            <td>95 km</td>
          </tr>
          <tr>
            <td>8</td>
            <td>Rahu</td>
            <td>Ranganathaswamy / Rahu Temple</td>
            <td>Thirunageswaram</td>
            <td>8 km</td>
          </tr>
          <tr>
            <td>9</td>
            <td>Kethu</td>
            <td>Naganathaswamy Temple</td>
            <td>Keezhperumpallam</td>
            <td>63 km</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
"""
render_page("/vaitheeswaran-koil/navagraha-temples-route-from-kumbakonam/", "Navagraha Temple Route Map from Kumbakonam | 9 Temple Circuit", "Detailed 1-day Navagraha temple route map from Kumbakonam & Vaitheeswaran Koil. Cover Sun, Moon, Mars, Rahu, Ketu, Jupiter, Saturn, Mercury, Venus.", navagraha_body, nav_active="koil")

# Vaidyanatha Swamy Temple Page
vaidyanatha_body = f"""
{make_breadcrumbs([("Home", "/"), ("Vaitheeswaran Koil", "/vaitheeswaran-koil/"), ("Vaidyanatha Swamy Temple", "/vaitheeswaran-koil/vaidyanatha-swamy-temple/")])}
<section class="section">
  <div class="container">
    <h1>Vaidyanatha Swamy Temple, Vaitheeswaran Koil</h1>
    <p class="badge">Angaraka (Mars) Navagraha Sthalam</p>
    
    <div style="line-height:1.8;">
      <p>The <strong>Vaidyanatha Swamy Temple</strong> at Vaitheeswaran Koil is one of the most revered Shiva temples in South India. Here, Lord Shiva is worshipped as Vaidyanathar (the Master Healer who cures all physical and mental ailments).</p>
      
      <h2>Key Features of the Temple</h2>
      <ul>
        <li><strong>Angaraka Shrine:</strong> Dedicated to Mars (Angarakan/Chevvai). Seekers perform Chevvai Dosham pariharam here.</li>
        <li><strong>Goddess Thaiyalnayaki:</strong> Appears carrying medicinal oil (Thailam) to heal devotees.</li>
        <li><strong>Siddhamirtham Tank:</strong> The sacred temple pond believed to possess holy curative waters.</li>
        <li><strong>Tiruchandur Tiruchendur & Jatayu Shrine:</strong> Where Lord Rama performed last rites for Jatayu.</li>
      </ul>
      
      <h2>Temple Timings</h2>
      <p><strong>Morning:</strong> 6:00 AM – 1:00 PM<br><strong>Evening:</strong> 4:00 PM – 9:00 PM</p>
    </div>
  </div>
</section>
"""
render_page("/vaitheeswaran-koil/vaidyanatha-swamy-temple/", "Vaidyanatha Swamy Temple Vaitheeswaran Koil | Timings & History", "Complete details of Vaidyanatha Swamy Temple in Vaitheeswaran Koil. Angaraka Chevvai dosham remedies, Siddhamirtham tank, and temple timings.", vaidyanatha_body, nav_active="koil")

# ---------------------------------------------------------
# 5. BLOG INDEX & 8 SEED POSTS
# ---------------------------------------------------------

blog_posts = [
  ("what-is-agastya-nadi-astrology-how-it-works", "What is Agastya Nadi Astrology and How Does It Work?", "Comprehensive overview of Sage Agastya's palm leaf manuscript system, thumb impression search, and verification Q&A."),
  ("nadi-jyotish-vs-vedic-astrology", "Nadi Jyotish vs Vedic Astrology: Key Differences Explained", "Comparing pre-written palm leaf predictions against horoscope chart calculations."),
  ("is-online-nadi-reading-genuine", "Is Online Nadi Reading Genuine? How to Spot Authentic Readers", "Safety guide for online consultations. Learn how verification Q&A protects you from fraudulent astrologers."),
  ("how-to-prepare-for-nadi-reading", "How to Prepare for Your Agastya Nadi Reading Session", "Essential tips to prepare for your online or in-person Nadi consultation for maximum accuracy."),
  ("thumb-impression-and-leaf-search-explained", "Thumb Impression Classification & Leaf Search Process", "Deep dive into 108 micro-patterns (Chakram, Conch) used to locate your palm leaf bundle."),
  ("vaitheeswaran-koil-one-day-itinerary", "Vaitheeswaran Koil One-Day Pilgrimage Itinerary", "Perfect 1-day itinerary combining temple darshan, Siddhamirtham bath, and Nadi reading."),
  ("navagraha-temples-tour-from-kumbakonam", "Navagraha Temples Tour from Kumbakonam & Vaitheeswaran Koil", "Optimal driving route map to visit all 9 Navagraha temples in 24 hours."),
  ("best-time-to-visit-vaitheeswaran-koil", "Best Time to Visit Vaitheeswaran Koil: Weather & Festivals", "Seasonal travel guidance, weather tips, and festival calendars for Vaitheeswaran Koil visitors.")
]

# Blog Index Page
blog_cards = ""
for slug, post_title, excerpt in blog_posts:
  blog_cards += f"""
  <div class="card" style="margin-bottom:1.5rem;">
    <span class="badge" style="width:fit-content;">Agastya Nadi Guide</span>
    <h3 style="margin-top:0.5rem;"><a href="/blog/{slug}/">{html.escape(post_title)}</a></h3>
    <p style="color:var(--color-text-muted); font-size:0.95rem;">{html.escape(excerpt)}</p>
    <div style="font-size:0.85rem; color:var(--color-text-muted); margin-top:1rem;">Published: September 2026 | By Agastya Nadi Editorial</div>
  </div>
  """

blog_index_body = f"""
{make_breadcrumbs([("Home", "/"), ("Blog", "/blog/")])}
<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Articles & Insights</span>
      <h1>Agastya Nadi Jyotish & Vaitheeswaran Koil Blog</h1>
      <p style="font-size:1.05rem; line-height:1.7;">Welcome to our dedicated knowledge center. Here you will find in-depth articles on Agastya Nadi astrology, authentic palm leaf reading techniques, spiritual pariharam remedies, and complete travel guide advice for Vaitheeswaran Koil and surrounding Navagraha temples.</p>
    </div>
    
    <div style="max-width:850px; margin:0 auto;">
      {blog_cards}
    </div>
  </div>
</section>
"""

blog_index_json_ld = json.dumps({
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Nadi Jyotish & Agastya Nadi Astrology Blog",
  "url": f"{BASE_URL}/blog/",
  "description": "Nadi Jyotish guidance, Vaitheeswaran Koil travel tips, and Agastya Nadi explainers."
})

render_page("/blog/", "Nadi Jyotish & Agastya Nadi Astrology Blog | Guidance & Travel", "Read in-depth articles on Agastya Nadi Jyotish, online palm leaf reading process, Vaitheeswaran Koil travel guides, and Navagraha temple routes.", blog_index_body, blog_index_json_ld, nav_active="blog")

# Generate individual blog post pages
for slug, post_title, excerpt in blog_posts:
  post_body = f"""
  {make_breadcrumbs([("Home", "/"), ("Blog", "/blog/"), (post_title, f"/blog/{slug}/")])}
  <section class="section">
    <div class="container" style="max-width:850px;">
      <span class="badge">Nadi Astrology Insights</span>
      <h1>{html.escape(post_title)}</h1>
      <p style="font-size:0.875rem; color:var(--color-text-muted); margin-bottom:2rem;">Updated: September 2026 | Category: Agastya Nadi Guidance | Reading Time: 5 mins</p>
      
      <div style="line-height:1.8; font-size:1.05rem;">
        <p><strong>Summary:</strong> {html.escape(excerpt)}</p>
        
        <h2>Understanding the Sacred Art</h2>
        <p>Agastya Nadi Jyotish is fundamentally rooted in the belief that your present life journey and past karmic actions are recorded on ancient Tamil palm leaves (Olai Chuvadi). Authored by Maharishi Agastya at Vaitheeswaran Koil, these leaves provide guidance when a seeker reaches a pivotal moment in life.</p>
        
        <h2>Key Aspects to Keep in Mind</h2>
        <p>Whether you choose an in-person session in Vaitheeswaran Koil or opt for a convenient online video consultation, ensure that your reader strictly adheres to the authentic verification process. A genuine Nadi reading never asks for your personal information upfront—the leaf itself discloses your birth details!</p>
        
        <div style="margin:2rem 0; padding:1.5rem; background:var(--color-bg-alt); border-radius:var(--radius-md);">
          <h3>Schedule Your Personal Nadi Reading</h3>
          <p>Discover what Sage Agastya wrote for your soul thousands of years ago.</p>
          <a href="/book-consultation/" class="btn btn-primary">Book Consultation Now</a>
        </div>
      </div>
    </div>
  </section>
  """
  
  post_json_ld = json.dumps({
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": post_title,
    "description": excerpt,
    "url": f"{BASE_URL}/blog/{slug}/",
    "datePublished": "2026-09-01",
    "author": {
      "@type": "Organization",
      "name": "Agastya Nadi Jyotish Editorial"
    }
  })
  
  render_page(f"/blog/{slug}/", f"{post_title} | Agastya Nadi Blog", excerpt[:150], post_body, post_json_ld, nav_active="blog")

# ---------------------------------------------------------
# 6. ABOUT, CONTACT, FAQ, LEGAL PAGES
# ---------------------------------------------------------

# About Page
about_body = f"""
{make_breadcrumbs([("Home", "/"), ("About Us", "/about/")])}
<section class="section">
  <div class="container">
    <h1>About Agastya Nadi Jyotish Center, Vaitheeswaran Koil</h1>
    <p class="badge">E-E-A-T & Spiritual Heritage</p>
    
    <div class="grid-2" style="margin-top:2rem;">
      <div>
        <h2>Our Lineage and Experience</h2>
        <p>Our center is located in the sacred town of Vaitheeswaran Koil, Tamil Nadu. For over four generations, our family of hereditary Nadi readers has preserved, maintained, and interpreted the ancient palm leaf manuscripts inscribed by Maharishi Agastya.</p>
        <p>Head Astrologer: <strong>[REPLACE: Guruji S. Agastya Nadi Reader]</strong> brings over 25+ years of dedicated practice in decoding ancient Tamil script and guiding devotees globally.</p>
      </div>
      <div class="card">
        <h3>Our Core Commitments</h3>
        <ul>
          <li>✓ 100% Authentic Leaf Bundles from Vaitheeswaran Koil</li>
          <li>✓ Transparent Pricing with No Hidden Pariharam Demands</li>
          <li>✓ Strict Confidentiality of Seekers' Birth & Thumb Data</li>
          <li>✓ Live Translation in English, Hindi, Tamil & Telugu</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""
render_page("/about/", "About Agastya Nadi Jyotish | Hereditary Readers Vaitheeswaran Koil", "Learn about our 4th-generation Agastya Nadi Astrology center in Vaitheeswaran Koil. Authentic hereditary readers and global online consultations.", about_body, nav_active="about")

# Contact Page
contact_body = f"""
{make_breadcrumbs([("Home", "/"), ("Contact Us", "/contact/")])}
<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Get in Touch</span>
      <h1>Contact Agastya Nadi Jyotish Center</h1>
      <p>Reach out for online reading inquiries, leaf search status, or travel guidance to Vaitheeswaran Koil.</p>
    </div>
    
    <div class="grid-2">
      <div class="card">
        <h3>Address & Phone</h3>
        <p><strong>Agastya Nadi Jyotish Center</strong><br>
        [REPLACE: Sannathi Street, Near Vaidyanatha Swamy Temple]<br>
        Vaitheeswaran Koil, Mayiladuthurai District<br>
        Tamil Nadu - 609117, India</p>
        <p style="margin-top:1rem;"><strong>Phone / WhatsApp:</strong> [REPLACE: +91 98765 43210]<br>
        <strong>Email:</strong> [REPLACE: info@agastyanadijyotish.com]</p>
      </div>
      
      <div class="card">
        <h3>Send a Message</h3>
        <form action="/contact/thank-you/" method="GET">
          <div class="form-group">
            <label class="form-label">Your Name</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label class="form-label">Email or Phone</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label class="form-label">Message</label>
            <textarea class="form-control" rows="4" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary" style="width:100%;">Send Message</button>
        </form>
      </div>
    </div>
  </div>
</section>
"""
render_page("/contact/", "Contact Agastya Nadi Jyotish | Vaitheeswaran Koil Center", "Contact Agastya Nadi Jyotish center in Vaitheeswaran Koil. Phone, WhatsApp, email, and address for online or in-person reading bookings.", contact_body, nav_active="contact")

# FAQ Page
faq_page_body = f"""
{make_breadcrumbs([("Home", "/"), ("FAQ", "/faq/")])}
<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="badge">Help & FAQ</span>
      <h1>Frequently Asked Questions</h1>
      <p>Find clear answers regarding Agastya Nadi leaf matching, online consultations, remedies, and temple visits.</p>
    </div>
    
    {make_faq_section([
      ("What happens if my palm leaf is not found?", "In rare cases, if a matching leaf bundle is not found during the search, we inform you honestly. We do not force false readings. You can re-attempt after a few months as new bundles are cataloged."),
      ("How long does an online Nadi reading session take?", "A typical session takes between 45 minutes to 2 hours depending on the number of Kandams (chapters) you choose to decode."),
      ("Are temple remedies (Pariharams) mandatory?", "Pariharams mentioned in Kandam 13 are recommended spiritual remedies (such as visiting specific temples or offering prayers) to alleviate past karmic obstacles. They are entirely voluntary."),
      ("What is the difference between right and left thumb impression?", "According to Nadi astrology tradition, the right thumb impression is used for males and the left thumb impression for females.")
    ])}
  </div>
</section>
"""
render_page("/faq/", "Frequently Asked Questions | Agastya Nadi Jyotish FAQ", "Comprehensive FAQ for Agastya Nadi Jyotish: leaf identification process, online video reading authenticity, remedies, and payment options.", faq_page_body)

# Privacy Policy
privacy_body = f"""
{make_breadcrumbs([("Home", "/"), ("Privacy Policy", "/privacy-policy/")])}
<section class="section">
  <div class="container" style="max-width:850px; line-height:1.8;">
    <h1>Privacy Policy</h1>
    <p>Last updated: September 2026</p>
    <p>At <strong>Agastyanadijyotish.com</strong>, we take your privacy seriously, especially regarding sensitive personal data such as thumb impressions and birth details.</p>
    
    <h2>1. Data Collection & Use</h2>
    <p>We collect your thumb impression image, full name, contact number, and email solely for the purpose of locating your personal Nadi palm leaf manuscript and conducting your reading consultation.</p>
    
    <h2>2. Data Deletion & Protection</h2>
    <p>Your thumb impression image and personal details are encrypted and stored securely. Once your consultation session is complete, you may request complete deletion of your thumb image records by contacting us at info@agastyanadijyotish.com.</p>
    
    <h2>3. No Third-Party Sharing</h2>
    <p>We strictly do NOT sell, rent, or trade your personal data or thumb impressions to any third-party marketing services.</p>
  </div>
</section>
"""
render_page("/privacy-policy/", "Privacy Policy | Agastya Nadi Jyotish", "Privacy Policy for agastyanadijyotish.com. Learn how we collect, protect, and handle thumb impressions and personal data.", privacy_body)

# Terms of Service
terms_body = f"""
{make_breadcrumbs([("Home", "/"), ("Terms of Service", "/terms/")])}
<section class="section">
  <div class="container" style="max-width:850px; line-height:1.8;">
    <h1>Terms of Service</h1>
    <p>Last updated: September 2026</p>
    <p>By accessing and using <strong>agastyanadijyotish.com</strong> or booking a consultation, you agree to the following terms and conditions.</p>
    
    <h2>1. Nature of Consultation</h2>
    <p>Agastya Nadi Jyotish is a traditional spiritual and astrological advice service based on ancient Tamil manuscript interpretations. Readings are intended for personal guidance and philosophical exploration.</p>
    
    <h2>2. Booking & Cancellations</h2>
    <p>Reading slots are booked in advance. If your leaf is not found during the bundle search phase, any advance deposit will be refunded in full.</p>
  </div>
</section>
"""
render_page("/terms/", "Terms of Service | Agastya Nadi Jyotish", "Terms of Service for booking online and in-person Agastya Nadi consultations.", terms_body)

# Disclaimer Page
disclaimer_body = f"""
{make_breadcrumbs([("Home", "/"), ("Disclaimer", "/disclaimer/")])}
<section class="section">
  <div class="container" style="max-width:850px; line-height:1.8;">
    <h1>Spiritual & Astrological Disclaimer</h1>
    <p>Agastya Nadi Jyotish readings delivered via agastyanadijyotish.com are provided strictly for spiritual, cultural, and self-reflective purposes. Predictions and remedies discussed during consultations do not constitute certified medical, legal, financial, or psychiatric advice.</p>
    <p>No guaranteed outcomes are promised or implied. Seekers are advised to exercise personal judgment and consult licensed professionals for health, financial, or legal matters.</p>
  </div>
</section>
"""
render_page("/disclaimer/", "Disclaimer | Agastya Nadi Jyotish Spiritual Guidance", "Spiritual and astrological guidance disclaimer for agastyanadijyotish.com consultations.", disclaimer_body)

# ---------------------------------------------------------
# 7. HINDI TRACK PAGES
# ---------------------------------------------------------

# Hindi Home (/hi/index.html)
hi_home_body = f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-content">
      <span class="badge">वैथीश्वरन कोइल की प्रामाणिक परंपरा</span>
      <h1>अगस्त्य नाड़ी ज्योतिष - ऑनलाइन ताड़पत्र भविष्यवाणी</h1>
      <p>महर्षि अगस्त्य द्वारा हजारों वर्ष पूर्व लिखे गए आपके भाग्य पत्र की खोज करें। वैथीश्वरन कोइल से सीधे ऑनलाइन वीडियो कॉल या व्यक्तिगत रूप से प्रामाणिक नाड़ी ज्योतिष परामर्श।</p>
      <div class="hero-actions">
        <a href="/hi/book-consultation/" class="btn btn-primary">परामर्श बुक करें</a>
        <a href="/hi/nadi-jyotish-online/" class="btn btn-outline">ऑनलाइन परामर्श जानें</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header">
      <h2>अगस्त्य नाड़ी ज्योतिष क्या है?</h2>
      <p>यह तमिल नाडु के वैथीश्वरन कोइल में संरक्षित ताड़पत्रों (ओलाई चुवडी) पर आधारित प्राचीन भविष्यवाणियों की एक पवित्र प्रणाली है।</p>
    </div>
  </div>
</section>
"""
render_page("/hi/", "अगस्त्य नाड़ी ज्योतिष | वैथीश्वरन कोइल नाड़ी ज्योतिष ऑनलाइन", "प्रामाणिक अगस्त्य नाड़ी ज्योतिष ताड़पत्र भविष्यवाणी। वैथीश्वरन कोइल से सीधे ऑनलाइन वीडियो कॉल परामर्श और हिंदी अनुवाद प्राप्त करें।", hi_home_body, is_hindi=True, nav_active="home")

# Hindi Online (/hi/nadi-jyotish-online/index.html)
hi_online_body = f"""
{make_breadcrumbs([("मुख्य पृष्ठ", "/hi/"), ("ऑनलाइन नाड़ी ज्योतिष", "/hi/nadi-jyotish-online/")])}
<section class="section">
  <div class="container">
    <h1>ऑनलाइन नाड़ी ज्योतिष परामर्श (हिंदी)</h1>
    <p>अब आप दिल्ली, मुंबई, पुणे या विश्व में कहीं भी बैठकर अपने अंगूठे के निशान के माध्यम से अपना नाड़ी पत्र खोज सकते हैं। लाइव वीडियो कॉल और हिंदी अनुवाद उपलब्ध।</p>
    <a href="/book-consultation/" class="btn btn-primary">अभी बुक करें</a>
  </div>
</section>
"""
render_page("/hi/nadi-jyotish-online/", "ऑनलाइन नाड़ी ज्योतिष | हिंदी में ताड़पत्र भविष्यवाणी", "ऑनलाइन नाड़ी ज्योतिष परामर्श हिंदी में। वैथीश्वरन कोइल से सीधे लाइव वीडियो कॉल पर अपने अगस्त्य नाड़ी पत्र की खोज करें।", hi_online_body, is_hindi=True, nav_active="online")

# Hindi Delhi (/hi/nadi-jyotish-delhi/index.html)
hi_delhi_body = f"""
{make_breadcrumbs([("मुख्य पृष्ठ", "/hi/"), ("नाड़ी ज्योतिष दिल्ली", "/hi/nadi-jyotish-delhi/")])}
<section class="section">
  <div class="container">
    <h1>दिल्ली NCR में अगस्त्य नाड़ी ज्योतिष ऑनलाइन</h1>
    <p>दिल्ली, गुड़गांव और नोएडा के श्रद्धालुओं के लिए वैथीश्वरन कोइल से सीधे ऑनलाइन नाड़ी ज्योतिष ताड़पत्र परामर्श सेवा।</p>
  </div>
</section>
"""
render_page("/hi/nadi-jyotish-delhi/", "नाड़ी ज्योतिष दिल्ली NCR | ऑनलाइन अगस्त्य नाड़ी परामर्श", "दिल्ली, गुड़गांव और नोएडा के लिए ऑनलाइन नाड़ी ज्योतिष। बिना दक्षिण भारत जाए हिंदी में प्रामाणिक ताड़पत्र भविष्यवाणी प्राप्त करें।", hi_delhi_body, is_hindi=True, nav_active="online")

# Hindi Mumbai (/hi/nadi-jyotish-mumbai/index.html)
hi_mumbai_body = f"""
{make_breadcrumbs([("मुख्य पृष्ठ", "/hi/"), ("नाड़ी ज्योतिष मुंबई", "/hi/nadi-jyotish-mumbai/")])}
<section class="section">
  <div class="container">
    <h1>मुंबई में अगस्त्य नाड़ी ज्योतिष ऑनलाइन परामर्श</h1>
    <p>मुंबई, ठाणे और नवी मुंबई के निवासियों के लिए वैथीश्वरन कोइल से लाइव वीडियो कॉल पर नाड़ी ज्योतिष परामर्श।</p>
  </div>
</section>
"""
render_page("/hi/nadi-jyotish-mumbai/", "नाड़ी ज्योतिष मुंबई | हिंदी ऑनलाइन ताड़पत्र भविष्यवाणी", "मुंबई निवासियों के लिए प्रामाणिक अगस्त्य नाड़ी ज्योतिष ऑनलाइन। लाइव वीडियो कॉल और हिंदी अनुवाद के साथ अपना नाड़ी पत्र जानें।", hi_mumbai_body, is_hindi=True, nav_active="online")


# ---------------------------------------------------------
# 8. SITEMAP.XML, ROBOTS.TXT, 404.HTML
# ---------------------------------------------------------

# Sitemap.xml
sitemap_urls = ""
for url in pages_generated:
  sitemap_urls += f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-09-27</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_urls}</urlset>
"""

with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
  f.write(sitemap_xml)

# Robots.txt
robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""

with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
  f.write(robots_txt)

# 404 Page
render_page("/404.html", "Page Not Found | Agastya Nadi Jyotish", "The requested page was not found. Return to Agastya Nadi Jyotish home page.", """
<section class="section">
  <div class="container text-center" style="text-align:center; padding:4rem 0;">
    <span class="badge">404 Error</span>
    <h1>Page Not Found</h1>
    <p>The page you are looking for might have been moved or does not exist.</p>
    <a href="/" class="btn btn-primary" style="margin-top:1rem;">Return to Home Page</a>
  </div>
</section>
""")

print(f"Build finished successfully! Total {len(pages_generated)} pages generated in output directory.")
