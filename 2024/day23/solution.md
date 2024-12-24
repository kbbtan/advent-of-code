# Day 23: LAN Party

## Star 1

We can naively brute-force all combinations of three computers and check if they are inter-connected (and also if they start with `t`).

## Star 2

Note that Star 1 already gives us [cliques](https://en.wikipedia.org/wiki/Clique_problem) of size 3. Given a clique of size 3, we can iteratively check the remaining computers in the network to see if they can each be added to the clique. 

Note that this problem is [NP-complete](https://en.wikipedia.org/wiki/NP-completeness), but the input size is small enough such that the algorithm completes relatively quickly.