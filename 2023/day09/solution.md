# Day 9: Mirage Maintenance

## Star 1

As with most AOC Star 1s, we can implement the algorithm directly to brute force the answer.

Due to the nature of this algorithm (going back down to get the differences and coming back up), it lends itself to a recursive implementation.

## Star 2
 
We can simply re-use the algorithm we had implemented in Star 1 to predict the past value instead of the future value, since the algorithm to predict these values remain the same.