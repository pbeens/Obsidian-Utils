
# find_stuff_to_process

## Purpose

This utility is designed to help you review all the content you've captured in your **Daily Notes** under a specific section: `## Stuff to Process`.

In your daily note template, you include a level-2 heading titled `## Stuff to Process` at the bottom of the page. This section is used as a catch-all for incoming items — especially when you're sharing content from your mobile device using the Obsidian app. On mobile, when you choose to share a URL or text snippet into Obsidian, you usually direct it to the current daily note. The shared content gets appended to the bottom of that note, and by convention, ends up underneath the `## Stuff to Process` heading.

This script scans all your daily notes to identify which ones still contain unprocessed items in that section — helping you clean up, triage, or move them elsewhere.


## Usage

1. Open a terminal and run:
    ```bash
    python find_stuff_to_process.py
    ```
2. By default, the script uses this path:

   ```
   D:\My Documents\Obsidian\Obsidian-Notes\Daily Notes
   ```
3. You can manually edit the script to change the `daily_notes_path` variable, or leave it blank to be prompted at runtime.
4. The script will:

   * Read every `.md` file in that folder
   * Look for `## Stuff to Process`
   * Print any remaining content under that heading

## Example Output

```
2025-09-10.md:
  - https://example.com/great-article
  - [[Follow up on GitHub repo]]

2025-09-08.md:
  - Book: Smart Notes – chapter 4
```

## Notes

* Headings must be exactly `## Stuff to Process` (case-sensitive).
* Content ends at the next level-2 heading (`##`) or at the end of the file.
* Blank lines are ignored.

## Planned Improvements (Future Ideas)

* Output results to a Markdown report
* * Add a configurable `heading_to_search_for` variable so users can define a custom heading instead of relying on "## Stuff to Process"


If you'd like to see any of these features implemented, please open an issue in this repository.

---

*Last updated: 2025-09-10*
