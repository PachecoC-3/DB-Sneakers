# FOMO Banner Mobile Navigation Overlap

- **Symptom:** The top portion of the hero section text (e.g., "ESTABLISHED 2024") was visibly cut off on mobile devices, hiding behind the search bar and navigation menu.
- **Root Cause:** The dynamically injected FOMO countdown banner (`#hypeBanner`) was structurally nested inside the `fixed` top navigation bar. This increased the total pixel height of the navigation block beyond the static `margin-top` (60px) assigned to the hero section underneath it, causing the content to slide up and under the nav.
- **The Fix:** Globally increased the `margin-top` CSS values for `.hero` and `.video-hero` from 60px/72px to `110px` across both desktop and mobile media queries to safely clear the combined height of the navigation plus the FOMO banner.
- **The Prompt That Worked:** "you see how on mobile, at least android, the top portion is a bit cutoff? Right under the search bar? Can you see this cutoff text?"
- **Future Prevention:** Whenever injecting new UI elements (like announcement bars) into a `position: fixed` global navigation component, always verify and explicitly increase the subsequent sibling section's `margin-top` or `padding-top` to match the new computed vertical height.
