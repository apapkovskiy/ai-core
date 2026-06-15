---
name: add_movie
description: Add a movie entry to the Notion Media database with enriched metadata. Use when the user asks to add a film/movie to Media, fill Notion movie properties, attach trailer and artwork links, include Russian plot/Wikipedia links, or set Score/5 from Kinopoisk rating.
---

# Add movie to Notion Media

Add the provided movie as a page in the Notion `Media` database and fill core properties consistently.

Use the Notion MCP server for all Notion read/write operations with this skill.

## Required outputs

For each movie, do all of the following:

1. Create the movie page in `Media`.
2. Find an official (or best available) YouTube trailer, preferable in Russian, and set it in the `Link` property.
3. Add a brief plot summary, preferably in Russian.
4. Find thumbnail, if you can set it as a page cover set it,
   if not then add the link to the image to the page.
5. Add Russian Wikipedia link when available, with visible link text exactly `Wikipedia` to the brief plot summary.
6. Set `Score/5` based on Kinopoisk rating.
7. Identify the film's genre. It can be based on metadata or plot description.
   It should be one or more of the following tags: `action`, `adventure`, `animation`, `biography`, `comedy`, `crime`, `documentary`, `drama`, `family`, `fantasy`, `film-noir`, `history`, `horror`, `mystery`, `Sci-Fi`, `thriller`, `war`, `ww2`, `western`, `arthause`.
8. Set page's icon to 🎬.

## Property mapping

- `Name` (title): movie title (localized title if user gave one; otherwise original title).
- `Link`: YouTube trailer URL.
- `Score/5`: converted from Kinopoisk score using the conversion rule below.
- `Summary`: Short Russian synopsis (2-4 sentences) plus link to `ru.wikipedia.org` page if found with visible link text exactly `Wikipedia`.
- `Tag`: genre(s) of the film, if identifiable from metadata or plot.
- `Release date`: release date if available from metadata.
- Thumbnail:
  - If page cover can be set via current tool/API, set it directly.
  - Otherwise, add the direct image URL in the page body under `Poster:` so user can set cover manually.

## Kinopoisk score conversion

Use Kinopoisk rating on a 10-point scale and convert to `Score/5`:

- Formula: `score_5 = round(score_10 / 2, 1)`
- If `Score/5` property only accepts integers, round to nearest integer.
- If Kinopoisk rating is unavailable, leave `Score/5` empty and note `Kinopoisk rating not found` in the page body.

Helper script for deterministic conversion:

- `scripts/normalize_score.py <score_10>` -> decimal score for `Score/5`
- `scripts/normalize_score.py <score_10> --integer-only` -> integer score

## Source selection rules

- Trailer priority:
  1. In Russian language if available, otherwise in English.
  2. Use 'Русский трейлер' in search queries to prioritize Russian trailers.
  3. High-quality widely viewed trailer from a reputable channel.

- Poster/thumbnail priority:
  1. Official poster (studio/distributor/official movie site).
  2. Reputable movie databases or press kits.
  3. Fallback to high-quality image with clear attribution via source URL.

- Wikipedia:
  - Prefer Russian page on `ru.wikipedia.org`.
  - If no Russian page exists, add no Wikipedia link unless user explicitly wants non-Russian fallback.

## Quality checks before finishing

- Ensure `Link` is YouTube and points to trailer content (not review or recap).
- Ensure plot text is concise and in Russian unless unavailable.
- Ensure Wikipedia link text is exactly `Wikipedia`.
- Ensure `Score/5` is consistent with latest Kinopoisk rating found.
- Ensure poster is either set as cover or included as a direct URL in page body.

## Output style when reporting completion

Return a short confirmation including:

- Movie added (title).
- Trailer URL used.
- Kinopoisk rating and computed `Score/5`.
- Whether cover was set directly or poster URL was added.
- Wikipedia status (added/not found).
