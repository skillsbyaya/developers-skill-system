# Interface copy

Wording written into a specification is built exactly as written, so it is chosen here once and carried everywhere. A screen is designed so that it needs no explaining; a sentence of explanation is the sign that the design is not finished. A project's own copy rules take precedence where they are stricter.

## Every word on a screen is one of five things

1. **A name:** a title, label, button or column heading. A name that needs a sentence beside it is the wrong name. A thing has one name everywhere, and a card's title and its button do not say it twice.
2. **A value:** the user's own data, a figure or a status, shown as a figure or a badge, once. What the product does by itself is a value (“Automatic · last ran Sun 8 Nov”), not a sentence (“Generates itself each week.”). A count that a button acts on sits on the button (“Create 12 orders”). A cell with nothing to say is empty.
3. **An answer:** shown only because something happened or is missing (empty, loading, failed, refused, saved). One line: what, and the next step where there is one. A result does not repeat figures the page already shows.
4. **A warning before harm:** only for an action that cannot be undone or that changes other records, and only in the confirmation, where the choice is made. One line. A confirmation whose title says everything has no line under it.
5. **A rule of entry the field cannot show:** a format, or what a blank or a 0 means. The field carries it where it can (a unit, a placeholder, an option that reads “Company default, £25”) before a sentence does.

Anything else is an explanation, and is designed out before the screen is specified.

## When something seems to need explaining

Work in this order, and stop at the first step that settles it:

1. **What would the user not know without it, and could anything go wrong that they cannot see and undo?** If nothing, there is nothing to write. Reassurance (“Safe to run again”), how the product works, what the page is for, what its visible controls do, and why a control is missing are all of this kind.
2. **Make the design say it.** Rename the thing. Show the fact as a value or a badge. Put the count on the button. Make the choice an option that names its own outcome. Add the unit to the field. Let a preview list what it will leave alone. Change the order of the page so what needs attention comes first.
3. **Only if no design carries it, write one line,** in its shortest form, where the decision is made, and tell the user which line you kept and what it prevents.

What someone needs in order to learn the product belongs in its guide or help, not on the working page.

## At a glance

Without reading a sentence, a page answers in this order: where am I (the title), what needs me (statuses and figures, first on the page), and what is the main thing I do here (one main button). A figure is shown only if someone acts on it, in one unit. A control that is set once belongs in settings, not on the working page.

## Shapes that show the design is not finished

- **A lead that previews the choices.** “Choose where you sell: to wholesale customers, through your own outlets, or both.” above three options that say the same. Ask the question; let the options answer it.
- **Option descriptions that restate the label.** Under an option, say only what differs between the options and matters to the choice (“Invoiced.” / “Not invoiced.”), or nothing.
- **Why an empty state is empty.** “No channels are set up yet, so there are no figures to show.” Say what is missing and the next action: “No channels yet.” “Add one in Settings → Channels.”
- **An all-clear about something that cannot exist yet.** “Every export is up to date.” before anything has been exported. When a section has nothing real to report and the page already gives the next step, the section is not shown.
