# Day 21: Keypad Conundrum

## Star 1

Given the chain of directional keypads, the problem appears to be suited for a Dynamic Programming approach. At each keypad, we first use BFS to find all the possible paths for the next keypad, then find the shortest path among them after recursively checking through the chain of keypads. We use memoization to reuse results from previous function calls.

## Star 2

Since we already implemented a Dynamic Programming approach for Star 1, our algorithm can handle the new complexity of added keypads.