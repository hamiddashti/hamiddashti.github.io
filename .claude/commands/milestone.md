---
description: Milestone review. Run the five read-only check agents in parallel and combine their reports into one
argument-hint: "[scope: files, a folder or a ROADMAP milestone]"
---

Scope: $ARGUMENTS. If it is empty, review the whole live site plus the workflow files.

1. In a single message, launch these five agents in parallel and give each one the scope: `site-check`, `code-standards`, `content-check`, `provenance-check`, `continuity-check`. All five are read-only.
2. When all five have reported, write one report, grouped by agent:
   - **Passed:** one line per agent.
   - **Needs attention:** across all agents, most important first. Give `file:line`, what is wrong and the concrete fix. Mark anything that is wrong on the live site right now.
   - **Fix list:** numbered, so the user can approve items one by one.
3. Don't apply any fix. Wait for the user to approve items. Approved fixes are then done as normal work and logged at `/wrap-up`.
4. If the ROADMAP.md milestone is met, propose ticking it, and give a one-line note for the next notebook entry.
