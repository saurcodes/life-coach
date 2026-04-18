# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A Claude Code plugin that provides structured life coaching. It is not a software application — there is no build step, no test suite, no dependencies. All files are markdown (coaching logic) and one Python utility script.

## Plugin Structure

The plugin name is `life-coach` (defined in `.claude-plugin/plugin.json`). Claude Code discovers it via:

```bash
claude --plugin-dir /path/to/life-coach-skills
```

Two types of content coexist:

**External slash commands** (`commands/*.md`) — each file becomes `/life-coach:<filename>` in Claude Code. These are thin wrappers that invoke the main skill.

**The skill** (`skills/life-coach/`) — the coaching brain. `SKILL.md` is the orchestrator. It routes to `command-handlers/`, `references/`, and `hooks/` on demand. Never load all reference files at once — only load what the current moment requires.

## Key Files to Understand Before Editing

- `skills/life-coach/SKILL.md` — the orchestrator. Contains the 7-phase session framework, Q+O rhythm, hook routing table, and mode definitions. Most behavioral changes happen here.
- `skills/life-coach/references/wisdom-library.md` — 40+ teachings organized by block type. Each entry has: teaching, modern translation, deploy-as script, follow-up question. All four fields are required.
- `skills/life-coach/references/exercise-library.md` — 25 exercises. Each entry requires: name, best-for, time, archetype fit, full script, debrief question. Never add a summary — the full script is what makes it usable.
- `skills/life-coach/command-handlers/` — internal logic loaded by the orchestrator when a command fires. Not the same as `commands/` (external).

## Editing Guidelines

**Adding a wisdom teaching**: Add to `wisdom-library.md` under the correct block-type section. Must include `Deploy as:` language and `Follow-up:` question. Must cite a real tradition and source text.

**Adding an exercise**: Add to `exercise-library.md`. Full script required — no summaries.

**Adding an external command**: Create `commands/<name>.md` with frontmatter `description` and a one-line instruction to invoke `life-coach:life-coach` and execute the relevant command handler.

**Changing session flow**: Edit `skills/life-coach/SKILL.md`. The Q+O rhythm, phase sequence, hook routing table, and mode behaviors are all there.

**Changing a command's behavior**: Edit the relevant file in `skills/life-coach/command-handlers/`, not `commands/`.

## Session Logging Script

`skills/life-coach/scripts/log_session.py` — Python 3, no dependencies. Run directly:

```bash
python3 skills/life-coach/scripts/log_session.py --interactive
python3 skills/life-coach/scripts/log_session.py --client <id> --session <n> --data '<json>'
```

Saves snapshots to `~/.claude/life-coach/sessions/<client_id>/`.

## What Not to Change

`skills/life-coach/references/crisis-protocol.md` — do not edit without careful review. Open an issue first.

The `description` field in `skills/life-coach/SKILL.md` frontmatter controls when Claude auto-triggers the skill. Changes here affect activation behavior across all conversations.
