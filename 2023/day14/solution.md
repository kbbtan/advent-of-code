# Day 14: Parabolic Reflector Dish 

## Star 1

We can loop through each column and move the rounded rocks north as required. We do this by keeping two pointers, one that points at the last seen cubed rock (or the top of the grid), and one that sweeps the column to look for rounded rocks.

## Star 2

Given that we already know how to simulate one tilt for Star 1, we can repeat this process to complete the cycle of tilts for Star 2. However, simulating this cycle for 1 billion iterations would take too long. Drawing inspiration from a similar problem in [Day 8](../day8/solution.md), we can check if a cycle occurs anywhere along this process, and "fast-forward" that number of iterations to avoid repeat simulations.