# Preview Loop

Use this workflow when the user will judge many small visible changes by looking at them: a page-by-page review, a copy or layout polish pass, a design hand-back. The whole pass is one story on one branch, and it stays incomplete until the user says the pass is done. Nothing lands per change.

1. Confirm the scope in a line: visible changes only. A change that needs a migration, a new route or new behaviour is recorded in the project's backlog as its own story and does not join the pass.
2. Start the app once, the way the project's instructions say (its dev server against local data), sign the user in, and open it in their browser. Say where it is running. Keep it running for the whole session.
3. Loop: the user says what to change; make the change; tell them which page to refresh. Their look is the working check. Run a narrow check only for something they cannot see, such as a server action or a calculation. No plan, record update or assurance note per change.
4. When the user accepts a batch, or an hour has passed, checkpoint through `close-session` packet close. The story record's execution area holds only the pages done, the pages left, and anything asked for that is not yet done or accepted.
5. Close through `close-session` as a checkpoint whenever the session ends before the user says the pass is done. When they do, record that their preview covered every change and close fully: the pass lands once, on the tiers its diff selects, with no separate review session. A sibling of a parallel set follows [Parallel sessions](#parallel-sessions) instead.

## Parallel sessions

When the user runs several passes at once, each session is one sibling of a set: its own worktree on its own branch, named from the set's base branch plus a letter (`story/<key>-a`, `-b`, …). A joining session fetches, takes the next unused letter and branches from the default branch.

- A sibling never edits the story record, status lines or backlog, which the set's landing writes once. It keeps its pages done, pages left and open asks in its checkpoint commit messages.
- When the user says the sibling's item is done, checkpoint with a message starting `checkpoint: done`. Then fetch and read the last commit subject on every sibling. If one is not done, stop there: the sibling waits, and nothing lands.
- The session that finds every sibling done lands the set. First push the base branch, created from the current default branch; if that push is refused, another sibling is already landing, so stop. Merge each sibling into it, show the user any conflict they would see, write the shared documents once, and close fully. After the merge, close-session deletes the sibling branches and their worktrees.
- "Land what's done" lands the done siblings the same way at any time and leaves the rest on their branches.
