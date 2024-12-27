"""
Contains solutions for Day 18 stars.
Run on Python 3.12.8.
"""
# Size of the memory space.
MEM_ROWS = 71
MEM_COLS = 71

# Bytes to consider.
BYTES_FALLEN = 1024

# Coordinate directions for moving up, right, down, left.
D_4 = [(1, 0), (0, 1), (0, -1), (-1, 0)]
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    # Construct the grid.
    # Represent empty spaces as False.
    grid = [[False for c in range(MEM_COLS)] for r in range(MEM_ROWS)]

    with open(INPUT_FILE) as file:
        coords = file.read().split()

        for coord in coords[:BYTES_FALLEN]:
            r, c = coord.split(",")
            grid[int(r)][int(c)] = True

    # Find the shortest path using BFS.
    curr_layer = [(0, 0)]
    seen = set()
    path_length = -1
    found = False

    while not found:
        path_length += 1
        next_layer = []

        for coord in curr_layer:
            # If we have reached the end, stop searching.
            if coord == (len(grid) - 1, len(grid[0]) - 1):
                found = True
                break

            # If seen before, skip.
            if coord in seen:
                continue
            else:
                seen.add(coord)

            # Try going in all four directions.
            for direction in D_4:
                new_r, new_c = coord[0] + direction[0], coord[1] + direction[1]

                # If out of bounds, skip.
                if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                    continue

                # If spot is corrupted, skip.
                if grid[new_r][new_c] == True:
                    continue

                # Add new coord to traverse.
                next_layer.append((new_r, new_c))

        curr_layer = next_layer

    return path_length
    
def star_2():
    """ Solution for Star 2.
    """
    # Construct the grid.
    # Represent empty spaces as False.
    grid = [[False for c in range(MEM_COLS)] for r in range(MEM_ROWS)]

    with open(INPUT_FILE) as file:
        coords = file.read().split()

        for coord in coords[:BYTES_FALLEN]:
            r, c = coord.split(",")
            grid[int(r)][int(c)] = True

    for coord in coords[BYTES_FALLEN:]:
        # Add fallen byte to the grid.
        r, c = coord.split(",")
        grid[int(r)][int(c)] = True

        # Find the shortest path using BFS.
        curr_layer = [(0, 0)]
        seen = set()
        found = False

        while len(curr_layer) > 0:
            next_layer = []

            for curr in curr_layer:
                # If we have reached the end, stop searching.
                if curr == (len(grid) - 1, len(grid[0]) - 1):
                    found = True
                    break

                # If seen before, skip.
                if curr in seen:
                    continue
                else:
                    seen.add(curr)

                # Try going in all four directions.
                for direction in D_4:
                    new_r, new_c = curr[0] + direction[0], curr[1] + direction[1]

                    # If out of bounds, skip.
                    if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                        continue

                    # If spot is corrupted, skip.
                    if grid[new_r][new_c] == True:
                        continue

                    # Add new coord to traverse.
                    next_layer.append((new_r, new_c))

            # If valid path is found, break out of the loop.
            if found:
                break

            curr_layer = next_layer

        # If valid path is not found, this is the byte that cuts off all paths.
        if not found:
            return coord

    return -1
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()