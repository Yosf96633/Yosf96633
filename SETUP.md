# Muhammad Yousaf · GitHub profile package

## Install

1. Open your public profile repository: `Yosf96633/Yosf96633`. Create it if it does not exist, using your exact GitHub username as the repository name.
2. Copy this package's `README.md` to the repository root.
3. Copy the complete `.github/assets/` directory into the repository. It is a hidden directory on Linux: press **Ctrl+H** in your file manager to show it.
4. Commit the README and assets together. Open your GitHub profile to see the result.

No build, API key, GitHub Action, hosting account, or package installation is required. The entire implementation is included in this archive. Keep the relative paths unchanged.

## Files and exact repository paths

| Repository path | Purpose |
| :--- | :--- |
| `README.md` | Complete profile content |
| `.github/assets/terminal-header.svg` | Editable desktop terminal artwork and SVG animation |
| `.github/assets/terminal-header.gif` | Desktop terminal playback |
| `.github/assets/terminal-mobile.svg` | Editable narrow terminal artwork and SVG animation |
| `.github/assets/terminal-mobile.gif` | Narrow terminal playback |
| `.github/assets/pipeline.svg` | Editable workflow artwork and SVG animation |
| `.github/assets/pipeline.gif` | Workflow playback |
| `.github/assets/footer.svg` | Editable terminal footer and SVG animation |
| `.github/assets/footer.gif` | Footer playback |
| `.github/assets/typing-intro.gif` | Looping terminal typing introduction |
| `.github/assets/typing-intro-static.png` | Reduced-motion typing introduction |
| `.github/assets/stack-flow.gif` | Animated connections across the tech stack |
| `.github/assets/stack-flow-static.png` | Reduced-motion tech stack illustration |
| `.github/scripts/generate_readme_animations.py` | Source generator for the typing and stack animations |
| `SETUP.md` | Installation and maintenance notes; does not need to be published |

```text
yousaf-profile/
  README.md
  SETUP.md
  .github/
    assets/
      terminal-header.svg
      terminal-header.gif
      terminal-mobile.svg
      terminal-mobile.gif
      pipeline.svg
      pipeline.gif
      footer.svg
      footer.gif
      typing-intro.gif
      typing-intro-static.png
      stack-flow.gif
      stack-flow-static.png
    scripts/
      generate_readme_animations.py
```

## Motion and editing

GIF files provide the default animation. The SVGs contain their own CSS animations and complete vector source; they need no external fonts, scripts, images, or stylesheets. The README uses SVG alternatives when a visitor prefers reduced motion; the SVGs also disable their animation for that preference.

The header keeps the identity readable while its cursor and session light animate. The workflow highlights successive nodes over a 14-second loop. These are illustrations, not live service health, agent execution, or contribution data.

The typing introduction cycles through four short lines about web apps, AI agents, document retrieval, and Linux. A moving signal and gently pulsing nodes connect the stack labels below the tools table. Both are local GIFs with static PNG alternatives for reduced motion.

To edit these two animations, update `.github/scripts/generate_readme_animations.py` and run `python3 .github/scripts/generate_readme_animations.py` from the repository root. Regeneration requires Pillow and the DejaVu Sans Mono font at the path specified in the script; displaying the committed images requires no dependencies.

The mobile header is selected below 600px. Text descriptions and links remain ordinary Markdown so essential information can be read even when images are unavailable.

Edit an SVG in a text editor or vector editor to change its artwork. GIFs are rendered copies, so SVG edits do not automatically update them: export the changed animation again, or change the matching image reference in the README to its SVG counterpart. GitHub's SVG file viewer can show a static preview; use the committed README to assess the final presentation.

## External services and links

The custom artwork makes no third-party requests. The tech stack icons load from [Skill Icons](https://github.com/tandpfun/skill-icons), with light and dark variants and ten icons per row. The text table below them lists the full stack, including Linux and tools without a matching icon in the grid.

The optional, collapsed statistics card uses another external image endpoint:

`https://github-readme-stats.vercel.app/api?username=Yosf96633&show_icons=true&hide_rank=true&hide_border=true&bg_color=0B0E14&title_color=C792EA&text_color=E6E6E6&icon_color=7CFFB2`

Collapsing the card does not guarantee that browsers defer its network request. To remove external image services, remove both the Skill Icons block and the optional telemetry `<details>` block. The text stack table and direct GitHub activity links still work without these images.

Navigation destinations:

- https://github.com/Yosf96633
- https://github.com/Yosf96633?tab=repositories
- https://github.com/Yosf96633/Autohunt
- https://github.com/Yosf96633/DocsAI
- https://linkedin.com/in/yousaf-dev18/
- https://yousaf-dev18.vercel.app/
- mailto:yousaf.dev18@gmail.com

## Optional statistics self-hosting

The public GitHub Readme Stats endpoint is best-effort and can fail during rate limits or traffic spikes. Its maintainers document deployment through GitHub Actions or your own hosted instance:

https://github.com/anuraghazra/github-readme-stats#deploy-on-your-own

Follow the current upstream deployment instructions. For a hosted instance, replace only `https://github-readme-stats.vercel.app` in the README with your deployment origin, keeping `/api` and the query parameters. Store any required token in the hosting provider's secret settings; never put it in the README or an image URL. A dedicated deployment still has GitHub API and hosting limits.

## References

- Profile repository setup: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- Relative README images: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- SVG image restrictions: https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image
- GitHub image viewing: https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files

## Content notes

Project descriptions and employment dates follow the supplied brief. No repository inspection, live deployment verification, new performance measurement, or account modification was performed. The speculative uptime line and broad production-ready claims were removed. No repository names were guessed for Vidspire, CamBot, or Better Auth Starter.
