# Day 9: Disk Fragmenter

## Star 1

We keep two pointers, one pointing to the first empty block, and one pointing to the last file block. Then, continually move the last file block to the first empty block until the pointers intersect.

## Star 2

This could also be done in a brute force manner with additional pointers to represent the `(start, end)` of empty / file blocks. For each file block, we need to sweep the disk to find the leftmost empty block that can fit it, resulting in a time complexity of $O(n^2)$.

A more involved solution is to use a dictionary to keep track of empty blocks. The keys are the empty block sizes, and they each hold a min-heap sorted by the position of the empty blocks. This allows us to efficiently find the leftmost empty block that can fit each file block, cutting down the time complexity to $O(n \log n)$.