---
name: tdd
description: Project-wide specification and test-driven workflow for every development change in this documentation repository. Use before any feature, fix, refactor, content or UI modification, configuration change, or other implementation work, then resume after implementation to verify the agreed acceptance specs. Align on the user's what and why, formalize minimal MMECE outcomes with planned tests, and validate visual documentation at 16:9, 3:4, and mobile sizes.
---

# Spec-Driven TDD

Use this skill in two phases: align and specify before implementation, then test and iterate after implementation. Keep implementation itself outside this skill.

## 1. Align on intent

1. Inspect the request and relevant project context.
2. Establish the requested observable outcome, its purpose, constraints, and boundaries.
3. Ask focused questions whenever uncertainty could change the expected result. Ask about **what** and **why**, never how to implement it.
4. Ask one to three questions per round and continue until no material ambiguity remains. Do not proceed while the goal is unclear.
5. Skip questions when the request already establishes the outcome and purpose.

Do not start implementation during this phase.

## 2. Write the acceptance checklist

Formalize the aligned goal as an MMECE checklist:

- **Minimal:** include only the requested outcome and essential constraints. Exclude speculative improvements and nice-to-haves.
- **Mutually exclusive:** ensure each spec covers a distinct observable result. Merge overlapping items.
- **Collectively exhaustive:** cover the whole requested outcome without expanding its scope.

Default to one integrated spec per request. Add another spec only when a distinct result can fail independently.

Write specs as observable outcomes, not implementation steps. Put the planned integrated test directly under each spec:

```markdown
### Acceptance checklist

- [ ] S1 — <observable expected result>
  - Verify: <integrated test and required evidence>
```

State non-goals only when needed to prevent scope creep. Present the checklist before development begins.

## 3. Hand off implementation

End the pre-development phase after the checklist is clear. Do not prescribe or perform implementation as part of this skill. Use the normal development workflow for the change, then resume this skill for verification.

Keep the checklist stable. Change it only when the user changes the goal or testing reveals a genuine ambiguity, and realign with the user before doing so.

## 4. Verify every spec

After implementation:

1. Build the documentation and run relevant source-level checks.
2. Execute the planned integrated test for every spec.
3. For visual documentation, always test the rendered site with the built-in browser tool or Playwright MCP at:
   - Fullscreen 16:9: `1440 × 810`
   - Half-screen 3:4: `768 × 1024`
   - Mobile: `390 × 844`
4. Inspect the page visually at each size. Do not rely on DOM metrics alone.
5. Check only what the specs require plus essential regressions: correct content and links, responsive visibility, layout balance, clipping or overflow, relevant interactions, accessibility semantics, and browser errors.
6. Record concise evidence beneath each spec. Mark a checkbox complete only after its planned test passes.

## 5. Iterate on failures

When a spec fails:

1. Record the observed mismatch.
2. Return to the normal implementation workflow for the fix.
3. Rebuild and rerun the failed test.
4. Recheck essential regressions at all three viewports.

Repeat until every spec passes or a genuine blocker requires user input. Never weaken a spec to match the implementation.

## 6. Report completion

Return the completed checklist with concise evidence, commands or checks run, and the three tested viewport sizes. Report any unresolved limitation explicitly. Do not claim completion without test evidence.
