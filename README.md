# The mock interview skill

Most people walk into interviews with almost no practice. This skill gives you the practice first: five Claudes
interview you for any job, from the real job post, before the real one. Free, MIT, no signup, no API key.

Made by **Alex Chen** ([@nocodealex](https://instagram.com/nocodealex)), an AI creator who builds free Claude Code skills. Full guide: [chen.media](https://chen.media/guides/practice-any-job-interview-with-5-claudes-first-free-mock-interview-skill).

## The panel

1. **The recruiter** checks the basics: why this job, why this company, your background, what you want next.
2. **The hiring manager** asks about results: what you did, what changed because of you, your first 90 days.
3. **The team lead** asks about the craft of the job (a real problem from the post) and how you work with others.
4. **The grader** scores every answer from 1 to 5 on relevance, evidence and structure, gives each interviewer's
   verdict (ADVANCE, MAYBE or NO) and an overall score out of 100.
5. **The coach** rewrites your three weakest answers in your own voice, using only facts you gave it.

Each interviewer asks real questions written for that job post, **one at a time, and waits for your answer**. Answer
by typing, or out loud with your computer's dictation. Say "skip" or "end" any time.

Everything goes in `.mock-interview/` where you run it: `TRANSCRIPT.md`, `REPORT.md` and `BETTER-ANSWERS.md`.

## Install

Paste this into Claude Code:

```
https://github.com/alexyc9381/mock-interview-skill
Install this skill, then confirm /mock-interview works.
```

Or as a plugin:

```
/plugin marketplace add alexyc9381/mock-interview-skill
/plugin install mock-interview-skill@mock-interview-skill
```

Or copy `skills/mock-interview` into `~/.claude/skills/`. Open a new Claude Code session afterwards.

## Use

```
/mock-interview job-post.pdf
```

A link or pasted text works too. Add your resume for sharper questions and rewrites:

```
/mock-interview https://example.com/jobs/product-designer  my-resume.pdf
```

One run is nine questions plus five sub-agent calls and counts toward your Claude plan's usage.

## Good to know

- It never invents employers, titles, dates or numbers. Where a better answer needs a fact it doesn't have, it
  leaves `[ADD: ...]` and asks you.
- It's practice made by language models. The real interviewers will ask their own questions, and it doesn't
  guarantee an offer.
- It is not made by Anthropic.

Run the tests with `python3 -m unittest discover -s tests`.

## Making a video or post about this?

Go ahead. Credit it like this, in your caption or description:

```text
/mock-interview skill by Alex Chen (@nocodealex): github.com/alexyc9381/mock-interview-skill
```

Tag [@nocodealex](https://instagram.com/nocodealex) so I can see it. Every file the skill writes already ends with
the same credit, so leave it in the shot.

Writing about it or citing it in a paper? Use **Cite this repository** in the sidebar on GitHub.
