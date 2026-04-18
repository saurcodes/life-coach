# Life Coach — Claude Code Plugin

A structured life coaching plugin that bridges ancient wisdom — Bhagavad Gita, Upanishads, Tao Te Ching, Buddhism, Chanakya's Arthashastra — with modern psychology. Built for people navigating real challenges: career crossroads, identity confusion, burnout, purpose loss, relationship stress, or simply feeling stuck.

---

## What It's Like

The coaching adapts to how you think. It asks one question at a time, listens to what you actually say, and offers back an observation, a named pattern, or a teaching from ancient tradition — not because it's scheduled, but because what you just said called for it.

Sessions follow a natural arc: surface the real problem (which is rarely the presenting problem), diagnose the root block, deliver one teaching that fits the moment, assign one exercise with a real deadline, and close with a specific commitment you'll be held to next time.

It also watches for things you don't name: when you push back on something that landed, when you've returned to the same point three times, when the emotion in a response shifts unexpectedly. These conditions trigger automatic responses — not interruptions, but redirections that keep the session honest.

---

## Installation

### Claude Code (CLI & Desktop)

```
/plugin marketplace add saurcodes/life-coach
/plugin install life-coach@life-coach
/reload-plugins
```

Commands are now available as `/life-coach:start`, `/life-coach:wisdom`, etc.

To uninstall: `/plugin uninstall life-coach@life-coach`

---

### Claude.ai

1. Download this repo as a ZIP (GitHub → Code → Download ZIP)
2. In Claude.ai, go to **Customize → Skills → + → Upload a skill**
3. Upload the ZIP

The skill activates automatically when the conversation calls for it.

---

### Development (without installing)

```bash
claude --plugin-dir /path/to/life-coach-skills
```

---

## Commands

| Command | What it does |
|---|---|
| `/life-coach:start` | Begin a session — checks for prior sessions first |
| `/life-coach:recap` | Structured summary of where the session stands |
| `/life-coach:close` | Close with insights, action items, and a challenge |
| `/life-coach:snapshot` | Save a record without closing |
| `/life-coach:diagnose` | Full root cause assessment |
| `/life-coach:reframe` | Fresh angle — pattern interrupt |
| `/life-coach:archetype` | See how the coach is reading and adapting to you |
| `/life-coach:wisdom [theme]` | Ancient teaching matched to your situation |
| `/life-coach:exercise [topic]` | Targeted exercise with full instructions |
| `/life-coach:challenge` | 48–72 hour micro-challenge |
| `/life-coach:checkin` | Accountability review from your last session |
| `/life-coach:progress` | Map the full arc of your coaching journey |
| `/life-coach:pattern` | Name a recurring pattern explicitly |
| `/life-coach:deepwork` | Higher intensity mode — compressed phases, harder push |
| `/life-coach:maintenance` | Integration mode — periodic check-in, no new diagnosis |

Commands also work as plain text intent: *"let's close the session"* triggers `/close`.

---

## Example Session

```
You:    I keep trying to change careers but never actually do it.
        I've been "almost ready" for two years.

Coach:  Two years of "almost ready" — that's a long time to be at
        the edge of something. Before we look at what's stopping
        you, I'm curious: if you knew the new career would work out
        perfectly — would you make the move tomorrow?

You:    Yes, instantly.

Coach:  So the question isn't whether you want it. You know what
        you want. The Gita calls this the real test — not desire,
        but the attachment to outcome that freezes action. What's
        the worst realistic failure you're actually afraid of?

You:    That I'll try, fail publicly, and prove everyone right
        who said I wasn't cut out for it.

Coach:  That's a Courage block with a specific shape: the fear isn't
        failure itself — it's being seen failing. Those are very
        different things, and they need different answers. What
        would "failing privately" look like — a version where you
        try and it doesn't work, but no one important finds out?
```

---

## How Wisdom Works

Ancient teachings appear in two ways:

**Wisdom seeds** — a single sentence or image dropped mid-conversation when what you just said genuinely calls for it. Not explained, not defended. If it opens something, the thread follows. If it doesn't land, it's released without ceremony.

**Full teachings** — one per session, matched to the diagnosed block. Wrapped in story, connected directly to your situation. Always followed by *"How does that land?"* — because a teaching that doesn't resonate gets released, never defended.

Traditions drawn from: Bhagavad Gita, Upanishads, Tao Te Ching, Buddhism (Theravada and Zen), Chanakya's Arthashastra, Vedic mythology, Japanese philosophy (Ikigai, Kintsugi).

---

## Session Continuity

At session close, a snapshot is saved — core challenge, root diagnosis, archetype, commitments made, and the exact accountability question to open the next session with.

```bash
# Logs automatically on /close, or run manually:
python3 skills/life-coach/scripts/log_session.py --interactive
```

Snapshots are stored in `~/.claude/life-coach/sessions/<client_id>/` and loaded when a returning session starts.

---

## Plugin Structure

```
life-coach/
├── .claude-plugin/
│   ├── plugin.json              # Plugin manifest
│   └── marketplace.json         # Marketplace catalog
├── SKILL.md                     # Root copy for Claude.ai ZIP upload
├── commands/                    # External slash commands (/life-coach:*)
├── skills/life-coach/           # Plugin skill (Claude Code)
│   ├── SKILL.md                 # Orchestrator — session flow & routing
│   ├── command-handlers/        # Internal logic per command group
│   ├── references/              # Load-on-demand: archetypes, wisdom, exercises...
│   ├── hooks/                   # Auto-firing condition hooks
│   └── scripts/                 # log_session.py
```

`SKILL.md` is the conductor. Reference files load only when the moment requires them — never all at once. Commands give direct control. Hooks fire automatically on detected conditions.

---

## Contributing

Contributions welcome. The most valuable additions are exercises and wisdom teachings grounded in real situations.

**Adding a wisdom teaching** — add to `skills/life-coach/references/wisdom-library.md` under the appropriate tradition section. Required fields:
- `Teaching` — the original story or concept
- `Modern translation` — what it means for someone alive today
- `The angle` — one sentence: what specific human truth this illuminates
- `Best when` — the situations where it fits, loosely across block types
- Must be grounded in a real tradition with a citable source. No invented parables.

**Adding an exercise** — add to `skills/life-coach/references/exercise-library.md`. Required fields: name, best-for, time required, archetype fit, full script, what to bring back, debrief question. No summaries — the full script is what makes it usable.

**Changing session flow** — edit `skills/life-coach/SKILL.md`. The Q+O rhythm, phase sequence, hook routing, and mode behaviors are all there.

**Crisis protocol** — do not edit `skills/life-coach/references/crisis-protocol.md` without opening an issue first.

---

## Philosophy

> **The client already has the answer.**
> The coach's job is to ask the question that makes them realize they've known it all along.

The ancient traditions here — Vedic, Buddhist, Taoist, Chanakya — are not decorative. They represent accumulated insight into how humans get stuck and how they get unstuck. Every teaching is grounded in the client's specific situation, never quoted for its own sake.

---

## License

MIT License. See `LICENSE` for details.
