# Day 14: Restroom Redoubt

## Star 1

We can iterate through each robot and calculate their final positions. Since the row and column indicies loop independently, we can also calculate each of them separately.

## Star 2

This is a very interesting question as it appears to be visual based.

Since the problem asks for the `fewest number of seconds`, we can loop through all possibilities of the robots' positions until we detect that a previous position has been seen.

Then, to define the Christmas tree, we can conceptualize it as the set of robots' positions which will result in the least variance between the positions. After checking all unique possibilities of robots' positions (which takes a few seconds), this gives us the solution nicely. Set `show_tree=True` for the `star_2` function for the tree to be visualized.