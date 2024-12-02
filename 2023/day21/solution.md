# Day 21: Step Counter 

## Star 1

This problem can be represented as a Dynamic Programming problem with subproblems represented by their `(coordinates, steps_left)`. Base cases are when `steps_left == 0`, in which case the only plot reachable is the plot itself. We propagate these reachable plots upwards, making sure to account for repeated plots.

## Star 2
 
Given the extremely large number of steps `26501365`, it is infeasible to map out the path to every single plot. Typically, such AOC problems require you to recognize some form of pattern in the problem, such that we can "simulate" computation by looping over this pattern.

For instance, one pattern that can be observed is that once a tile is reached, it can always be reached every 2 steps onwards (stepping off and on it again). Hence, this results in a binary split for the garden plots. Given an infinite number of steps, each plot is either reachable using an odd number of steps, or an even number of steps.

However, we still require a method of knowing how much space the `26501365` steps we are given can cover in the infinite grid. This can be done by observing that from the centre of a grid, the direct paths in all eight directions (vertical, horizonal and diagonal) are all clear. Hence, the maximum distance covered can be represented as a diamond shape over the infinite grid. Credits to [villuna](https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21) for making this observation and for providing an excellent visual representation of the solution.