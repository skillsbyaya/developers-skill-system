# Screen Review

Judge a built screen by looking at it, then fix what is wrong. Use it before a person is shown a new or changed screen.

## Look first

Render the screen and open the pictures yourself: the whole page at phone width and at computer width, with realistic data, plus any state the change touches (empty, error, editing). Reading the code, or checking it against written rules, is not this review; token and value drift show in code, but whether a screen is good shows only in the picture.

Look as someone opening the page for the first time, before recalling any rule:

- What is this page for, and where does the eye go first? Is that the right place?
- Does anything look broken: things out of line, uneven gaps, controls of clashing sizes, a control that blends into its surface, text that is hard to read?
- Is anything said or shown twice? Is anything there that the page could lose?
- Is it obvious what can be pressed, and what each press will do?
- Does it look like it belongs with the product's best existing screens? Open one beside it and compare.
- Does it still work at phone width?

## Fix, then look again

Fix what you found using the existing tokens and shared components, render again, and repeat until you would not be embarrassed to show it. A fault found here is fixed wherever the same fault appears. If the problem is the page's organisation or wording, not its presentation, take it to `agent-ux-designer` or the writer before polishing.

## What not to write down

This workflow changes the screen, not the design documents. Do not add what you learned to `DESIGN.md` or any rule list: how one page was fixed does not bind the next. Only a new token or shared component, or a decision the user states is for the whole product, goes to the design-token-system workflow.

## Finish

Show the user the whole page at once, pictures and a short account of what it does in the same message. A comment they make about this page is about this page; ask once if it is unclear whether they mean it for every screen.
