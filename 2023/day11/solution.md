# Day 11: Cosmic Expansion

## Star 1

Another search problem following from Day 10. One observation is that instead of expanding the universe, we can keep track of which rows / columns are empty, and update the steps accordingly when a path passes through them.

## Star 2
 
Similar to Star 1, except that empty rows are now expanded by a factor of 1,000,000 instead of twice. Luckily, due to our observation for Star 1, we can just change how much we update the steps when a path passes through an empty row / column.