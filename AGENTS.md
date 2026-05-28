# Project Agent Rules

## Scope

- These rules apply to the `ai-core` workspace.
- Keep changes focused on local agent/skill assets under `.agents/` unless explicitly asked otherwise.

## Repo Map

- `.agents/`
  - `skills/`
    - `notion/`
      - `add_movie/`
        - `SKILL.md`
        - `scripts/normalize_score.py`

## Skill Authoring Defaults

- Create skills under `.agents/skills/<domain>/<skill-name>/`.
- Every skill must include `SKILL.md` with YAML frontmatter containing only:
  - `name`
  - `description`
- Keep SKILL instructions concise and action-oriented.
- Put reusable helpers in `scripts/`, long reference material in `references/`, and output resources in `assets/`.
- Do not add extra documentation files (README, changelog, install guides) unless explicitly requested.

## Editing and Validation

- Prefer the smallest safe change.
- Preserve existing structure and naming conventions.
- When adding scripts, run a representative execution test and report the command and result.
- If a packaging/validation script exists in this repo, use it before finalizing.

## Safety

- Never read or expose secrets/credentials/PII.
- Treat `.env*`, key/token files, and credential-like paths as sensitive.
- If sensitive data is encountered accidentally, stop and report exposure without quoting secret values.

## Response Style

- Be concise and practical.
- Report changed file paths explicitly.
- Include short next steps only when useful.
