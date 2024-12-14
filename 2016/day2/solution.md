# Day 2: Bathroom Security

## Star 1

We can simply loop through each instruction and attempt to update our current position. If we ever step out of bounds, we ignore the step and carry on.

## Star 2

We can repeat the same process as Star 1. To handle the irregular shape of the new keypad, we can use `None` for the empty positions and add an additional check when we step into them.