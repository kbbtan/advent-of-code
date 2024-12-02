# Day 4: Scratchcards

## Star 1

We can obtain the solution by checking our list of numbers against the list of winning numbers. One optimization to note is that we can store the winning numbers as a set, such that we can check each of our numbers against it in `O(1)` time instead of `O(n)`. Also, one point of interest is that our points for each card can be modeled as $2^{m-1}$, where $m \geq 1$ is the number of matching numbers, instead of manually doubling it each time.

## Star 2

We can keep track of the number of scratchcards we have using a dictionary structure. Then, we can reuse the same logic in Star 1 to count the number of matches for each card once, and multiply it by the number of scratchcards we have.