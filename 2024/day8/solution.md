# Day 8: Resonant Collinearity

## Star 1

We can iterate through every pair of antennas with the same frequency and locate the coordinates of the antinodes they form. Afterwards, we check if the antinode location is still within the grid, and if so, we add it to a set to avoid double counting locations.

## Star 2

We can reuse our logic for Star 1, but we extend our search for antinodes by considering every `n * delta` location away from the antennas, where `delta` is the difference in distance between them.