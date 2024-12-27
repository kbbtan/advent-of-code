# Day 19: Linen Layout

## Star 1

If one of our towels can be placed at the front of the pattern, we can recursively check if the rest of the pattern can be completed by our towels. We can also implement a memoization table for repeat computations.

## Star 2

We can implement a similar structure as the algorithm for Star 1, but each time we find a valid arrangement, we add 1 to the total instead of returning `True`.