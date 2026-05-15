# Netlify Build Minute Exhaustion

- **Symptom:** The project was rapidly burning through its monthly allocation of Netlify build minutes, leading to potential service freezes or unexpected billing for the DB Sneakers live site.
- **Root Cause:** The continuous integration (CI) deployment workflow was unoptimized. Netlify was automatically triggering full site builds on every minor commit, save, or non-production branch push, executing heavy build scripts unnecessarily.
- **The Fix:** Reconfigured the Netlify deployment workflow and CI pipeline rules. Implemented branch-specific build triggers to ensure only production-ready pushes initiated a full build, bypassing the build sequence for minor adjustments and test branches.
- **The Prompt That Worked:** "Optimize the site's deployment workflow on Netlify to avoid unnecessary build usage."
- **Future Prevention:** Upon setting up a new client site on Netlify or similar hosting platforms, immediately configure the `netlify.toml` file with strict `ignore` commands and lock auto-publishing exclusively to the `main` production branch to preserve computing resources.
