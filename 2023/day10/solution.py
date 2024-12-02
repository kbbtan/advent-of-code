"""
Contains solutions for Day 10 stars.
Run on Python 3.8.3.
"""
from collections import deque

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    # Define the neighbors of each possible graph character.
    NEIGHBOR_MAP = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)]
    }

    # Represent the input as a 2D array.
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda row: list(row), grid))

    # Implement BFS using a queue.
    # Nodes are stored in a ((row, column), step) format.
    seen_pipes = set()
    queue = deque([])
    max_steps = 0

    # Find the start point.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                # Add start point to the queue.
                queue.append(((r, c), 0))

                # Figure out its neighbors.
                S_neighbors = []
                for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r, new_c = r + direction[0], c + direction[1]

                    # Checks are out of bounds.
                    if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                        continue

                    pipe = grid[new_r][new_c]

                    # Valid pipe characters to the bottom of the start position.
                    if direction == (1, 0) and (pipe == "|" or pipe == "L" or pipe == "J"):
                        S_neighbors.append(direction)

                    # Valid pipe characters to the top of the start position.
                    elif direction == (-1, 0) and (pipe == "|" or pipe == "7" or pipe == "F"):
                        S_neighbors.append(direction)

                    # Valid pipe characters to the left of the start position.
                    elif direction == (0, -1) and (pipe == "-" or pipe == "L" or pipe == "F"):
                        S_neighbors.append(direction)

                    # Valid pipe characters to the right of the start position.
                    elif direction == (0, 1) and (pipe == "-" or pipe == "J" or pipe == "7"):
                        S_neighbors.append(direction)

                # Replace S with its corresponding pipe.
                for pipe in NEIGHBOR_MAP:
                    if NEIGHBOR_MAP[pipe] == S_neighbors:
                        grid[r][c] = pipe

                break

    while len(queue) > 0:
        coords, steps = queue.popleft()

        # We have seen this location before.
        if coords in seen_pipes:
            continue

        # Add each neighbor to the next layer.
        for direction in NEIGHBOR_MAP[grid[coords[0]][coords[1]]]:
            queue.append(((coords[0] + direction[0], coords[1] + direction[1]), steps + 1))

        # Indicate that we have traversed this location.
        # If we end up here again we won't traverse it.
        seen_pipes.add(coords)

        # Record the number of steps at this location.
        max_steps = max(max_steps, steps)

    return max_steps, seen_pipes, grid
    
def star_2():
    """ Solution for Star 2.
    """
    # Define the mapping for our expanded grid.
    EXPANDED_MAPPING = {
        "|": [
            [".", "|", "."],
            [".", "|", "."],
            [".", "|", "."]
        ],
        "-": [
            [".", ".", "."],
            ["-", "-", "-"],
            [".", ".", "."]
        ],
        "L": [
            [".", "|", "."],
            [".", "L", "-"],
            [".", ".", "."]
        ],
        "J": [
            [".", "|", "."],
            ["-", "J", "."],
            [".", ".", "."]
        ],
        "7": [
            [".", ".", "."],
            ["-", "7", "."],
            [".", "|", "."]
        ],
        "F": [
            [".", ".", "."],
            [".", "F", "-"],
            [".", "|", "."]
        ],
    }

    # Use our solution from Star 1 to obtain a set of pipe locations.
    _, pipe_locations, grid = star_1()

    # Increase the resolution of each pipe to encompass a 3x3 space.
    expanded_grid = [["." for j in range(len(grid[0]) * 3)] for i in range(len(grid) * 3)]

    # Map pipes in the main loop into the expanded grid.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # The location is a pipe and is not a junk pipe.
            if grid[r][c] != "." and (r, c) in pipe_locations:
                # Get the 3x3 mapping.
                pipe = grid[r][c]
                mapping = EXPANDED_MAPPING[pipe]

                # The top left coordinates of each 3x3 subgrid.
                sub_r = r * 3
                sub_c = c * 3

                # Copy over each position from the expanded resolution mapping.
                for i in range(3):
                    for j in range(3):
                        expanded_grid[sub_r + i][sub_c + j] = mapping[i][j]



    # Perform Flood Fill on the expanded grid to identify tiles not in the loop.
    queue = deque([])

    # Add all edge tiles which are not pipes.
    for c in range(len(expanded_grid[0])):
        queue.append((0, c))
        queue.append((len(expanded_grid) - 1, c))
    for r in range(1, len(expanded_grid) - 1):
        queue.append((r, 0))
        queue.append((r, len(expanded_grid[0]) - 1))

    # Perform Flood Fill.
    while len(queue) > 0:
        coords = queue.popleft()
        r, c = coords
        
        # If location has already been marked.
        if expanded_grid[r][c] != ".":
            continue

        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r = r + direction[0]
            new_c = c + direction[1]

            # Checks are out of bounds.
            if new_r < 0 or new_r >= len(expanded_grid) or new_c < 0 or new_c >= len(expanded_grid[0]):
                continue

            # Add adjacent empty tiles to the queue.
            if expanded_grid[new_r][new_c] == ".":
                queue.append((new_r, new_c))

        # Mark location as checked.
        expanded_grid[r][c] = "O"

    # Check for remaining empty tiles (tiles left are enclosed within the loop).
    # Only check for the center tile in each 3x3 grid - corresponds to tile in original grid.
    enclosed_tiles = 0
    for r in range(0, len(expanded_grid), 3):
        for c in range(0, len(expanded_grid[0]), 3):
            if expanded_grid[r + 1][c + 1] == ".":
                enclosed_tiles += 1

    return enclosed_tiles
    
def main():
    """ Contains driver code for running solutions.
    """
    star_1_sol, _, _ = star_1()
    print("Solution for Star 1: ", star_1_sol)
    print("Solution for Star 2: ", star_2())

main()