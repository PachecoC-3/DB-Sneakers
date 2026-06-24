# Netlify Publish Directory Misconfiguration

- **Symptom:** Code pushed to the `main` branch on GitHub was successfully executing without errors, but the live website was not updating to reflect the new changes (e.g., CSS fixes, JavaScript functionality).
- **Root Cause:** The `netlify.toml` configuration file was explicitly instructing Netlify to build and publish the old `DB Sneakers` folder. As development shifted into the new `Storefront` folder to build "Option 28", the configuration file was never updated. Netlify dutifully republished the untouched, outdated `DB Sneakers/index.html` file on every push.
- **The Fix:** Modified `netlify.toml` to set `publish = "Storefront"`, pointing the live build process to the correct working directory.
- **Future Prevention:** 
  - Whenever migrating work to a new primary folder or restructuring the project, always double-check the deployment configuration (`netlify.toml` or Netlify UI) to ensure the build target matches the new directory.
  - If a live push succeeds on GitHub but doesn't reflect on the live URL (and caching has been ruled out via Incognito mode), immediately verify the target build directory.
