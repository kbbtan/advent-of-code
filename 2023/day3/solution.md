# Day 3: Gear Ratios

## Star 1

We can treat the engine schematic as an undirected graph, where every character is connected to all of its adjacent characters. When we encounter a valid symbol, we can first check its neighbors to see if it is connected to any digits, then continue to traverse the digits until the full number is uncovered. To avoid double-counting digits, we can set them to periods (`.`) after we count them the first time.

## Star 2

We can apply similar logic to traverse through the engine schematic, but instead we now identify stars (`*`) that are adjacent to exactly two numbers, multiply them together and get the total of these products. We also want to change the schematic back to its original state after checking each star, such that the numbers can still be considered for subsequent stars.