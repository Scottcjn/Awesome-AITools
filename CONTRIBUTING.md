# Contributing to Awesome AI Tools

Thanks for helping improve Awesome AI Tools. This repository is a curated list
of AI tools, agents, models, cloud platforms, writing aids, media tools, and
related documentation, so contributions should keep the catalog useful,
accurate, and easy to scan.

## What to Contribute

Good contributions include:

- AI tools with a stable product page, GitHub repository, or documentation page.
- Open source AI agents, model tools, coding assistants, media generators,
  evaluation tools, or deployment platforms.
- Clear updates to descriptions, pricing labels, links, stars badges, or related
  docs pages under `docs/`.
- Broken-link fixes and cleanup for stale or renamed tools.
- Improvements that keep `README.md` and `README-CN.md` consistent where the
  change affects both language versions.

Avoid adding unrelated products, pure ads, tracking links, duplicate tools, or
entries without enough public information for readers to evaluate the tool.

## Before Opening a Pull Request

1. Search `README.md`, `README-CN.md`, and `docs/` for the tool name and URL.
2. Check whether the tool belongs in an existing category from the table of
   contents.
3. Use the recommendation template linked from the README issue reference when
   proposing a new tool.
4. Keep descriptions factual and concise.
5. Update both English and Chinese docs when the existing content is mirrored.

If you are unsure where a tool belongs, open an issue first and include the tool
URL, category, pricing model, and why it fits the list.

## Entry Style

- Keep the existing Markdown table format: `Name`, `Description`, `Links`, and
  `Fees`.
- Use canonical URLs and GitHub repository links where available.
- Include a GitHub stars badge for open source repositories when nearby entries
  use one.
- Use `Free`, `Paid`, `Free/Paid`, `Free Trial`, or a similarly short fees label
  that matches surrounding entries.
- Keep category headings and table-of-contents links in sync.
- Avoid long promotional copy; summarize the practical value of the tool.

Example:

```markdown
| Example Tool | Open-source AI workflow tool for local model evaluation. | [Github](https://github.com/example/tool) | Free |
```

## Local Checks

Run the formatting helper if you touch the main READMEs:

```bash
python3 scripts/format_readmes.py
```

Run whitespace validation before committing:

```bash
git diff --check
```

The repository also has a GitHub Actions link-check workflow using Lychee for
Markdown files. For changed links, manually verify the URLs when practical and
mention any link that cannot be checked locally.

## Pull Request Checklist

- The tool or resource is not already listed.
- The entry is in the best matching category.
- English and Chinese versions are updated when appropriate.
- New or changed links resolve to the intended pages.
- Table formatting still matches nearby rows.
- `python3 scripts/format_readmes.py` was run if the main READMEs changed.
- `git diff --check` passes.

Small, focused pull requests are easiest to review. Submit unrelated tool
additions, link fixes, and category reorganizations separately when possible.
