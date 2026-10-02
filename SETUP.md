# Muhammad Yousaf · Linux Desktop profile

The README implements the violet Linux Desktop design with a geometric penguin hero, illustrated project panels, animated SVG diagrams, a waveform ribbon, and linked technology icons. All profile and project text stays readable as ordinary Markdown.

## Install

1. Use the public profile repository `Yosf96633/Yosf96633`.
2. Keep `README.md` in the repository root and copy the complete `.github/assets/` directory with it.
3. Commit the README and assets together. The relative image paths must remain unchanged.

Displaying the committed profile requires no build, API key, GitHub Action, or hosting account. This workspace change has not been committed or pushed.

## Content coverage

- All five selected projects have visible descriptions: myShell, AutoHunt, DocsAI, Vidspire / Vidly, and Better Auth Starter.
- The four extensively documented projects include expandable implementation and architecture notes from the public portfolio.
- AutoHunt uses its actual CV-to-job-application workflow, replacing the provisional mockup's security-research description.
- All 42 original stack icons are retained. Sixteen additional technologies from the portfolio, projects, and experience bring the stack to 58 icons.
- All three original experience entries and their achievements are retained. The earlier Hiba Logics PHP/Laravel internship is included from the public portfolio.
- Education, engineering notes, GitHub activity links, the optional statistics card, and contact links are retained.

Names are available through icon hover titles and alternative text; the stack has no text-only badges. Each icon links to its technology's site. The sentiment project was called Vidspire in the previous README and Vidly in the portfolio, so both names are displayed.

## Assets

| Repository path | Purpose |
| :--- | :--- |
| `.github/assets/desktop/hero-ubuntu-v3.png` | Active static hero with the Ubuntu logo and a visible eye placed farther back from the beak |
| `.github/assets/desktop/project-*.svg` | Five animated project diagrams, with desktop/mobile and static alternatives |
| `.github/assets/desktop/section-*.svg` | Eight section headings |
| `.github/assets/desktop/stack-*.svg` | Seven technology group headings, with mobile compositions |
| `.github/assets/desktop/experience-*.svg` | Four experience panels, with mobile compositions |
| `.github/assets/desktop/contact-*.svg` | Three linked contact cards |
| `.github/assets/desktop/building.gif`, `building-mobile.gif` | Animated violet/cyan waveform compositions |
| `.github/assets/desktop/building-static.png`, `building-mobile-static.png` | Reduced-motion waveforms |
| `.github/assets/desktop/ARTWORK.md` | Hero generation prompt, tool provenance, and content references |
| `.github/assets/stack/` | 58 local technology logos and source/license notes |
| `.github/scripts/generate_desktop_assets.py` | Editable vector artwork and waveform generator |
| `.github/scripts/prepare_desktop_icons.py` | Contrast tiles for the additional SVG marks |

The earlier terminal assets and generator are retained, but the new README does not use them.

## Motion, mobile layouts, and interaction

The project banners animate a few points along their illustrated connections using native SVG animation. The waveform is a small looping GIF. These illustrations do not report live system health, contribution counts, or performance measurements.

The README selects static project illustrations and the static waveform for `prefers-reduced-motion: reduce`. Project and experience artwork uses a separate composition below 600px. Technology icons wrap naturally on narrow screens. The native descriptions and links remain usable if images do not load.

Section navigation uses GitHub-supported custom named anchors. Project panels and contact cards link to real destinations; implementation notes and the GitHub statistics card expand with native `details` elements. The profile does not require scripts or custom page CSS.

## Edit or regenerate

Edit `README.md` to update descriptions, dates, contact links, or the icon grid. The current text incorporates the previous README plus the public portfolio's project and experience details; references are in `ARTWORK.md`.

Edit the design data and drawing functions in `.github/scripts/generate_desktop_assets.py`, then run:

```bash
python3 .github/scripts/generate_desktop_assets.py
```

Regeneration uses Python, Pillow, and the DejaVu Sans / Sans Mono fonts under `/usr/share/fonts/truetype/dejavu/`. It redraws the code-native SVGs and waveform; it does not replace or edit the generated hero. Committed assets display without these dependencies.

New SVG marks can be placed on contrast tiles with:

```bash
python3 .github/scripts/prepare_desktop_icons.py
```

The script is idempotent and preserves the upstream logo paths and colors. BullMQ uses its original wide logo at the correct aspect ratio.

To replace the hero, use the image generation prompt in `ARTWORK.md` with the built-in image generation tool and save the chosen banner as a new version before changing the README reference.

## External services

All custom artwork and technology logos are local. Only the optional, collapsed GitHub statistics image uses `github-profile-summary-cards.vercel.app`; its availability depends on that service. No live stats are invented in the local artwork.

Logo provenance is recorded in `.github/assets/stack/SOURCES.md`; the original Devicon MIT license remains included. Brand marks remain the property of their respective owners.

## References

- Profile README setup: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- Relative images and README behavior: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- Custom anchors: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#custom-anchors
- SVG as an image: https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image
