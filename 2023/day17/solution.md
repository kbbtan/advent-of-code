# Day 17: Clumsy Crucible

## Star 1

We can solve this problem using a Dijkstra pathfinding algorithm to search through the grid of blocks. Each state is represented by its coordinate on the grid and the last direction it had taken (either vertical or horizontal). When leaving a state, we project all of its steps in the perpendicular direction for `[1, 3]` steps, then force it to turn. This ensures that the maximum number of steps condition is always met.

## Star 2
 
We can mostly reuse our code for the next star, simply updating the projection step to project outwards for `[4, 10]` steps instead of the `[1, 3]` steps required for Star 1.