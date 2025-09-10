# Obsidian Utils

A collection of small, practical utilities for Obsidian users. These tools were originally created for personal use, but may be useful to others looking to streamline workflows, automate note tasks, or enhance plugin-based functionality.

Each utility is designed to be minimal, direct, and easy to modify.

## 🗂 Directory Structure

```
obsidian-utils/
│
├── \[utility\_name].py        # Python script for the utility
├── \[utility\_name].md        # Markdown doc describing the utility
├── TEMPLATE.md                # Standard format for utility documentation
├── .gitignore                 # Python-based defaults
└── LICENSE                    # MIT License
```

## 🧰 Available Utilities

| Script | Description |
|--------|-------------|
| [`remove_heading_bold.py`](remove_heading_bold.md) | Removes bold formatting from Markdown headings (e.g. converts `### **Title**` to `### Title`) in a selected file. |
| [`find_stuff_to_process.py`](find_stuff_to_process.md) | Scans all Daily Notes and lists entries that remain under the `## Stuff to Process` heading. This is especially useful if you regularly share URLs or content into Obsidian from your **mobile device**, since those shared items are typically appended to the bottom of the Daily Note under this heading (for me) as part of your daily note template. |
| [`find_all_keywords.py`](find_all_keywords.md) | Collects all keywords found under `## Keywords` headings in your vault. Outputs a deduplicated list in plain text, as wikilinks, or as wikilinks with ✅ checkmarks for keywords that already exist as `.md` files. Saves the result in a dated Markdown file in the root of your vault.



## 📄 License

This repository is licensed under the [MIT License](LICENSE).

## 🙋‍♂️ Contributing

If you’d like to suggest an improvement, report a bug, or request a new feature, please open an issue in this repository.

---

_Last updated: 2025-09-10_