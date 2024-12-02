# Day 13: Point of Incidence

## Star 1

For this star, we can check for the reflection in each pattern through brute force, looping through each mirror and checking if that makes the pattern symmetrical.

One improvement we can make is to store each row and column as a binary integer, where 1 represents rocks (#) and 0 represents ash (.). Then, for each row / column on opposite ends of the mirror, we can check for their equality in `O(1)` time instead of looping through each of their characters. 


## Star 2
 
For this star, we can reuse the same algorithm as for Star 1.

The only difference is that in this case, instead of checking which reflections make the reflections exactly equal, we are checking for which reflections are off by exactly one character. In the case of our bit representation, we check for a single bit leftover after XORing the reflections with each other.