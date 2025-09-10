# find_all_keywords

## Purpose

This utility scans all Markdown files in your Obsidian vault to extract keywords listed under the `## Keywords` heading.

In my workflow, I use a custom GPT called [**Find Keywords**](https://chatgpt.com/g/g-mL985wIE7-find-keywords) to generate keyword suggestions for individual notes. After generating the list, I paste those into a `## Keywords` section at the bottom of the note. This script then crawls the vault to find all such entries, deduplicates them, and outputs them in a new Markdown file.

If you use a different method to collect or organize keywords, this script will still work — as long as the keywords are placed under a `## Keywords` heading and use `[[wikilink]]` syntax.

When the script runs, you will be prompted to choose one of three output formats:

1. **Plain text keywords** – for reviewing or exporting into other systems  
2. **Wikilinks (`[[Keyword]]`)** – suitable for pasting into Obsidian topic maps or MOCs  
3. **Wikilinks with ✅ checkmarks** – adds a ✅ if the keyword already exists as a `.md` file in your vault  



## Usage

1. Run the script:
    ```bash
    python find_all_keywords.py
    ```

2. When prompted, select the output format:

   ```
   Select output format:
   1. Plain text keywords
   2. Wikilinks (e.g., [[LMS]])
   3. Wikilinks with ✅ checkmarks for keywords that exist as files
   ```

3. The script will:

   * Search your entire Obsidian vault (or the folder you specify)
   * Locate `## Keywords` sections in each Markdown file
   * Parse all `[[keyword]]` entries
   * Normalize and deduplicate them
   * Output the result to a Markdown file in the **root of your vault** with today’s date

4. Example file name:

   ```
   2025-09-10 - Extracted Keywords.md
   ```

## Example Output

**If you selected Option 3 (wikilinks with checkmarks):**

```markdown
---
created: 2025-09-10
tags: [Keywords]
description: Extracted list of unique keywords under ## Keywords headings across vault.
---

[[APIs]] ✅
[[ChatGPT]] ✅
[[Learning Management System]]
[[LMS]]
[[Parsing Techniques]] ✅
[[Prompt Engineering]]
[[Python]] ✅
```

## Notes

* Vault path can be hard-coded at the top of the script, or left blank to be prompted.
* Only `[[wikilinks]]` are extracted — plain text or other formats are ignored.
* Aliases (`[[path/to/file|Name]]`) and nested paths are stripped, and only the keyword is retained.
* The checkmark (✅) is only shown if a `Keyword.md` file exists somewhere in the vault.

## Planned Improvements (Future Ideas)

* Add output grouping by originating file
* Include usage frequency count for each keyword
* Allow custom heading besides `## Keywords`

If you'd like to see any of these features implemented, please open an issue in this repository.

---

*Last updated: 2025-09-10*
