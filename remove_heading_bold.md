# remove_heading_bold

## Purpose

When clipping content from the web using the Obsidian Web Clipper, it’s common for headings to be formatted with both heading markers (like `###`) and bold markdown (`**`). For example:

```markdown
### **What’s Jailbreaking?**
```

This results in visually redundant formatting in Obsidian, where the heading is already bolded by the theme. This utility cleans up the file by removing the bold formatting from all markdown headings, while preserving the heading level and text.

## Usage

1. Run the script from the command line:

```bash
python remove_heading_bold.py
```

2. You will be prompted to enter the full path to the Markdown file you want to clean up.

3. The script will:

   * Read the file
   * Remove `**` formatting from any headings (lines starting with one or more `#` followed by `**`)
   * Overwrite the file with the cleaned-up version

4. If no changes are detected, it will inform you that no edits were necessary.

## Example

### Before

```text
## **Introduction**
### **What’s Jailbreaking?**
```

### After

```text
## Introduction
### What’s Jailbreaking?
```

## Notes

* Only affects bold inside headings.
* Other bold text elsewhere in the document remains unchanged.
* The file is updated **in-place**.
* Currently supports UTF-8 encoded Markdown files.

## Planned Improvements (Future Ideas)

* Add `--dry-run` mode to preview changes without overwriting.
* Optionally back up the original file before modifying.
* Allow batch processing of all `.md` files in a folder.

If you'd like to see any of these features implemented, please open an issue in this repository.

---

*Last updated: 2025-09-10*
