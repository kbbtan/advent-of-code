# Day 12: Garden Groups

## Star 1

We can use a standard Flood Fill algorithm for this problem on each region. The area is calculated on entering every new plot within the region, and the perimeter is calculated on every step taken out of the region.

## Star 2

We can reuse the Flood Fill idea from Star 1, but every time we step out of the region, we instead take note of the side's `(direction, row, column)` tuple. 

After completing Flood Fill, we can iterate through sides with the same `direction` to check if they can be merged together into one side. This is done by sorting them according to their row / column based on the direction, and then checking if the corresponding row / column increases incrementally by 1.