# Life Coach — Claude Code Plugin

A life coaching plugin for Claude Code that bridges ancient wisdom traditions — Vedas, Upanishads, Bhagavad Gita, Tao Te Ching, Buddhism, Chanakya's Arthashastra — with modern psychology and structured coaching methodology.

---

## What This Plugin Does

Once installed, this plugin transforms Claude into a structured life coach capable of:

- Running multi-phase coaching sessions using a proven 7-phase framework
- Detecting and adapting to 8 distinct client archetypes (Analyst, Achiever, Empath, Seeker, Strategist, Philosopher, Integrator, Builder)
- Diagnosing root blocks across 5 dimensions: Clarity, Capability, Courage, Circumstance, and Identity
- Weaving ancient wisdom seeds naturally into conversation — dropped when the moment calls for it, never on a schedule
- Delivering 40+ full wisdom teachings matched to the client's specific block and archetype
- Assigning 25 targeted exercises across 7 coaching domains
- Tracking progress and continuity across sessions via session snapshots
- Firing automatic hooks for crisis detection, resistance, insight moments, and more

---

## Plugin Structure

```
life-coach-skills/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest (name, version, description)
├── commands/                         # External slash commands (/life-coach:*)
│   ├── start.md, close.md, recap.md, snapshot.md
│   ├── diagnose.md, reframe.md, archetype.md
│   ├── wisdom.md, exercise.md, challenge.md
│   ├── checkin.md, progress.md, pattern.md
│   ├── deepwork.md, maintenance.md
└── skills/
    └── life-coach/                   # Main skill (life-coach:life-coach)
        ├── SKILL.md                  # Orchestrator — routing tables & session flow
        ├── command-handlers/         # Internal command logic
        │   ├── session-management.md # /start /recap /close /snapshot
        │   ├── diagnostic.md         # /diagnose /reframe /archetype
        │   ├── exercise-wisdom.md    # /exercise /wisdom /challenge
        │   └── progress-accountability.md  # /checkin /progress /pattern /deepwork /maintenance
        ├── references/               # Load-on-demand reference files
        │   ├── client-archetypes.md
        │   ├── crisis-protocol.md
        │   ├── diagnostic-deep.md
        │   ├── exercise-library.md
        │   ├── session-memory-template.md
        │   └── wisdom-library.md
        ├── hooks/                    # Auto-firing condition hooks
        │   ├── 01-crisis-scan.md
        │   ├── 02-resistance-detector.md
        │   ├── 03-emotion-surge.md
        │   ├── 04-insight-flash.md
        │   ├── 05-loop-detector.md
        │   ├── 06-advice-seeking.md
        │   ├── 07-commitment-inflation.md
        │   └── 08-session-drift.md
        └── scripts/
            └── log_session.py        # Session snapshot persistence
```

**Design principle**: `SKILL.md` is the conductor. Reference files load on demand — never all at once. External commands give direct control. Internal hooks fire automatically when conditions are detected.

---

## Installation

### Claude Code (CLI & Desktop)

**Step 1** — Add this repo as a marketplace (one-time):

```
/plugin marketplace add saurcodes/life-coach
```

**Step 2** — Install the plugin:

```
/plugin install life-coach@life-coach
```

**Step 3** — Activate:

```
/reload-plugins
```

All commands are now available as `/life-coach:start`, `/life-coach:wisdom`, etc.

To uninstall: `/plugin uninstall life-coach@life-coach`

---

### Claude.ai

Claude.ai uses a ZIP upload for skills:

1. Download or clone this repo
2. Zip the `skills/life-coach/` folder
3. In Claude.ai, go to **Customize → Skills → + → Upload a skill**
4. Upload the ZIP

The skill will appear in your Skills list and can be toggled on/off. Custom skills are private to your account by default. Team/Enterprise plans can share skills organization-wide via organization settings.

---

### Test Without Installing (development)

Load the plugin for a single session without installing it:

```bash
claude --plugin-dir /path/to/life-coach-skills
```

---

### Session Logging (Optional)

The `/life-coach:close` command calls `scripts/log_session.py` to persist session snapshots. Requires Python 3:

```bash
chmod +x skills/life-coach/scripts/log_session.py
```

Session logs are saved to `~/.claude/life-coach/sessions/<client_id>/`.

---

## Usage

### Automatic Activation

The skill triggers automatically when you express being stuck, navigating a life challenge, or needing structured guidance:

- *"I'm stuck and don't know what to do"*
- *"I need help thinking through a career decision"*
- *"Something feels off but I can't name it"*
- *"I'm burned out and don't know how to reset"*

### Commands

All commands are namespaced under `life-coach:`. They also work as plain text intent (e.g., "let's close the session" triggers close).

