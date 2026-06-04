from pathlib import Path
import re

icons_folder = Path("icons")

for svg_file in icons_folder.glob("*.svg"):
    text = svg_file.read_text(encoding="utf-8")

    # Replace existing fill values like fill="#000000" or fill="black"
    text = re.sub(r'fill="[^"]*"', 'fill="white"', text)

    # If there was no fill attribute at all, add one to the opening <svg> tag
    if 'fill="white"' not in text:
        text = text.replace("<svg", '<svg fill="white"', 1)

    svg_file.write_text(text, encoding="utf-8")

    print(f"Updated {svg_file}")