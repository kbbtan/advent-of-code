# Day 11: Plutonian Pebbles

## Star 1

Brute force is possible where each stone is simply expanded for 25 blinks and their total remaining stones summed up.

This lends itself to a Dynamic Programming approach as each tuple of `(stone, blinks)` is expanded multiple times in the search. We can keep a memo of previous solutions and use it to save on time.

## Star 2

With our Dynamic Programming solution for Star 1, we can reuse it for Star 2 and still have it run efficiently on the larger input.