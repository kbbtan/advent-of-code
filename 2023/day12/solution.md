# Day 12: Hot Springs

## Star 1

This solution lends itself well to a Dynamic Programming solution with memoization.

We can solve subproblems by considering the first character in the record, and recursively solving for the rest of the record. We reach our base case when the record is empty, in which case we can check the remaining group records to determine if it is valid.

On every `subproblem(record, group_records)`, there are the following base cases:
1. If the `record` string is empty and `group_records` is empty, we have filled in the record completely and we return `1` to indicate this arrangement.
2. If the `record` string is empty and `group_records` is not empty, we have unallocated damaged springs and we return `0`.

Otherwise, there are the following subproblems:
1. If the first character is a `.`, we simply move on to the next character.
2. If the first character is `#`, we look ahead to check if the group matches the requirement in `group_records`. 
    - If there is a mismatch (either the group length is not appropriate or there are no remaining group records), return `0`.
    - Otherwise, we remove the first group from `group_records` and continue on with the record.
3. If the first character is a `?`, try both combinations from above.

## Star 2

The algorithm remains the same, except that we process our input differently to reflect the new unfolded records. Since we used Dynamic Programming for the previous Star, our solution can be reused and it still runs in feasible time.
 
