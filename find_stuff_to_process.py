"""
find_stuff_to_process.py

Scans daily notes in your Obsidian vault and reports all files that still contain
content under the "## Stuff to Process" heading.

Default folder path is set to the Daily Notes folder. You may:
- Leave it as-is (ideal for personal use)
- Manually change the `daily_notes_path` variable
- Leave it blank to be prompted at runtime
"""

from pathlib import Path
import sys

# Default path to Daily Notes folder (can be changed by user)
daily_notes_path = r"D:\My Documents\Obsidian\Obsidian-Notes\Daily Notes"

def get_notes_path():
    global daily_notes_path
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).expanduser().resolve()
    if not daily_notes_path:
        daily_notes_path = input("Enter your Daily Notes folder path: ").strip()
    return Path(daily_notes_path).expanduser().resolve()

def extract_stuff_to_process(text):
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Stuff to Process":
            start = i + 1
            break
    if start is None:
        return []

    block = []
    for line in lines[start:]:
        if line.strip().startswith("## "):  # Stop at next level-2 heading
            break
        if line.strip():  # Skip blank lines
            block.append(line.strip())
    return block

def main():
    path = get_notes_path()
    if not path.exists() or not path.is_dir():
        print(f"❌ Folder not found: {path}")
        return

    matches = {}
    for file in sorted(path.glob("*.md")):
        text = file.read_text(encoding="utf-8")
        items = extract_stuff_to_process(text)
        if items:
            matches[file.name] = items

    if not matches:
        print("✅ No remaining items under '## Stuff to Process' in any file.")
    else:
        print("\n📋 Items still under '## Stuff to Process':\n")
        for filename, items in matches.items():
            print(f"{filename}:")
            for item in items:
                print(f"  - {item}")
            print()

if __name__ == "__main__":
    main()
