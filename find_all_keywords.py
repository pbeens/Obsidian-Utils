"""
find_all_keywords.py

Scans all Markdown files in your Obsidian vault and collects all [[keywords]] found
under the `## Keywords` heading. Outputs them in alphabetical order to a Markdown file
in the vault root. Supports three output modes:
1. Plain text
2. Wikilinks
3. Wikilinks with ✅ checkmarks for keywords that exist as files
"""

from pathlib import Path
import sys
import re
from datetime import datetime

# Default vault path (change as needed)
vault_path = r"D:\My Documents\Obsidian\Obsidian-Notes"

def get_vault_path():
    global vault_path
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).expanduser().resolve()
    if not vault_path:
        vault_path = input("Enter your Obsidian vault path: ").strip()
    return Path(vault_path).expanduser().resolve()

def extract_keywords_from_text(text):
    lines = text.splitlines()
    keywords = set()
    in_keywords_section = False

    for line in lines:
        if line.strip() == "## Keywords":
            in_keywords_section = True
            continue
        if in_keywords_section:
            if line.strip().startswith("## "):
                break
            matches = re.findall(r"\[\[([^\[\]]+)\]\]", line)
            for match in matches:
                # Clean up: strip path and alias
                keyword = match.split("|")[-1].split("/")[-1].strip()
                if keyword:
                    keywords.add(keyword)
    return keywords

def find_existing_note_names(path):
    return {file.stem.strip() for file in path.rglob("*.md")}

def get_output_mode():
    print("\nSelect output format:")
    print("1. Plain text keywords")
    print("2. Wikilinks (e.g., [[LMS]])")
    print("3. Wikilinks with ✅ checkmarks for keywords that exist as files")
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in {"1", "2", "3"}:
            return int(choice)
        print("Invalid input. Please enter 1, 2, or 3.")

def main():
    path = get_vault_path()
    if not path.exists() or not path.is_dir():
        print(f"❌ Folder not found: {path}")
        return

    all_keywords = set()

    for file in path.rglob("*.md"):
        try:
            text = file.read_text(encoding="utf-8")
            all_keywords.update(extract_keywords_from_text(text))
        except Exception as e:
            print(f"⚠️ Skipped {file.name}: {e}")

    if not all_keywords:
        print("✅ No keywords found under '## Keywords' in any files.")
        return

    sorted_keywords = sorted(all_keywords, key=str.casefold)
    output_mode = get_output_mode()
    existing_note_names = find_existing_note_names(path) if output_mode == 3 else set()

    today = datetime.now().strftime("%Y-%m-%d")
    output_file = path / f"{today} - Extracted Keywords.md"

    # YAML frontmatter
    yaml = f"""---
created: {today}
tags: [Keywords]
description: Extracted list of unique keywords under ## Keywords headings across vault.
---
"""

    # Format based on output mode
    body_lines = []
    for kw in sorted_keywords:
        if output_mode == 1:
            body_lines.append(kw)
        elif output_mode == 2:
            body_lines.append(f"[[{kw}]]")
        elif output_mode == 3:
            check = " ✅" if kw in existing_note_names else ""
            body_lines.append(f"[[{kw}]]{check}")

    full_output = f"{yaml}\n" + "\n".join(body_lines)
    output_file.write_text(full_output, encoding="utf-8")
    print(f"\n✅ Keywords saved to: {output_file}")

if __name__ == "__main__":
    main()
