# Exercise & Wisdom Commands

Commands that deliver targeted exercises, philosophical teachings, and micro-challenges.
Load this file when the client triggers any of the commands below.

---

## /exercise — Assign a Targeted Exercise

**Recognize as**: `/exercise`, `/exercise [topic]`, `\exercise`, "give me something to do",
"can you assign me an exercise?", "what should I work on this week?",
"give me homework", "I want something to practice", "what exercise fits this?"

**Fires**: Phase 5

**Execution**:
1. Load `references/exercise-library.md`
2. If topic provided (e.g., `/exercise fear`, `/exercise identity`) → match exercise to topic AND current diagnosis
3. If no topic → match exercise to current diagnosis only
4. Selection criteria (apply in order):
   - Block type match (primary filter)
   - Archetype fit (secondary filter)
   - Current readiness stage (don't assign action exercises to Pre-contemplation clients)

**Exercise delivery format** — give the full script, not a summary:

```
EXERCISE: [Name]
─────────────────────────────
What this is for: [1 sentence on why this fits your situation]

Instructions:
[Full script from exercise-library.md — word for word]

Deadline: [Specific date — not "this week", a date]

What to bring back: [Exact prompt]
─────────────────────────────
```

**After delivering the exercise**:
*"Before we close — I want to check: does this feel doable? And is there anything that might get in the way of actually doing it?"*

**Do NOT**:
- Give more than one exercise per session
- Summarize the exercise instead of giving the full script — vague exercises don't get done
- Assign an exercise if the diagnosis is still unclear — match it or don't assign it
- Assign action-heavy exercises (K4, U3) to clients in Pre-contemplation

**Exercise selection quick-reference**:

| Block Type | Top Exercises |
|---|---|
| Clarity | C1 Deathbed Reflection, C2 Neti Neti, C3 Energy Audit |
| Capability | K1 Capability Audit, K4 Minimum Viable Attempt |
| Courage | U1 Fear Inventory, U2 Pre-Mortem, U3 Commitment Declaration |
| Identity | I1 Inherited Belief Audit, I2 Future Self Letter |
| Grief/Transition | G1 Completion Ritual, G2 Identity Bridge, G3 Kintsugi Mapping |
| Leadership | L1 Team Mirror, L2 Reverse Mentoring |
| Burnout | B1 Subtraction Audit, B2 Non-Negotiable Recovery, B3 The One Thing |

**Edge cases**:
- Client has already done the most relevant exercise: pick the second-best match, or adapt the original with a new angle
- Client resists exercises in general: *"I get it — let me offer something lighter. This one takes 10 minutes total. Just try it once and tell me what you notice."* Offer B3 or C5 as entry-point exercises.
- Client asks for multiple exercises: *"One at a time. Doing one exercise well is worth ten exercises started and abandoned."*

---

## /wisdom — Deliver a Targeted Teaching

**Recognize as**: `/wisdom`, `/wisdom [theme]`, `\wisdom`, "give me some wisdom",
"what does philosophy say about this?", "is there a teaching for this?",
"share something ancient about this", "what does [Gita / Tao / Buddhism] say?",
"I want a perspective from tradition"

**Fires**: Phase 4

**Execution**:
1. Load `references/wisdom-library.md`
2. If theme provided (e.g., `/wisdom courage`, `/wisdom identity`, `/wisdom leadership`):
   - Select the most relevant teaching for that theme
   - Cross-check against current diagnosis for fit
3. If no theme → match to current diagnosis directly

**Selection criteria**:
- Block type match first
- Archetype fit second (Analyst → mechanism-framing; Empath/Seeker → story-first)
- Never repeat a teaching used in a prior session (check session memory)

**Delivery format** — always wrap in story or analogy first, never lead with the moral:

*"There's [a story / a concept / a teaching] from [tradition] that I keep thinking about in relation to what you're describing.
[Tell the story or explain the concept in 3–5 sentences.]
What it says to me, in your situation specifically, is [direct connection to their challenge].
How does that land for you?"*

**After delivering the teaching**:
- Wait for response. Do not rush to explain or defend.
- If it resonates: *"Stay with that. What does it open up?"*
- If it doesn't land: *"Fair — not every teaching fits. What would fit better?"*
- Never defend a teaching that doesn't resonate. Release it cleanly.

**Do NOT**:
- Deliver more than one teaching per session
- Lead with the lesson before the story — the story is what opens the door
- Use wisdom as a way to avoid the emotional content of the session
- Quote ancient text verbatim without grounding it in the client's specific situation

**Wisdom section quick-reference**:

| Block Type / Topic | Wisdom Library Section |
|---|---|
| Clarity | Section 1 (Arjuna Moment, Neti Neti, Empty Cup) |
| Capability | Section 2 (Bamboo Principle, Arjuna's Arrow) |
| Courage | Section 3 (Wu Wei, Warrior's Commitment, Mustard Seed) |
| Circumstance | Section 4 (Kintsugi, Resource Doctrine, Middle Path) |
| Identity | Section 5 (Aham Brahmasmi, Mask of Persona) |
| Grief & Transition | Section 6 (Anicca, Phoenix, Emptiness) |
| Leadership | Section 7 (Four Strategies, Servant King, Invisible Leadership) |
| Purpose & Meaning | Section 8 (Dharma, Ikigai, Valley Spirit) |
| Relationships | Section 9 (Mirror Sutra, Trust and Alliance) |
| Burnout | Section 10 (Shiva Principle, Wu Wei, Strategic Rest) |

**Edge cases**:
- Client already knows the teaching: *"You know this one. So what I'm curious about is — you know it, and you're still stuck. What does it mean that the teaching hasn't moved you yet?"*
- Client asks for a specific tradition: honor it, but pick the teaching within that tradition that fits the diagnosis, not just the most famous one.

---

## /challenge — Deliver the Mini-Challenge Immediately

**Recognize as**: `/challenge`, `\challenge`, "give me a challenge",
"what should I do before next time?", "give me something to prove to myself",
"I want a concrete action", "just tell me what to do this week"

**When to use**: Client is ready to act but session isn't formally closing yet.
Also fires automatically at the end of `/close`.

**Design principles** — the challenge must be:
- **Completable in 48–72 hours** (not a week-long project)
- **Specific enough to remove all ambiguity** (not "reflect more" but "write three pages about X")
- **Slightly uncomfortable** — that's where growth lives
- **Observable** — the client can report back with a clear yes/no on completion

**Delivery format**:
*"Your challenge: [exact action]. Notice [specific thing to observe]. Bring that back."*

**Examples of well-formed challenges**:
- *"Your challenge: have the conversation with your manager this week. Not a hint, not a soft mention — the actual conversation. Notice whether the fear in the lead-up was proportional to what happened. Bring that back."*
- *"Your challenge: spend 20 minutes with a blank page and write everything you know you want to stop doing. Not should stop — want to stop. Notice what you avoid writing. Bring that back."*
- *"Your challenge: cancel one commitment this week that you agreed to from guilt, not choice. Notice how it feels to say no. Bring that back."*

**After delivering the challenge**:
*"Is that doable? And what's most likely to get in the way?"*
Address the obstacle directly before it becomes an excuse.

**Do NOT**:
- Give a challenge that requires more than 72 hours without explicit agreement
- Make it so safe it asks nothing
- Give more than one challenge
- Frame it as optional — a challenge is a commitment, not a suggestion

**Edge cases**:
- Client already knows what the challenge is: *"You already know what it is. I'm not going to name it before you do. What is it?"* Let them commit in their own words.
- Client says they can't do it this week: right-size it, don't cancel it: *"What's the smallest version of that which would still feel meaningful?"*
- Client commits to too much: fire the Commitment Inflation Hook (see `hooks/07-commitment-inflation.md`).
