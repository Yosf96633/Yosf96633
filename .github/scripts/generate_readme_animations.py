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
CYAN = "#64D8E8"


def font(size):
    return ImageFont.truetype(FONT_PATH, size)


def bold_font(size):
    return ImageFont.truetype(FONT_PATH.replace("SansMono.ttf", "SansMono-Bold.ttf"), size)


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
    lines = ["Building a shell in C++20.",
             "Designing agents with explicit state.",
             "Grounding answers in cited sources.",
             "Shipping useful tools on Linux."]
    frames, durations = [], []

    def render(text, cursor=True):
        image, draw = card((800, 108))
        draw.text((24, 16), "yousaf@github  ~/building", font=font(15), fill=MUTED)
        draw.text((24, 53), ">", font=font(24), fill=GREEN)
        draw.text((54, 53), text, font=font(24), fill=TEXT)
        # Keep both accent colors in the shared GIF palette.
        draw.ellipse((754, 21, 762, 29), fill=CYAN)
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


def save_gif(name, frames, durations):
    palette = frames[0].quantize(colors=128)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE)
               for frame in frames]
    indexed[0].save(ASSETS / f"{name}.gif", save_all=True,
                    append_images=indexed[1:], duration=durations,
                    loop=0, optimize=False, disposal=1)


def terminal_header(mobile=False):
    width, height = (480, 474) if mobile else (960, 370)

    def render(cursor, signal):
        image, draw = card((width, height))
        draw.line((1, 49, width - 1, 49), fill=BORDER)
        for x, color in ((28, CYAN), (48, "#F5A623"), (68, GREEN)):
            draw.ellipse((x - 5, 20, x + 5, 30), fill=color)
        draw.text((102, 18), "yousaf@linux: ~ / profile", font=font(13), fill=MUTED)
        draw.text((28, 65), "$ ./myShell --interactive", font=font(16), fill=GREEN)

        if mobile:
            draw.text((28, 96), "MUHAMMAD", font=bold_font(38), fill=TEXT)
            draw.text((28, 143), "YOUSAF", font=bold_font(38), fill=TEXT)
            draw.text((28, 194), "Linux Systems + Agentic AI", font=font(20), fill=CYAN)
            divider, row_y, text_size = 238, (252, 283, 314, 345), 16
        else:
            draw.text((28, 96), "MUHAMMAD", font=bold_font(48), fill=TEXT)
            draw.text((306, 96), "YOUSAF", font=bold_font(48), fill=TEXT)
            draw.text((28, 146), "Linux Systems + Agentic AI", font=font(24), fill=CYAN)
            divider, row_y, text_size = 193, (207, 238, 269, 300), 17
        draw.line((28, divider, width - 28, divider), fill=BORDER)
        rows = (("OS", "Linux / processes / terminals"),
                ("SHELL", "C++20 / POSIX / job control"),
                ("AGENTS", "LangGraph / RAG / tools"),
                ("WEB", "Next.js / FastAPI / TypeScript"))
        for y, (label, value) in zip(row_y, rows):
            draw.text((28, y), label, font=font(14), fill=MUTED)
            draw.text((104, y - 3), value, font=font(text_size), fill=TEXT)

        if mobile:
            draw.text((28, 391), "PARSE -> EXECUTE", font=font(15), fill=GREEN)
            draw.text((236, 391), "REASON -> ACT", font=font(15), fill=CYAN)
            status_y, cursor_box = 435, (440, 433, 451, 451)
        else:
            draw.line((615, 216, 615, 330), fill=BORDER)
            draw.text((647, 219), "PARSE -> EXECUTE", font=font(18), fill=GREEN)
            draw.text((647, 251), "REASON -> ACT", font=font(18), fill=CYAN)
            draw.text((647, 301), "systems / agents / web", font=font(14), fill=MUTED)
            status_y, cursor_box = 331, (920, 329, 931, 347)
        if signal:
            draw.ellipse((30, status_y + 6, 38, status_y + 14), fill=GREEN)
        draw.text((47, status_y), "ready for input", font=font(12), fill=MUTED)
        if cursor:
            draw.rectangle(cursor_box, fill=GREEN)
        return image

    frames = [render(cursor, signal) for cursor, signal in
              ((True, True), (True, False), (False, False), (True, True))]
    save_gif("terminal-mobile" if mobile else "terminal-header", frames,
             [600, 350, 350, 600])


def footer():
    def render(cursor):
        image, draw = card((480, 92))
        draw.text((25, 20), "$ ./contact --human", font=font(18), fill=GREEN)
        draw.text((25, 51), "Connection kept alive.", font=font(14), fill=MUTED)
        if cursor:
            draw.rectangle((257, 53, 267, 71), fill=CYAN)
        return image

    save_gif("footer", [render(True), render(False)], [700, 350])


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    typing_intro()
    terminal_header()
    terminal_header(mobile=True)
    footer()
    print("Generated terminal and typing animations with a static typing alternative.")
