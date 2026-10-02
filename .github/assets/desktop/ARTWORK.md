# Linux Desktop artwork

The profile uses the approved violet Linux Desktop concept. Assets are local and need no runtime build or external image service.

## Hero

- Active file: `hero-ubuntu-v3.png`.
- Eye correction source: `hero-ubuntu-v2.png`, retained as the previous version.
- Original artwork: `hero.png`, retained as the source for the targeted edit.
- Generated using the built-in image generation tool on 2026-10-02.
- The concept mockup was used as a style reference; its provisional project copy was not reused.
- The active hero uses Ubuntu's Circle of Friends and a clearly visible, opaque eye moved farther back from the beak. The eye correction was made with the built-in image generation tool. It is a static illustration.

### Final generation prompt

```text
Use case: ui-mockup.
Asset type: final production hero banner artwork for Muhammad Yousaf's GitHub profile README.
Input image: supplied previous full-page mockup is a STYLE REFERENCE ONLY. Generate a new standalone wide hero artwork matching its top panel, not a whole README screenshot.
Primary request: a spectacular Linux desktop inspired hero banner in a wide landscape composition approximately 1536x864. Dark nearly-black aubergine with brilliant violet, icy cyan, warm orange points, sharp readable off-white typography, realistic three dimensional graphic illustration.
Composition: one standalone rounded framed hero window, hairline violet border, tiny decorative orange/violet/cyan window dots in thin top bar; small monospace bar title exactly "yousaf@linux ~" and small right bar label exactly "systems / agents / web". In left upper-middle region the large name exactly "MUHAMMAD" on first line and "YOUSAF" in violet on second line, enormous heavy modern sans serif. Below name three short lines exactly "Linux Systems", "Agentic AI", "Full-stack Engineering" separated by fine small colored dots or consistent left alignment; ensure readable mobile-scaled type, do not cram a long subtitle.
Main illustrative focal object on right: large dimensional low-poly Tux-inspired penguin, black crystalline surfaces, beautiful electric violet and cyan wireframe facets, orange beak and white chest, sitting amongst angular dark mountain ranges with distant purple planet backdrop. Floating translucent glass window outlines with simple circuit motifs, orbital AI node links, dramatic subtle glows. Penguin must clearly read as Linux, premium illustration not cartoon sticker.
At bottom right integrate a SMALL graphical terminal window titled "~/building" with three readable lines exactly "parse → execute", "reason → act", "ship → improve". Terminal is a secondary accent only. Main text avoids overlap with penguin or terminal; strong negative space, clear professional hierarchy.
Overall: match supplied reference's violet Linux ricing mood and spectacular visual richness, cohesive refined colors, rendered as a sharp premium banner. All important labels away from edges.
Constraints: output contains ONLY the standalone hero banner, no project cards, no tool stack, no footer, no concept label "02", no mockup frame, no GitHub browser UI, no outer page, no security claims, no random supplementary prose, no time or status claims, no watermark. Exact spelling of MUHAMMAD YO U S A F = YOUSAF. No fabricated biography. The artwork is intended to be embedded as an image in Markdown.
```

### Previous Ubuntu edit prompt

