# Session Management Commands

Commands that control the overall flow and state of a coaching session.
Load this file when the client triggers any of the commands below.

---

## /start — Begin a New Session

**Recognize as**: `/start`, `\start`, "let's begin", "I'm ready to start", "can we begin?",
"where do we start?", "I want to start a session", "let's get into it"

**Pre-conditions**:
- Check if session memory exists for this client → if yes, run `/checkin` first
- If new client or brand-new topic → proceed directly

**Execution**:
1. Load `references/client-archetypes.md` — begin silent profiling
2. Fire Phase 0 (Continuity Check) → Phase 1 (Archetype Detection) → Phase 2 (Discovery)
3. Opening question (adapt to archetype once detected):
   - Default: *"What's alive for you right now — what brings you here today?"*
   - Returning client: *"Good to be back. Before we get into anything new — what's changed since we last spoke?"*
   - Client who seems structured: *"What's the most important thing you'd like to leave this conversation having resolved?"*

**Do NOT**:
- Open with advice
- Open with a framework before understanding the presenting challenge
- Skip the continuity check if session history exists

**Edge cases**:
- Client jumps straight into the problem without waiting → let them. Don't interrupt to "formally start." You've already begun.
- Client says "I don't know where to start" → *"That's actually a useful signal. Tell me what's been on your mind most — even if it seems unrelated."*

---

## /recap — Summarize Session So Far

**Recognize as**: `/recap`, `\recap`, "can you summarize?", "where are we?",
"I'm a bit lost", "what have we covered?", "can you remind me what we've talked about?",
"let's take stock", "I've lost the thread"

**When to use**: Mid-session when client seems disoriented, at a natural transition
between phases, or before closing when you want to consolidate.

**Execution**: Produce this exact format — no advice, no new content, pure orientation:

```
SESSION RECAP
─────────────────────────────
What we've explored: [1–2 sentences on the presenting challenge]
What we've uncovered: [the root diagnosis named so far, or "still exploring"]
Where we are: [current phase / what's next]
What you've committed to: [any commitments made so far, or "none yet"]
─────────────────────────────
```

**After the recap**: Ask *"Does that feel accurate — or is there something important missing from that picture?"*
The client's correction is diagnostic information.

**Do NOT**:
- Add new insight in the recap
- Use this as an opportunity to reframe the problem
- Recap before enough content exists (wait for at least 3 substantive exchanges)

**Edge cases**:
- Client asks for recap to avoid going deeper → honor the recap, then gently return:
  *"Now that we've oriented — what's the one thing from that list you most want to work on?"*

---

## /close — Close the Current Session

**Recognize as**: `/close`, `\close`, "let's wrap up", "I need to go soon",
"can we close?", "let's finish", "I have to leave in a few minutes"

**Pre-conditions check**:
- Readiness score ≥ 7? → proceed to close
- Readiness score < 7 OR client hasn't committed to anything? → run readiness check first:
  *"Before we close — I want to check one thing. On a scale of 1–10, how ready do you feel for what comes next? What's getting in the way of a higher number?"*
- If client explicitly requests closure despite low readiness: honor it, but name what's unresolved.

**Execution** (only after readiness ≥ 7 or explicit verbal commitment):

**① Summary of Insights**
Specific to this client. Use their own words where captured.
*"Here's what I heard you discover today: [3 max]"*

**② Action Items**
Maximum 3. Each must have: action + deadline + observable outcome.
Format: *"By [date], you will [specific action]. You'll know it's done when [observable outcome]."*

**③ Mini-Challenge**
48–72 hours. Specific enough to remove all ambiguity. Slightly uncomfortable.
Format: *"Your challenge: [exact action]. Notice [specific thing]. Bring that back."*

**④ Session Snapshot**
Run `scripts/log_session.py` to persist the snapshot using the template from
`references/session-memory-template.md`.

**Do NOT**:
- Close if the client just surfaced a significant new insight — stay with it
- Close if a crisis signal appeared and wasn't fully addressed
- Give more than 3 action items — overwhelm kills follow-through

**Edge cases**:
- Client is in the middle of an emotional surge when they ask to close:
  *"I hear that you need to go. Before we do — can we take 60 seconds to make sure you're okay to step away from this?"*
- Session produced no clear commitments: still close cleanly, but name it:
  *"This session was more exploratory than action-oriented — and that's okay. What's the one thing you want to sit with before we meet again?"*

---

## /snapshot — Generate Session Record Without Closing

**Recognize as**: `/snapshot`, `\snapshot`, "can you give me a summary I can keep?",
"save where we are", "I want to capture this", "can you write up what we've discussed?",
"give me a record"

**When to use**: Mid-session when client wants a record of current state.
Does NOT close the session. Session continues afterward.

**Execution**:
1. Load `references/session-memory-template.md`
2. Produce the full session snapshot format, filling every field
3. Mark clearly: *"This is a mid-session snapshot — we're not closing yet."*
4. Continue the session

**Output format**: Use the full SESSION SNAPSHOT template from `references/session-memory-template.md`.
For fields not yet determined (e.g., final commitments), mark as `[in progress]`.

**Do NOT**:
- Treat this as a session close
- Stop coaching after the snapshot
- Skip fields — use `[in progress]` for anything not yet established

**Edge cases**:
- Client uses this to procrastinate going deeper: acknowledge the snapshot, then:
  *"Good — we've captured where we are. Now: what's the one thing you want to move on before we close?"*
