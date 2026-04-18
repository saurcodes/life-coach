#!/usr/bin/env python3
"""
log_session.py — Persist coaching session snapshots to disk.

Called at the end of every session via /close or /snapshot commands.
Outputs a structured markdown file for continuity across sessions.

Usage:
    python scripts/log_session.py --client <id> --session <n> --data '<json>'

    Or interactive mode (prompts for each field):
    python scripts/log_session.py --interactive

Output: sessions/<client_id>/session_<n>_<date>.md
"""

import argparse
import json
import os
from datetime import datetime


SNAPSHOT_TEMPLATE = """
═══════════════════════════════════════════════
SESSION SNAPSHOT
═══════════════════════════════════════════════
Date: {date}
Session number: {session_number}

CORE CHALLENGE (in client's own words):
{core_challenge}

ROOT DIAGNOSIS:
  Primary block type: {block_type}
  Emotional driver: {emotional_driver}
  Readiness score at close: {readiness_score}/10

CLIENT ARCHETYPE DETECTED: {archetype}

WISDOM USED:
  Teaching: {wisdom_teaching}
  How it landed: {wisdom_landing}

EXERCISE ASSIGNED:
  Name: {exercise_name}
  Instructions given: {exercise_instructions}
  Deadline: {exercise_deadline}
  What to bring back: {exercise_bring_back}

COMMITMENTS MADE:
{commitments}

MINI-CHALLENGE:
  {mini_challenge}
  Notice: {mini_challenge_notice}

KEY INSIGHT FROM THIS SESSION:
{key_insight}

WHAT WAS NOT RESOLVED (carry forward):
{unresolved}

NEXT SESSION OPENS WITH:
  {next_session_question}

COACH NOTES (not shared with client):
  What I noticed but didn't name yet: {coach_notes_unspoken}
  What to watch for next time: {coach_notes_watch}
  Hypothesis to test: {coach_notes_hypothesis}
═══════════════════════════════════════════════
"""


def format_commitments(commitments_list):
    if not commitments_list:
        return "  None recorded"
    lines = []
    for i, c in enumerate(commitments_list, 1):
        action = c.get("action", "[not specified]")
        by_when = c.get("by_when", "[not specified]")
        how_know = c.get("how_know", "[not specified]")
        lines.append(f"  {i}. Action: {action} | By when: {by_when} | How we'll know: {how_know}")
    return "\n".join(lines)


def get_sessions_dir(client_id):
    base = os.path.join(os.path.dirname(__file__), "..", "sessions", client_id)
    os.makedirs(base, exist_ok=True)
    return base


def log_session(data: dict):
    client_id = data.get("client_id", "anonymous")
    session_number = data.get("session_number", 1)
    date_str = datetime.now().strftime("%Y-%m-%d")

    commitments_text = format_commitments(data.get("commitments", []))

    snapshot = SNAPSHOT_TEMPLATE.format(
        date=date_str,
        session_number=session_number,
        core_challenge=data.get("core_challenge", "[not captured]"),
        block_type=data.get("block_type", "[not diagnosed]"),
        emotional_driver=data.get("emotional_driver", "[not identified]"),
        readiness_score=data.get("readiness_score", "?"),
        archetype=data.get("archetype", "[not detected]"),
        wisdom_teaching=data.get("wisdom_teaching", "[none used]"),
        wisdom_landing=data.get("wisdom_landing", "[not recorded]"),
        exercise_name=data.get("exercise_name", "[none assigned]"),
        exercise_instructions=data.get("exercise_instructions", "[not recorded]"),
        exercise_deadline=data.get("exercise_deadline", "[not set]"),
        exercise_bring_back=data.get("exercise_bring_back", "[not specified]"),
        commitments=commitments_text,
        mini_challenge=data.get("mini_challenge", "[none assigned]"),
        mini_challenge_notice=data.get("mini_challenge_notice", "[not specified]"),
        key_insight=data.get("key_insight", "[not captured]"),
        unresolved=data.get("unresolved", "[none noted]"),
        next_session_question=data.get("next_session_question", "[not set]"),
        coach_notes_unspoken=data.get("coach_notes_unspoken", ""),
        coach_notes_watch=data.get("coach_notes_watch", ""),
        coach_notes_hypothesis=data.get("coach_notes_hypothesis", ""),
    )

    sessions_dir = get_sessions_dir(client_id)
    filename = f"session_{session_number:02d}_{date_str}.md"
    filepath = os.path.join(sessions_dir, filename)

    with open(filepath, "w") as f:
        f.write(snapshot.strip())

    print(f"Session snapshot saved: {filepath}")
    return filepath


def interactive_mode():
    print("\n=== Life Coach Session Logger ===\n")
    data = {}

    data["client_id"] = input("Client ID (anonymous reference, not real name): ").strip() or "anonymous"
    data["session_number"] = int(input("Session number: ").strip() or "1")
    data["core_challenge"] = input("Core challenge (client's words): ").strip()
    data["block_type"] = input("Block type [Clarity/Capability/Courage/Circumstance/Identity]: ").strip()
    data["emotional_driver"] = input("Emotional driver (be specific): ").strip()
    data["readiness_score"] = input("Readiness score at close (1-10): ").strip()
    data["archetype"] = input("Client archetype: ").strip()
    data["wisdom_teaching"] = input("Wisdom teaching used (or 'none'): ").strip()
    data["wisdom_landing"] = input("How it landed [Resonated/Didn't land/Partially]: ").strip()
    data["exercise_name"] = input("Exercise assigned (or 'none'): ").strip()
    data["exercise_deadline"] = input("Exercise deadline (specific date): ").strip()
    data["exercise_bring_back"] = input("What to bring back: ").strip()
    data["mini_challenge"] = input("Mini-challenge (exact text): ").strip()
    data["mini_challenge_notice"] = input("Notice (what to observe): ").strip()
    data["key_insight"] = input("Key insight from session: ").strip()
    data["unresolved"] = input("What was not resolved (carry forward): ").strip()
    data["next_session_question"] = input("Next session opens with (exact question): ").strip()

    print("\nCommitments (press Enter with blank action to stop):")
    commitments = []
    for i in range(1, 4):
        action = input(f"  Commitment {i} - Action: ").strip()
        if not action:
            break
        by_when = input(f"  Commitment {i} - By when: ").strip()
        how_know = input(f"  Commitment {i} - How we'll know: ").strip()
        commitments.append({"action": action, "by_when": by_when, "how_know": how_know})
    data["commitments"] = commitments

    data["coach_notes_unspoken"] = input("\nCoach notes - What I noticed but didn't name: ").strip()
    data["coach_notes_watch"] = input("Coach notes - What to watch for next time: ").strip()
    data["coach_notes_hypothesis"] = input("Coach notes - Hypothesis to test: ").strip()

    return log_session(data)


def main():
    parser = argparse.ArgumentParser(description="Log a coaching session snapshot")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("--client", help="Client ID")
    parser.add_argument("--session", type=int, help="Session number")
    parser.add_argument("--data", help="JSON string of session data")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.data:
        data = json.loads(args.data)
        if args.client:
            data["client_id"] = args.client
        if args.session:
            data["session_number"] = args.session
        log_session(data)
    else:
        print("Use --interactive for guided input, or --data '<json>' for direct input.")
        print("Run with --help for options.")


if __name__ == "__main__":
    main()
