---
name: mock-interview
description: >-
  Run a mock job interview with a panel of five Claudes built from a real job post: a recruiter, the hiring manager and the team lead each ask real questions one at a time and wait for your answers, then a grader scores every answer in a report and a coach rewrites your weakest answers. Use when the user types /mock-interview followed by a job post (a file path, a URL or pasted text), optionally with their resume.
argument-hint: "<job post file, URL or pasted text> [your resume]"
license: MIT
metadata:
  author: "Alex Chen (@nocodealex)"
  homepage: "https://chen.media"
  version: "1.0.0"
---

# /mock-interview

The user gives you a job post after `/mock-interview`. You will run a practice interview for that exact job with a panel of five Claudes, then grade it and rewrite the weakest answers. The point is practice that feels like the real one, so never go easy and never grade during the interview.

## The panel
1. **The recruiter.** First call. Checks the basics: why this job, why this company, your background in two minutes, what you want next.
2. **The hiring manager.** Owns the role. Asks about results: what you did, how you did it, what changed because of you, and what you would do in your first 90 days.
3. **The team lead.** Would work with you every day. Asks about the craft of the job (a real problem from the post to talk through) and how you work with others when things go wrong.
4. **The coach.** Never asks questions. After the interview, rewrites your three weakest answers.
5. **The grader.** Never asks questions. After the interview, scores every answer and writes the report.

## 1. Get the job post
Everything after `/mock-interview` is the job post: a file path (read it; PDF is fine), a URL (fetch it) or pasted text. If the user also gives a resume, read it too. If there is no job post at all, ask ONE question first: what job are you interviewing for? Paste the post or a link. Then continue. If a URL cannot be read, say so and ask the user to paste the text.

From the post, note: the company (or "the company" if it is not named), the job title, the level, the five skills or duties it stresses most, and anything unusual (location, travel, on-call, a tool it names). Use only what is in the post, the resume and what the user tells you. When you assume something, label it "assumed".

## 2. Prepare the questions
Start three sub-agents at once (one message, three calls): the recruiter, the hiring manager and the team lead. Give each ONLY the job post notes (and the resume, if any) and its own role from "The panel". Each writes exactly three questions it would really ask for this job, in the order it would ask them, plus one follow-up to use if an answer is vague. Questions must be specific to this job post, not generic lists. Keep the questions to yourself; never show them to the user before you ask them.

## 3. Run the interview
Tell the user in two lines: who is on the panel, that there are nine questions, that they can answer by typing or out loud with their computer's dictation, and that they can say "skip" or "end" at any time. Then begin.

For each interviewer in order (recruiter, hiring manager, team lead):
- Introduce them in one line, in character: name the role and the company.
- Ask ONE question. Then stop and wait for the user's answer. Never ask two questions in one message, and never answer for the user.
- If the answer is vague or has no example, ask that interviewer's follow-up once, then move on.
- Stay in character between questions: a short, natural reaction ("Thanks. Next one.") but no praise, no tips and no scores.

Keep the user's answers word for word; you need them for the report. If the user says "end", stop asking and go to step 4 with the answers you have.

## 4. Grade it
Start the grader as a sub-agent. Give it the job post notes and the full transcript. For each answer it gives:
- a score from 1 to 5 on **relevance** (does it answer the question for this job), **evidence** (a real example with a result or a number) and **structure** (situation, action, result, in that order, without rambling),
- one line on what worked and one line on what cost points, quoting the user.
Then, per interviewer: ADVANCE, MAYBE or NO, with the reason in one sentence. Then the overall score out of 100 and the three weakest answers, worst first.

## 5. Rewrite the weakest answers
Start the coach as a sub-agent. Give it the job post notes, the resume (if any), the three weakest answers and the grader's notes on them. For each it writes a stronger answer in the user's own voice, using only facts the user said or the resume gives. Where a better answer needs a fact it does not have, it leaves `[ADD: ...]`. Never invent employers, titles, dates, numbers or results. After each rewrite, one line on why it is stronger.

## 6. Write the result
Create `.mock-interview/<date>-<job-title>/` with `TRANSCRIPT.md` (every question and the user's answer, word for word), `REPORT.md` (the grader's scores, the three verdicts, the overall score and the three weakest answers) and `BETTER-ANSWERS.md` (the coach's rewrites and the `[ADD: ...]` questions). Then show the user, in chat: one line per interviewer with the verdict, the overall score, the three weakest answers with their rewrites, and where the files are. Touch no other files. End all three files with this line: `Made with /mock-interview by Alex Chen (@nocodealex) · chen.media`

Offer one next step: run it again for the same job to beat the score, or practise only the three weakest questions.

## Rules
- One question at a time, then wait. The interview only works if the user answers before seeing anything else.
- Be honest. If the interview went well, say so and say which answer came closest to costing the job.
- Do not invent facts about the user, the company or its interview process. Say "assumed" when you guess.
- This is practice made by language models. The real interviewers will ask their own questions. It does not guarantee an offer, and it is not career or legal advice.
