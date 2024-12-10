# Day 10: Hoof It

## Star 1

We can perform a search algorithm (e.g. DFS) from every trailhead and identify the `9`s reachable. We can use a set to keep track of the `9` coordinates to prevent overcounting.

## Star 2

Notice that the number of unique hiking trails per trailhead can also be represented by how many times a `9` is reached from that trailhead. If the same `9` is reached multiple times, different unique paths were used to reach it. Hence, we can solve this Star by making a small tweak to our code for Star 1 to allow overcounting.