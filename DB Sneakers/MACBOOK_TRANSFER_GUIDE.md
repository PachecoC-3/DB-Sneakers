# 🚀 DB Sneakers Hype Hub — MacBook Transfer Guide

## Quick Start (5 Minutes)

### Step 1: Install Git
Open Terminal on MacBook and run:
```bash
xcode-select --install
```
This installs Git. Click "Install" when prompted.

### Step 2: Clone the Project
```bash
cd ~/Documents
git clone https://github.com/PachecoC-3/DB-Sneakers.git
cd DB-Sneakers
```

### Step 3: You're Done!
The entire project is now on your MacBook at `~/Documents/DB-Sneakers/`

---

## Project Structure
```
DB-Sneakers/
├── netlify.toml              ← Netlify deployment config
└── DB Sneakers/
    ├── index.html             ← LIVE production site
    ├── index-staging.html     ← STAGING/test site (video hero + new features)
    ├── _redirects             ← Netlify routing
    ├── assets/
    │   ├── hero-bg.mp4        ← Hero section background video
    │   └── img/
    │       ├── brand_logo.png ← Main logo (used everywhere)
    │       ├── logo_graffiti.png
    │       ├── tag_drip.png
    │       └── tag_hype.png
    ├── process_images.py      ← Image processing script
    ├── PROCESS_IMAGES.bat     ← Windows batch runner (won't need on Mac)
    └── inventory_staging/     ← Staging product images
```

---

## 🔑 Critical Credentials & URLs

### Shopify Storefront API
- **Store:** `db-sneakers-hype-hub-llc.myshopify.com`
- **Storefront Access Token:** `33f66e06740a2a5c1fdfe9fecf9b6a58`
- **API Version:** `2024-01`
- **GraphQL Endpoint:** `https://db-sneakers-hype-hub-llc.myshopify.com/api/2024-01/graphql.json`

### Shopify Admin
- **Admin URL:** `https://admin.shopify.com/store/db-sneakers-hype-hub-llc`
- **Login:** Daniel's Shopify credentials

### Netlify Deployment
- **Live Site:** `https://dbsneakershypehubllc.com`
- **Staging Site:** `https://luxury-chebakia-92f0bb.netlify.app/index-staging.html`
- **GitHub Repo:** `https://github.com/PachecoC-3/DB-Sneakers.git`
- **Auto-deploys:** Every `git push origin main` auto-deploys to Netlify

### GitHub
- **Repo:** `https://github.com/PachecoC-3/DB-Sneakers`
- **Branch:** `main`

---

## 🖥️ How to Make Changes on MacBook

### Edit the site:
1. Open `DB Sneakers/index.html` (live) or `index-staging.html` (test) in any code editor
2. VS Code recommended: `brew install --cask visual-studio-code`

### Push changes live:
```bash
cd ~/Documents/DB-Sneakers
git add .
git commit -m "Description of your change"
git push origin main
```
Changes go live on Netlify within ~30 seconds.

### Test locally:
```bash
cd "DB Sneakers"
python3 -m http.server 8000
```
Then open `http://localhost:8000` in your browser.

---

## 📋 Current Status

### Live Site (index.html)
- ✅ Full Shopify inventory (259 products)
- ✅ GraphQL cursor-based pagination
- ✅ Alphabetical sorting (default)
- ✅ Clickable page numbers
- ✅ Logo scrolls to top
- ✅ Shop Pay checkout
- ✅ Shopify storefront redirects to custom site

### Staging Site (index-staging.html) — PENDING DANIEL APPROVAL
- ✅ Everything from live, PLUS:
- ✅ Full-screen video hero section
- ✅ Branded loading screen (logo + progress bar)
- ✅ Favicon (logo in browser tab)
- ✅ Product images fill boxes (object-fit: cover)
- ✅ Taller image containers (340px)
- ✅ Mobile-optimized video hero (45vh)
- ✅ Mobile 2-column bento grid with yellow gaps

### To Push Staging → Live:
Once Daniel approves, copy staging content to production:
```bash
cp "DB Sneakers/index-staging.html" "DB Sneakers/index.html"
git add . && git commit -m "LIVE: Video hero + all staging features" && git push origin main
```

---

## 🔧 Shopify Admin Changes Made

### Checkout Redirect (theme.liquid)
Added to `layout/theme.liquid` line 9:
```html
<script>window.location.href = "https://dbsneakershypehubllc.com/";</script>
```
This redirects anyone hitting the old Shopify storefront to the custom site.

---

## 📱 Social Links
- **TikTok 1:** `https://www.tiktok.com/@DBsneakershypehub3`
- **TikTok 2:** `https://www.tiktok.com/@DB.Sneakers.Hype`
- **Instagram:** `https://www.instagram.com/db.sneakers.hype.hub/`
- **WhatsApp:** `https://wa.me/13122909736`

---

## ⚠️ Things Daniel Still Needs To Do
1. **Set Product Types** in Shopify Admin — many products show as "Misc" instead of "Hat"
2. **Film a custom video** — replace the stock hero video with his own product reel
3. **Consider a custom domain** — already has `dbsneakershypehubllc.com` ✅
