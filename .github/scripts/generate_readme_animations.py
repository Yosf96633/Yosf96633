"""Regenerate README animations with Python and Pillow."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ASSETS = Path(__file__).resolve().parents[1] / "assets"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BG = "#0B0E14"
BORDER = "#263040"
TEXT = "#E6E6E6"
MUTED = "#9AA3B8"
GREEN = "#7CFFB2"
PURPLE = "#C792EA"


def font(size):
    return ImageFont.truetype(FONT_PATH, size)


def card(size):
    image = Image.new("RGB", size, BG)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((1, 1, size[0] - 2, size[1] - 2), 14,
                           outline=BORDER, width=2)
    return image, draw


def save_loop(name, frames, durations, still):
    # One shared palette prevents color flicker between frames.
    palette = still.quantize(colors=128)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE)
               for frame in frames]
    indexed[0].save(ASSETS / f"{name}.gif", save_all=True,
                    append_images=indexed[1:], duration=durations,
                    loop=0, optimize=False, disposal=1)
    still.save(ASSETS / f"{name}-static.png")


def typing_intro():
    lines = ["Building full-stack web apps.",
             "Connecting AI agents to useful tools.",
             "Turning documents into cited answers.",
             "At home in the Linux terminal."]
    frames, durations = [], []

    def render(text, cursor=True):
        image, draw = card((800, 108))
        draw.text((24, 16), "yousaf@github  ~/building", font=font(15), fill=MUTED)
        draw.text((24, 53), ">", font=font(24), fill=GREEN)
        draw.text((54, 53), text, font=font(24), fill=TEXT)
        # Keep both accent colors in the shared GIF palette.
        draw.ellipse((754, 21, 762, 29), fill=PURPLE)
        if cursor:
            x = 56 + draw.textlength(text, font=font(24))
            draw.rectangle((x, 56, x + 11, 80), fill=GREEN)
        return image

    for line in lines:
        for count in range(len(line) + 1):
            frames.append(render(line[:count]))
            durations.append(65)
        for cursor in (True, False, True, False):
            frames.append(render(line, cursor))
            durations.append(400)
        for count in range(len(line) - 1, -1, -2):
            frames.append(render(line[:count]))
            durations.append(35)
    save_loop("typing-intro", frames, durations, render(lines[0], False))


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    typing_intro()
    print("Generated the typing intro with a static alternative.")