| Command | What it does |
|---|---|
| `/life-coach:start` | Begin a new session with continuity check |
| `/life-coach:recap` | Structured summary of where the session stands |
| `/life-coach:close` | Close with insights, action items, and a challenge |
| `/life-coach:snapshot` | Save a session record without closing |
| `/life-coach:diagnose` | Full multi-axis root cause assessment |
| `/life-coach:reframe` | Fresh perspective — pattern interrupt |
| `/life-coach:archetype` | See how Claude is reading and adapting to you |
| `/life-coach:wisdom [theme]` | Ancient teaching matched to your situation |
| `/life-coach:exercise [topic]` | Targeted exercise with full instructions and deadline |
| `/life-coach:challenge` | 48–72 hour micro-challenge |
| `/life-coach:checkin` | Accountability review from your last session |
| `/life-coach:progress` | Map the full arc of your coaching journey |
| `/life-coach:pattern` | Name a recurring pattern explicitly |
| `/life-coach:deepwork` | Switch to Deep Work Mode (higher intensity) |
| `/life-coach:maintenance` | Switch to Maintenance Mode (integration check-in) |

### Example Session

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

*Notice the Gita reference in the second response — a wisdom seed dropped when it fit, not on schedule.*

### Operating Modes

| Mode | When | Behavior |
|---|---|---|
| **Discovery** (default) | New client or new topic | Slower, exploratory, readiness threshold 6/10 |
| **Deep Work** (`/life-coach:deepwork`) | Clear challenge, ready to go hard | Compressed phases, full diagnosis, threshold 8/10 |
| **Maintenance** (`/life-coach:maintenance`) | Integration phase or periodic check-in | Arc review, no new diagnosis, shorter sessions |

### Automatic Hooks

These fire without any command — Claude detects the condition and responds:

| Hook | Triggers when... |
|---|---|
| 🔴 Crisis Scan | Any language suggesting suicidal ideation, self-harm, or acute crisis |
| 🟠 Resistance Detector | Client pushes back on the same point 2+ times |
| 🟠 Emotion Surge | Unexpected emotional shift mid-session |
| ✨ Insight Flash | Client has a sudden moment of self-recognition |
| 🟡 Loop Detector | Same concern returns 3+ times without resolution |
| 🟡 Advice Intercept | "Just tell me what to do" before the root block is diagnosed |
| 🟡 Commitment Inflation | Commitment is too vague, too large, or unrealistic |
| 🟡 Session Drift | 5+ exchanges with no movement toward insight or action |

---

## Wisdom in Conversation

Ancient teachings appear in two ways:

**Wisdom seeds** — brief, organic. A single sentence or image from tradition dropped mid-conversation when what the client just said genuinely calls for it. Not explained, not defended. If it resonates, the thread opens. If it doesn't, it's released. Used only when the moment earns it, never on a schedule.

**Full teachings** (Phase 4) — one per session, matched to the diagnosed block and archetype. Wrapped in story, connected directly to the client's situation, followed by *"How does that land?"*

Traditions drawn from: Bhagavad Gita, Upanishads, Tao Te Ching, Buddhism (Theravada and Zen), Chanakya's Arthashastra, Vedic mythology, Cherokee parable, Jungian psychology, Japanese philosophy (Ikigai, Kintsugi).

---

## Session Logging

At session close, a snapshot enables continuity in future sessions:

```bash
# Interactive mode
python3 scripts/log_session.py --interactive

# JSON mode
python3 scripts/log_session.py --client alice --session 3 --data '{
  "core_challenge": "Career crossroads",
  "block_type": "Courage",
  "emotional_driver": "Fear of public failure",
  "readiness_score": "8",
  "archetype": "Achiever",
  "next_session_question": "You committed to the conversation with your manager by Friday. What happened?"
}'
```

Snapshots are stored in `sessions/<client_id>/session_<n>_<date>.md` and loaded automatically when a returning client starts a new session.

---

## Contributing

Contributions welcome — new exercises, wisdom teachings, archetype profiles, hook patterns, and language improvements all make the plugin more effective.

### What to Contribute

- **New exercises**: Add to `references/exercise-library.md` — include name, best-for, time required, archetype fit, full script, and debrief question
- **New wisdom teachings**: Add to `references/wisdom-library.md` under the appropriate block-type section — include teaching, modern translation, deploy-as script, and follow-up question
- **New archetypes**: Add to `references/client-archetypes.md` with detection signals, coaching adaptations, wisdom style, exercise style, and pace
- **Hook improvements**: Add detection patterns, edge cases, or response scripts to the relevant `hooks/` file
- **Bug fixes**: Incorrect archetype mappings, missing edge cases, broken scripts

### Contribution Guidelines

1. **Follow the existing format** — each section has a consistent structure. New content must match it.
2. **One exercise = full script** — never add an exercise summary. Half-written instructions don't get used.
3. **One teaching = full deployment script** — include the `Deploy as:` language and the `Follow-up:` question.
4. **Test your additions** — use the plugin in a real session with your new content before submitting.
5. **No invented traditions** — all wisdom teachings must be grounded in real philosophical or contemplative traditions with a cited source.
6. **Crisis protocol is not a contribution area** — changes to `references/crisis-protocol.md` require careful review. Open an issue first.

---

## Philosophy

> **The client already has the answer.**
> The coach's job is to ask the question that makes them realize they've known it all along.

Every command, every hook, every phase, every teaching exists only to serve that moment of recognition.

The ancient wisdom traditions here — Vedic, Buddhist, Taoist, Jungian — are not decorative. They represent thousands of years of accumulated insight into how humans get stuck and how they get unstuck. This plugin treats them with that respect: grounding every teaching in the client's specific situation, never quoting for its own sake.

---

## License

MIT License. See `LICENSE` for details.
