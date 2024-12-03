# Day 3: Mull It Over

## Star 1

We can implement this as a regex problem, where we only extract the valid (uncorrupted) `mul` instructions based on the syntax given.

## Star 2

We can implement this similar to Star 1, but we also extract valid `do` and `don't` instructions. 

Then, we implement a global `toggle` to keep track of the last `do` / `don't` instruction, while only applying the `mul` instructions as necessary.