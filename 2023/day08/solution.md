# Day 8: Haunted Wasteland

## Star 1

The solution can be done through brute-force. Simply follow the instructions, looping around as necessary, until we find Z.

## Star 2

We could brute force the solution, but it would take too long to find an exact step that results in all nodes landing on Z.

To solve this, the key observation to make is that once you reach a node that ends with Z, the next step always brings you to the second node in the path you took, i.e. once you reach a node that ends with Z, the number of steps to get back to the node is constant.

With this in mind, we can simply find the number of steps it takes to get to a Z node for each start node, and then take their LCM to get the answer without simulating the whole sequence of steps.

Credits to this [Stackoverflow Post](https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-the-least-common-multiple) for the algorithm to efficiently compute the lowest common divisior of two numbers.