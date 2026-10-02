"""Give additional SVG logos contrast tiles without altering their artwork."""

from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1] / "assets" / "stack"
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)

NAMES = ["c", "websockets", "github", "html5", "css3", "php", "laravel",
         "mysql", "cmake", "sqlite", "socketio", "openai", "groq", "resend", "cloudinary"]


def main():
    for name in NAMES:
        path = ROOT / f"{name}.svg"
        source = ET.parse(path).getroot()
        if source.get("data-contrast-tile") == "true":
            continue
        if "viewBox" not in source.attrib:
            source.set("viewBox", f'0 0 {source.get("width", "24")} {source.get("height", "24")}')
        source.set("x", "7")
        source.set("y", "7")
        source.set("width", "34")
        source.set("height", "34")
        source.set("preserveAspectRatio", "xMidYMid meet")
        outer = ET.Element(f"{{{SVG_NS}}}svg", {"width": "48", "height": "48",
                          "viewBox": "0 0 48 48", "data-contrast-tile": "true"})
        ET.SubElement(outer, f"{{{SVG_NS}}}rect", {"width": "48", "height": "48",
                      "rx": "8", "fill": "#191422" if name == "github" else "#ffffff"})
        outer.append(source)
        ET.ElementTree(outer).write(path, encoding="unicode")
    print("Prepared 15 additional SVG logos with contrast tiles; original marks and colors retained.")


if __name__ == "__main__":
    main()
