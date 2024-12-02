# Day 16: The Floor Will Be Lava

## Star 1

For this star, we can represent each tile on the grid as a series of states `(row, column, direction)`, where `direction` is the direction the beam of light is currently travelling. Then we can use a search algorithm to identify which tiles become energized.

## Star 2
 
For this star, we can replicate the algorithm for Star 1, but just repeat it on different starting states to represent entering the grid from different edge tiles and compare their results.