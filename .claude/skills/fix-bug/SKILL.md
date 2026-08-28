---
name: fix-bug
description: >-
  Fixes a specific bug in a file. Does the work inside an isolated git
  worktree/branch so it never touches the main checkout directly. Once
  the fix is drafted, hands it off to the review-fix subagent, which
  must reply PASS or FAIL. A PR is only opened when the reviewer says
  PASS. On FAIL, the fix is reported but no PR is opened.
---

# Fix Bug Skill

Do these steps in order. Do not skip the review step, even if the fix
looks obviously correct to you.

## Step 1 — Create an isolated worktree
Create a new git worktree on its own branch for this fix, so the work
never touches the main checkout directly. Name the branch something
like `fix/<short-description>`.

Example:
```
git worktree add ../wt-fix-bug -b fix/calc-add
```

## Step 2 — Fix the bug
Inside that new worktree, find and fix the described bug. Make the
smallest correct change — do not refactor unrelated code. Where
possible, verify your fix with at least two different concrete
examples (not just the one that happens to look right).

## Step 3 — Hand off to the reviewer
Do NOT judge your own fix. Invoke the `review-fix` subagent and give
it the diff of your change. Wait for its reply.

The reviewer will reply with exactly one of:
- `PASS` — the fix is correct and safe to ship
- `FAIL` — with reasons why the fix is wrong or incomplete

## Step 4 — Act on the verdict
- If the reviewer replies **PASS**: open a pull request from the
  worktree branch. Include the reviewer's PASS verdict in the PR
  description.
- If the reviewer replies **FAIL**: do NOT open a PR. Report the
  reviewer's reasons back to the user instead, and stop.

## Step 5 — Clean up
Remove the worktree once the PR is opened (or once you've reported a
FAIL), so it doesn't linger:
```
git worktree remove ../wt-fix-bug
```---
name: fix-bug
description: >-
  Fixes a specific bug in a file. Does the work inside an isolated git
  worktree/branch so it never touches the main checkout directly. Once
  the fix is drafted, hands it off to the review-fix subagent, which
  must reply PASS or FAIL. A PR is only opened when the reviewer says
  PASS. On FAIL, the fix is reported but no PR is opened.
---

# Fix Bug Skill

Do these steps in order. Do not skip the review step, even if the fix
looks obviously correct to you.

## Step 1 — Create an isolated worktree
Create a new git worktree on its own branch for this fix, so the work
never touches the main checkout directly. Name the branch something
like `fix/<short-description>`.

Example:
```
git worktree add ../wt-fix-bug -b fix/calc-add
```

## Step 2 — Fix the bug
Inside that new worktree, find and fix the described bug. Make the
smallest correct change — do not refactor unrelated code. Where
possible, verify your fix with at least two different concrete
examples (not just the one that happens to look right).

## Step 3 — Hand off to the reviewer
Do NOT judge your own fix. Invoke the `review-fix` subagent and give
it the diff of your change. Wait for its reply.

The reviewer will reply with exactly one of:
- `PASS` — the fix is correct and safe to ship
- `FAIL` — with reasons why the fix is wrong or incomplete

## Step 4 — Act on the verdict
- If the reviewer replies **PASS**: open a pull request from the
  worktree branch. Include the reviewer's PASS verdict in the PR
  description.
- If the reviewer replies **FAIL**: do NOT open a PR. Report the
  reviewer's reasons back to the user instead, and stop.

## Step 5 — Clean up
Remove the worktree once the PR is opened (or once you've reported a
FAIL), so it doesn't linger:
```
git worktree remove ../wt-fix-bug
```