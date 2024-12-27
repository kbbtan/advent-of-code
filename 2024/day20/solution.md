# Day 20: Race Condition

## Star 1

We first traverse the racetrack to find the distances to each track grid. Then, we traverse the racetrack again, but for each track grid, we find all track grids reachable within two grids regardless of walls. Then, we can use their pre-computed distances to find the amount of time saved.

## Star 2

This problem is similar to Star 1, but we expand the search space to search for all track grids reachable within **twenty** grids for each track grid.