# Day 1: Trebuchet?!

## Star 1

The solution can be obtained by following the steps as described in the problem. Identify the first and last digit in each line of the puzzle input, concatenate them, and get their sum as integers.

## Star 2

This problem is similar to Star 1, but digits can now be represented in their word equivalents (e.g. "one" represents "1"). One solution is to add a helper function which can identify these words and convert them to their digit equivalents as we loop through each line, and then apply the same steps taken for Star 1 to these digits.