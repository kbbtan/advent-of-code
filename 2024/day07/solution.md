# Day 7: Bridge Repair

## Star 1

We can brute force all possible equations and check them against the target number.

## Star 2

We can similarly check all the possible equations with the added concatenation operator.

To improve on speed, we could implement a Dynamic Programming approach to save the calculations of subproblems. This can be implemented since the operators are always evaluated left-to-right regardless of precedence.