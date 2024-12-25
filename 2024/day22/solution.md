# Day 22: Monkey Market

## Star 1

We can brute force the secret numbers following the pseudorandom algorithm given.

## Star 2

We can reuse the same algorithm as in Star 1, but take note of the first time a sequence of price changes occurs for each buyer and add it to a running total between all buyers. This can be done as we know that the monkey will immediately sell once a sequence is observed for the first time.