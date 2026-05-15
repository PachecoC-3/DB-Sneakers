# CSS Variable Inheritance & Overflow Layout Break

- **Symptom:** When injecting a clean, white micro-interaction card component into the live site, the card turned dark navy blue and the text items improperly hung out the bottom of the card during the hover animation.
- **Root Cause:** The new component inherited a global CSS variable (`var(--card-bg)`) intended for the site's default dark cards, and the container lacked explicit height constraints to hide overflowing items during the Y-axis transform.
- **The Fix:** Removed the global CSS variable references, hardcoded the intended DB Sneakers Cyan (`var(--pr)`) to isolate the component from global themes. Explicitly set `height: 60px; overflow: hidden;` on the `info-container` and increased the hover translate distance from `-20px` to `-60px` to ensure the default text slides completely out of the frame.
- **The Prompt That Worked:** "this looks nothing like this option 28 style. Also instead of the dark navy blue, can we change that to the color of picture 3?"
- **Future Prevention:** When injecting standalone templates into existing client sites, ALWAYS verify global CSS variable overrides. Explicitly define container heights and `overflow: hidden` when using `transform: translateY` micro-animations to prevent text bleeding.
