# Preview Loop

Use this workflow when the user will judge many small visible changes by looking at them: a page-by-page review, a copy or layout polish pass, a design hand-back. The whole pass is one story on one branch, and it stays incomplete until the user says the pass is done. Nothing lands per change.

1. Confirm the scope in a line: visible changes only. A change that needs a migration, a new route or new behaviour is split out as its own story and does not join the pass.
2. Start the app once, the way the project's instructions say (its dev server against local data), sign the user in, and open it in their browser. Say where it is running. Keep it running for the whole session.
3. Loop: the user says what to change; make the change; tell them which page to refresh. Their look is the working check. Run a narrow check only for something they cannot see, such as a server action or a calculation. No plan, record update or assurance note per change.
4. When the user accepts a batch, or an hour has passed, recheck the branch, then commit `checkpoint:` to the story branch and push. The story record's execution area holds only the pages done and the pages left.
5. Close through `close-session` as a checkpoint whenever the session ends before the user says the pass is done. When they do, record that their preview covered every change and close fully: the pass lands once, on the tiers its diff selects, with no separate review session.
