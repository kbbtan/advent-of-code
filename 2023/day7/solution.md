# Day 7: Camel Cards

## Star 1

This solution is relatively straightforward in implementation, but the tedious part lies in making sure that we consider all possible cases when we determine the type of the hands. We first sort the hands into their types by considering the composition of the hands. For example, if we have 3 different labels and the composition is 3-1-1, it is a three of a kind, but if it is 2-2-1, it is a two pair. Then, we can sort these hands within each of their types according to the strength of their individual cards, giving us the hands sorted by rank.

## Star 2

This problem is similar to Star 1, except that we have to be more careful with considering our cases with the addition of the Joker as a wildcard. Implementation wise, this essentially results in the addition of more `if` statements. As long as we sort the hands into their correct types, the remaining logic will sort the hands properly into their corresponding ranks.

An edge case that I failed to spot initially was that in the case of a hand with composition 2-2-1, if there is 1 Joker in the hand, it becomes a **Full House**, not **Three of a Kind**. Credits to the test input provided by [u/LxsterGames](https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/) which helped to debug this issue.