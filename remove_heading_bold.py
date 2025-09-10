"""
remove_heading_bold.py

Removes bold markdown formatting from headings in an Obsidian note.
This is useful when web clipping results in headings like `### **Heading**`.

Filename will be prompted at runtime.
"""

import re
from pathlib import Path

# Leave blank to force prompt
file_path = ""

def get_input_file():
    global file_path
    if not file_path:
        file_path = input("Enter the path to the Markdown file: ").strip()
    return Path(file_path).expanduser().resolve()

def remove_bold_from_headings(text):
    # Regex: Look for markdown headings (e.g., ###) followed by bold (**text**)
    heading_regex = re.compile(r'^(#+\s+)\*\*(.+?)\*\*$', re.MULTILINE)
    return heading_regex.sub(r'\1\2', text)

def main():
    path = get_input_file()
    if not path.exists() or not path.is_file():
        print(f"❌ File not found: {path}")
        return

    content = path.read_text(encoding="utf-8")
    updated = remove_bold_from_headings(content)

    if content != updated:
        path.write_text(updated, encoding="utf-8")
        print(f"✅ Bold formatting removed from headings in: {path.name}")
    else:
        print("ℹ️ No changes made — no bold headings found.")

if __name__ == "__main__":
    main()
