# Sticky Mobile Menu Overlay Fix

- **Symptom:** On mobile devices, clicking a navigation link inside the hamburger menu (e.g., "Shop", "About", "Contact") scrolled the page to the target section, but the dark menu overlay remained visible and blocked the content.
- **Root Cause:** Because the website functions as a Single Page Application (using anchor hash links to scroll to different sections), the browser does not trigger a full page reload when a navigation link is clicked. Without a page reload, the state of the mobile menu remains unchanged (open).
- **The Fix:** We injected a JavaScript event listener inside `index.html` that specifically listens for clicks on any anchor tag within `.nav-center`. When a click is detected on a screen width of 768px or less, it explicitly sets `document.querySelector('.nav-center').style.display = 'none';`, immediately hiding the overlay.
- **Future Prevention:** Whenever implementing anchor-based smooth scrolling or SPA-style navigation, always ensure that overlay menus have an automatic close event bound to their child links.
