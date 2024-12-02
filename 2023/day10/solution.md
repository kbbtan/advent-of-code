# Day 10: Pipe Maze

## Star 1

I would say that the most troublesome part of this Star is translating the input format into a searchable format.

Then, the solution can be found using your standard search algorithm of choice (BFS / DFS etc.).

## Star 2
 
Star 2 can be solved using a standard flood fill algorithm, but with the following caveats
- pipes not belonging to the main loop (junk pipes) can be considered enclosed
- "squeezing" between pipes is allowed

The first caveat can be solved by marking junk pipes as empty tiles. We know which pipes belong to the main loop using what we've implemented for Star 1, and for the purposes of Flood Fill, the junk pipes are no different from the empty tiles.

The second caveat is really the key problem behind this Star. To solve it, we can increase the resolution of our puzzle space by representing each pipe as a 3x3 grid. 

For instance, consider the following mapping in the example input:
```
7F
......
-7..F-
.|..|.
```

By expanding the resolution of our grid, we reveal the "hidden" pathways between the pipes. Then, we can implement a standard Flood Fill algorithm on this expanded grid to solve our problem.

2:10