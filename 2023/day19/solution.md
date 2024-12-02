# Day 19: Aplenty

## Star 1

For this star, we can implement the algorithm given as-is and get the Star. The main problem lies around string processing and digesting the input into a usable format.

## Star 2
 
Since the number of possible parts is too many, we can no longer brute force every possible part and check if they are accepted. Instead, we can treat the workflows as a graph to traverse, and keep track of the combination of conditions that occur at the "accept" node.