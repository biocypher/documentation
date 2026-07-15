---
name: humanizer
description: Remove signs of AI-generated writing from text and revise drafts so they sound natural, specific, and human-written. Use when editing, reviewing, or rewriting documentation, guides, landing pages, release notes, or other prose to reduce AI tells such as inflated symbolism, promotional language, superficial -ing analysis, vague attributions, em dash overuse, rule-of-three cadence, AI-coded vocabulary, passive voice, negative parallelisms, filler phrases, generic conclusions, and chatbot-like framing.
---

# Humanizer

## Overview

Use this skill to edit text that sounds generated, padded, promotional, or too mechanically polished. Preserve the author's meaning, structure, register, and useful specifics while replacing AI-coded patterns with plainer, more natural prose.

For the full pattern guide and examples, read `references/signs-of-ai-writing.md` when the text is long, high-stakes, or requires a detailed audit.

## Workflow

1. Read the user's text and infer the intended audience, format, and voice.
2. If the user provides a writing sample, calibrate to it before rewriting. Match sentence length, word choice, paragraph openings, punctuation habits, transitions, and recurring verbal habits.
3. Scan for clusters of AI-writing tells, not isolated words. Do not flatten legitimate formal, technical, academic, or dry prose just because it is polished.
4. Draft a rewrite that covers everything the original covers. Keep paragraph count and rough structure unless the user asks for a stronger edit.
5. Ask yourself: "What still makes this sound obviously AI generated?" Fix the remaining tells.
6. Return the final rewrite. Include a short audit or change summary only when the user asks for review, comparison, or explanation.

## Documentation Guidance

- Keep docs useful before they are polished. Prefer concrete setup steps, product behavior, limits, examples, and decision points over sweeping claims about impact.
- Rewrite marketing-like copy into documentation copy unless the file is explicitly a landing page.
- Preserve headings, anchors, snippets, links, command names, option names, and API terms exactly unless the user asks for structural edits.
- Do not remove necessary repetition in procedural docs. Repetition can be clearer than elegant synonym cycling when it names the same button, page, file, or concept.
- Avoid narrating changes in stable docs. Changelogs and migration guides can say what changed; evergreen docs should describe the current behavior.

## Edit Rules

- Preserve meaning, claims, constraints, names, numbers, citations, and nuance.
- Prefer concrete details over significance inflation.
- Prefer simple constructions such as "is," "are," and "has" when they are clearer than "serves as," "stands as," "boasts," "features," or "represents."
- Replace vague authorities such as "experts say" or "industry reports suggest" with a named source when provided. If no source exists, cut the claim or state the uncertainty plainly.
- Remove chatbot residue such as "Of course," "I hope this helps," "let me know," "here is," "let's dive in," and knowledge-cutoff disclaimers.
- Break forced rule-of-three lists when two items or a more specific sentence would be more natural.
- Remove decorative bolding, emojis, title-case headings, and inline-header bullet lists unless the user's format requires them.
- Rewrite passive or subjectless fragments when an active subject makes the sentence clearer.
- Use straight quotation marks unless preserving a style guide that requires curly quotes.
- Ensure the final rewrite contains no em dashes or en dashes. Replace them with periods, commas, colons, parentheses, or a restructured sentence.

## Voice Guidance

For personal essays, blog posts, opinion pieces, and casual writing, allow some human texture: varied rhythm, mild opinion, uncertainty, asides, or a sharper verb when the author's voice supports it.

For documentation, encyclopedic, technical, legal, academic, or reference text, keep the prose neutral and plain. Do not add personality where neutrality is the human voice.

## False Positives

Do not flag a sentence only because it is grammatical, formal, dry, or uses one common transition word. Preserve specific details, mixed feelings, dated references, defensible first-person choices, genuine asides, and useful repetition. Watch for clusters: promotional tone plus em dashes plus rule-of-three plus vague significance language is a stronger signal than any one feature alone.

## Output

Default to returning only the revised text. When the user asks for an audit or when the edit is substantial, include:

1. A concise list of the main AI-writing patterns found.
2. The revised text.
3. A short note on what changed.
