"""
Contains solutions for Day 20 stars.
Run on Python 3.12.8.
"""
# Coordinate directions for moving up, right, down, left.
D_4 = [(1, 0), (0, 1), (0, -1), (-1, 0)]

# Character constants for the grid.
START = "S"
END = "E"
WALL = "#"
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        grid = list(map(list, file.read().split()))

    # Find coords of start and end spaces.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == START:
                start = (r, c)
            if grid[r][c] == END:
                end = (r, c)

    # Store shortest distance to all non-wall spaces.
    shortest_distances = {}

    # Perform BFS to find the shortest distance to all non-wall spaces.
    curr_layer = [start]
    path_length = 0

    while len(curr_layer) > 0:
        next_layer = []

        for coords in curr_layer:
            # If seen before, skip.
            if coords in shortest_distances:
                continue

            # Record shortest path to this coords.
            else:
                shortest_distances[coords] = path_length

            # Try going in four directions.
            for direction in D_4:
                next_r, next_c = coords[0] + direction[0], coords[1] + direction[1]

                # If out of bounds, skip.
                if next_r < 0 or next_r >= len(grid) or next_c < 0 or next_c >= len(grid[0]):
                    continue

                # If hit a wall, skip.
                if grid[next_r][next_c] == WALL:
                    continue

                # Add to traverse.
                next_layer.append((next_r, next_c))

        # Move to the next layer.
        path_length += 1
        curr_layer = next_layer

    num_cheats = 0

    # For each empty space on the racetrack.
    for coords in shortest_distances:
        wall_coords = []

        # Find walls in all directions.
        for direction in D_4:
            new_r, new_c = coords[0] + direction[0], coords[1] + direction[1]

            # If out of bounds, skip.
            if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                continue

            # If it is a wall, record it.
            if grid[new_r][new_c] == WALL:
                wall_coords.append((new_r, new_c))

        # From those walls, find empty spaces to skip to.
        for wall_coord in wall_coords:
            for direction in D_4:
                new_r, new_c = wall_coord[0] + direction[0], wall_coord[1] + direction[1]

                # If out of bounds, skip.
                if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                    continue

                # If next spot is a wall, skip.
                if grid[new_r][new_c] == WALL:
                    continue

                # Check if the cheat helps enough.
                cheat_skip = shortest_distances[(new_r, new_c)] - shortest_distances[coords] - 2
                if cheat_skip >= 100:
                    num_cheats += 1

    return num_cheats
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        grid = list(map(list, file.read().split()))

    # Find coords of start and end spaces.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == START:
                start = (r, c)
            if grid[r][c] == END:
                end = (r, c)

    # Store shortest distance to all non-wall spaces.
    shortest_distances = {}

    # Perform BFS to find the shortest distance to all non-wall spaces.
    curr_layer = [start]
    path_length = 0

    while len(curr_layer) > 0:
        next_layer = []

        for coords in curr_layer:
            # If seen before, skip.
            if coords in shortest_distances:
                continue

            # Record shortest path to this coords.
            else:
                shortest_distances[coords] = path_length

            # Try going in four directions.
            for direction in D_4:
                next_r, next_c = coords[0] + direction[0], coords[1] + direction[1]

                # If out of bounds, skip.
                if next_r < 0 or next_r >= len(grid) or next_c < 0 or next_c >= len(grid[0]):
                    continue

                # If hit a wall, skip.
                if grid[next_r][next_c] == WALL:
                    continue

                # Add to traverse.
                next_layer.append((next_r, next_c))

        # Move to the next layer.
        path_length += 1
        curr_layer = next_layer

    num_cheats = 0

    # For each empty space on the racetrack.
    for coords in shortest_distances:
        # Try all possible cheats lasting up to 20 picoseconds.
        # Search this space using BFS.
        curr_layer = [coords]
        seen = set()

        for cheat_length in range(21):
            next_layer = []

            for next_coords in curr_layer:
                # If seen before, skip.
                if next_coords in seen:
                    continue
                else:
                    seen.add(next_coords)

                # If coords has a shortest distance, check if the cheat is good enough.
                if next_coords in shortest_distances:
                    cheat_skip = shortest_distances[next_coords] - shortest_distances[coords] - cheat_length
                    if cheat_skip >= 100:
                        num_cheats += 1

                # Try going in four outward directions.
                for direction in D_4:
                    next_r, next_c = next_coords[0] + direction[0], next_coords[1] + direction[1]

                    # If out of bounds, skip.
                    if next_r < 0 or next_r >= len(grid) or next_c < 0 or next_c >= len(grid[0]):
                        continue

                    # Expand in all directions.
                    next_layer.append((next_r, next_c))

            curr_layer = next_layer

    return num_cheats
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()