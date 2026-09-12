# Direct Delivery

Use this workflow for one clear, bounded change that can be implemented and verified inline. An existing story or package remains authoritative but does not by itself require a deeper route.

Read [Delivery controls](../references/delivery-controls.md) before editing. When the selected unit is a packet within a multi-packet story or package, also read [Packet coordination](../references/packet-coordination.md); its continuation, safety gate, and commit boundary apply even on this route.

Run implementation and routine affected verification inline; do not use a worker merely because this route was selected. Independent assurance remains available when the delivery controls require it.

1. Confirm the owned outcome and inspect only the code, contracts, current diff, and project rules needed to locate the real change surface.
2. Establish the smallest meaningful failing or observable check when practical. For a no-code or non-testable change, identify equivalent acceptance evidence.
3. Make the smallest cohesive change at the lowest shared cause. Preserve unrelated work and avoid opportunistic cleanup.
4. Run the narrow affected checks, inspect the complete selected-unit diff (the packet delta when packet coordination applies), and broaden verification only when shared contracts or risk require it.
5. Apply the completion and close rules in the delivery controls. Every direct-delivery session closes through `close-session`: use packet close when the selected unit is a named packet or slice, otherwise full close.

Do not create a delivery record merely for traceability. If discovery exposes coupled packets, material uncertainty, a critical domain, several review slices, or durable continuation need, stop before broad edits, preserve the current record and evidence, and select coordinated or staged delivery.