```text
Use case: precise-object-edit.
Asset type: existing final GitHub profile hero banner; make a precise, conservative edit.
Input image: the attached local hero.png is the EDIT TARGET. Keep its original wide aspect ratio and composition.
Primary request: change ONLY two details in this exact artwork.
1. In the small translucent floating window at the lower center-left (approximately x=45% of image width, y=68% of image height), replace the white Arch Linux A-shaped symbol with the authentic Ubuntu "Circle of Friends" logo: a circle formed by three equally spaced connected curved sections with three small circular heads around its outside, precisely balanced and recognizable. The mark should be Ubuntu orange with restrained glow, sitting centered on the same glass pane at about the same visual size. No Arch Linux symbol remains. Do not add "Ubuntu" text or any additional logos.
2. Correct the left-facing penguin's single visible eye. Its current orange concentric camera-like ring looks unnatural and is poorly seated on the face. Remove that eye completely and place a smaller, natural dark eye correctly within the side of its head, above and slightly behind the beak hinge, underneath the forehead, following the perspective of the existing left-facing head. Use a subtly oval dark iris/pupil, an anatomically seated eyelid, and a tiny restrained white specular reflection. No orange ring or red mechanical eye. Integrate it with the black faceted face so it belongs to the head; preserve the head shape, orange beak, pose, wireframe geometry, and lighting elsewhere.
Invariants: preserve ALL other pixels and layout as closely as possible. Keep exactly the existing palette, mountains, planets, purple and cyan wireframe penguin body, glass windows, circuitry and dots, top title bar, border, foreground scenery, and terminal panel. Do not zoom, crop, redesign, recolor the whole image, or move objects.
Preserve ALL text verbatim, in its original position and typography: "yousaf@linux ~", "systems / agents / web", "MUHAMMAD", "YOUSAF", "Linux Systems", "Agentic AI", "Full-stack Engineering", "~/building", "parse → execute", "reason → act", "ship → improve".
No circles or arrows marking the edits, no annotations, no captions, no watermark. Output only the corrected final banner.
```

### Eye relocation and visibility — final edit prompt

```text
Use case: precise-object-edit.
Input image: hero-ubuntu-v2.png is the edit target. Make a strictly local edit ONLY to the penguin eye.
Critical correction: the current eye is much too close to the beak and far too dim. Changing only its opacity or size is NOT sufficient. The eye MUST be visibly relocated.
Coordinates in the supplied 1672 x 941 image: the WRONG old eye is centered approximately at (1117, 199). Remove this old eye completely and restore the dark head surface there. Place the ONLY visible NEW eye centered approximately at (1190, 192): about 73 pixels to the RIGHT of the current eye, farther BACK from the orange beak into the middle of the broad side of the penguin's head. This is approximately 71.2% of image width and 20.4% of image height. Do not move it left toward the beak or leave it at its original location.
New eye: clearly visible, FULLY OPAQUE, crisp and naturally seated in the side of the head. About 24 pixels across and 18 pixels high, following the head's left-facing perspective. Give it a modest ivory-white eye surround, a warm brown iris with a solid dark pupil, and a distinct small white reflection. This is an organic bird eye with a subtle eyelid, NOT a glowing ring, camera lens, red robotic eye, or translucent barely visible dot. Locally integrate the faceted surface around this eye so no wireframe edge crosses the eye. There must be a generous, plainly visible area of black face BETWEEN the beak base and the new eye, so the eye looks like it belongs on the side of the skull instead of the nose.
Invariants: preserve the penguin's existing head outline, beak, pose, neck, low-poly body, all purple/cyan lighting, the Ubuntu logo, every floating window, mountains, planets, circuit trails, terminal panel, and background. Preserve all text and its positioning exactly, especially "MUHAMMAD YOUSAF", "yousaf@linux ~", "systems / agents / web", "Linux Systems", "Agentic AI", "Full-stack Engineering", "~/building", "parse → execute", "reason → act", "ship → improve".
Keep the original image dimensions and framing. Do not globally change brightness or opacity. No annotations, arrows, circles, watermark, or extra eye. Output only the corrected banner.
```

## Code-native illustrations and animation

The section headings, five project banners, four experience banners, contact cards, and animated waveform are generated by [generate_desktop_assets.py](../../scripts/generate_desktop_assets.py). The project diagrams are illustrative, not live activity or performance data. Each animated project banner has a static reduced-motion alternative and a separate mobile composition.

## Content references

The selected projects' summaries, achievements, employment dates, education, and engineering notes are retained. Additional implementation detail and the Hiba Logics internship come from the owner's [project data](https://github.com/Yosf96633/new_portfolio/blob/main/src/features/profile/data/projects.ts), [experience data](https://github.com/Yosf96633/new_portfolio/blob/main/src/features/profile/data/experiences.ts), and [stack data](https://github.com/Yosf96633/new_portfolio/blob/main/src/features/profile/data/tech-stack.ts). Better Auth Starter's expanded description follows its [README](https://github.com/Yosf96633/Better_auth_starter). The sentiment project is named Vidspire in the previous README and Vidly in the portfolio; both names are retained.
