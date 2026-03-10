---
layout: page
title: About
permalink: /about/
---

This is a personal blog built with Jekyll and hosted on GitHub Pages.

The theme uses IBM Plex Mono for headings and interface elements, paired with IBM Plex Serif for body text. It supports dark mode automatically via `prefers-color-scheme`.

## Writing a post

Create a new file in `_posts/` with the naming convention `YYYY-MM-DD-your-title.md`. Add front matter at the top:

```yaml
---
title: Your Post Title
tag: Topic
lede: A one-sentence summary that appears as a styled introduction.
---
```

The `tag` and `lede` fields are optional. If no `lede` is provided, the post excerpt is used on the listing page.

## Customization

Edit `_config.yml` to set your site title, description, and author. Colors and fonts live in `assets/css/style.css` as CSS custom properties — swap them to make the theme your own.
