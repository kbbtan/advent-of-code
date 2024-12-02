# Day 5: If You Give A Seed A Fertilizer

## Star 1

The most tedious part of this solution was extracting the variables we needed from the format of the input file. Once we have that sorted, we can apply the algorithm given to us to obtain the solution.

## Star 2

Given that we are now working with seed ranges, the previous solution no longer works as considering the conversions for each seed would be too time consuming. Hence, we need to perform conversions on entire seed ranges. When comparing seed ranges to mappings, there are five cases to consider. Let the mapping's start and end numbers be `mapping_start` and `mapping_end`, and the source item's start and end numbers be `item_start` and `item_end`:

1. `mapping_start > item_end || mapping_end < item_start`. The mapping range is completely outside of the item range and we can ignore this mapping.
2. `mapping_start > item_start && mapping_end < item_end`. The item range is split into three subsets and only the middle subset captured by the mapping can be mapped. For the remaining two subsets, we need to continue attempting to find mappings for them. 
3. `mapping_start > item_start`. The item range is split into two subsets and only the right subset captured by the mapping can be mapped. For the left subset, continue attempting to find mappings for it.
4. `mapping_end < item_end`. Similar to case 3 but with the left and right subsets flipped.
5. Otherwise, we know that the mapping captures the entire item range. We can use the mapping to map the entire seed range.

We can also make use of a stack to store source item ranges, such that we can push the new subset ranges we create back into the stack to continue finding mappings for them.