# DB Sneakers Hype Hub — Complete Project Documentation 🚀
## Last Updated: April 4, 2026

---

## PROJECT STATUS: ✅ CHECKOUT FLOW COMPLETE & TESTED

The DB Sneakers Hype Hub website is a fully functional e-commerce store connected to Shopify.

---

## Quick Reference

| Item | Value |
|------|-------|
| **Shopify Store URL** | `db-sneakers-hype-hub.myshopify.com` |
| **Shopify Admin** | `db-sneakers-hype-hub.myshopify.com/admin` |
| **Partner Account** | `pacheco.carlos887@gmail.com` at `partners.shopify.com` |
| **Storefront API Token** | `0906a0e54db9ccce653c2a568a2fc54b` |
| **Staging File** | `index-staging.html` (development — has live credentials) |
| **Production File** | `index.html` (clean copy — update when ready to launch) |
| **SDK** | Shopify Buy Button SDK via CDN |
| **Test Payment Provider** | Bogus Gateway (card `1` = approved, `2` = declined, `3` = error) |

---

## Account Setup Details

### Shopify Partner Account
- **Owner:** Carlos Pacheco III
- **Email:** pacheco.carlos887@gmail.com
- **URL:** partners.shopify.com
- **Purpose:** Free developer access to build client stores

### Development Store
- **Store name:** DB Sneakers Hype Hub
- **URL:** db-sneakers-hype-hub.myshopify.com
- **Type:** Client Transfer Store (free until transferred to Daniel)
- **Business location:** United States

### Storefront API App
- **App name:** Hype Hub Storefront (legacy custom app)
- **Token:** 0906a0e54db9ccce653c2a568a2fc54b
- **API Scopes:**
  - `unauthenticated_read_product_listings`
  - `unauthenticated_read_product_inventory`
  - `unauthenticated_read_product_tags`
  - `unauthenticated_write_checkouts`
  - `unauthenticated_read_checkouts`

---

## Test Products in Shopify

| Product | Type | Price | Compare At | Initial Inventory |
|---------|------|-------|-----------|-------------------|
| Air Max 90 Retro | Sneaker | $129.99 | $159.99 | 10 |
| Retro Snapback Gold | Hat | $34.99 | $44.99 | 25 |

---

## Test Order Completed

- **Order #:** A5MJ9H5AN
- **Total:** $164.98 USD
- **Payment:** Bogus Gateway (test mode)
- **Status:** ✅ Confirmed
- **Date:** April 4, 2026

---

## Architecture

```
Customer visits website (index.html or index-staging.html)
    ↓
Shopify Buy SDK loads from CDN
    ↓
initShopifyClient() connects to db-sneakers-hype-hub.myshopify.com
    ↓
fetchShopifyProducts() pulls products via Storefront API (paginated, 20 at a time)
    ↓
renderProducts() displays them in the 90s-themed product grid
    ↓
addToCart() → updateCart() → goToCheckout()
    ↓
shopifyClient.checkout.create() + addLineItems()
    ↓
Redirect to checkout.shopify.com (Shopify handles payment securely)
    ↓
Order appears in Shopify Admin → Daniel ships the product
```

---

## Scaling & Security Features Implemented

### Pagination (N+1 Fix)
- Products load in batches of 20 using `fetchQuery({first: 20})`
- "LOAD MORE HEAT" button uses `fetchNextPage()` for additional products
- Handles catalogs of any size efficiently

### Environment Separation
- `index-staging.html` = Development (test freely here)
- `index.html` = Production (keep clean, update only when ready)

### Error Handling
- 90s-themed "CONNECTION LOST! CHECK YOUR DIAL-UP!" fallback for network errors
- Retry button functionality for both product loading and checkout
- Graceful degradation if Shopify API is unreachable

---

## Bugs Fixed During Integration (April 4, 2026)

1. **Cloudflare script tag** — Removed `data-cfasync` src attribute that blocked all inline JS
2. **Shopify product IDs** — Wrapped string IDs in quotes inside onclick handlers
3. **Cart total variable** — Added `let total=0;` initialization before cart render loop
4. **Cart footer visibility** — Added `f.style.display='block';` to show checkout button
5. **Checkout client check** — Removed `.domain` property check that doesn't exist on SDK

---

## What Daniel Can Do Without Code

| Task | How |
|------|-----|
| **Add products** | Shopify Admin → Products → Add product |
| **Bulk import** | Products → Import → Upload CSV file |
| **Process orders** | Shopify Admin → Orders |
| **Issue refunds** | Orders → select order → Refund (full or partial) |
| **Cancel orders** | Orders → select order → Cancel |
| **Track inventory** | Automatic — stock decreases with each sale |
| **Customer emails** | Automatic — order confirmation, shipping, refund notifications |
| **Add tracking** | Orders → select order → Enter tracking number |

---

## Steps to Go Live 🚀

1. [ ] Daniel adds his real product catalog (sneakers & hats with photos, prices, sizes)
2. [ ] Transfer store ownership from Partner account to Daniel's Shopify account
3. [ ] Daniel selects a Shopify plan (Basic $39/mo recommended to start)
4. [ ] Daniel sets up real Shopify Payments (with his banking info for payouts)
5. [ ] Enable Shop Pay, Apple Pay, Google Pay in payment settings
6. [ ] Buy a custom domain (e.g., dbsneakers.com)
7. [ ] Host index.html on a platform (Netlify, Vercel, or Shopify hosting)
8. [ ] Copy credentials from index-staging.html to index.html
9. [ ] Final end-to-end test with real payment provider
10. [ ] GO LIVE! 🚀

---

## Important Notes
- **Storefront API tokens are PUBLIC by design** — they only allow read access to products and creating checkouts. No sensitive data is exposed.
- **All payment processing happens on Shopify's secure domain** (checkout.shopify.com) — we never touch credit card data.
- **Daniel should install the Shopify mobile app** for real-time order notifications on his phone.
- **Bulk uploads:** For 100+ products, use CSV import. Shopify provides a template at Settings → Products → Import.
