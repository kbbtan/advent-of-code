# Day 6: Guard Gallivant

## Star 1

We can simulate the guard movement in the grid and keep track of how many unique positions were visited using a set.

## Star 2

We can detect if a loop has occured if the guard enters a previous **position** facing the same **direction**. One brute force solution is to try inserting a new obstacle at every possible location on the grid, but we can optimize this by observing that only obstacles placed along the original path would change the guard's path. 

Another possible optimization which I left unimplemented is to keep track of the coordinates of obstacles along each row and column. Then, we can jump the guard to the next obstacle without having to simulate every step.