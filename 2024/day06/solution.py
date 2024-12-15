"""
Contains solutions for Day 6 stars.
Run on Python 3.12.8.
"""
# Mappings for the change in direction after turning right.
RIGHT = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}
 
INPUT_FILE = "input.txt"

def star_1(ans=True):
    """ Solution for Star 1.
    """
    # Read input as a 2D array.
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")
        grid = list(map(lambda x: list(x), grid))
        
    # Records current coordinates and direction.
    start = None
    dir = (-1, 0)

    # Set of coordinates seen to avoid repeating coordinates.
    seen = set()

    # Find the coordinates of the starting character.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                start = (i, j)
                break
        if start:
            break

    curr = start
    # While current coordinates are still within the grid.
    while curr[0] in range(len(grid)) and curr[1] in range(len(grid[0])):
        # Record coordinates and direction.
        seen.add(curr)

        # Try moving one step in specified direction.
        new_pos = (curr[0] + dir[0], curr[1] + dir[1])

        # If new position is out of range, path ends.
        if not (new_pos[0] in range(len(grid)) and new_pos[1] in range(len(grid[0]))):
            break

        # If new position is an obstacle, turn right instead.
        elif grid[new_pos[0]][new_pos[1]] == "#":
            dir = RIGHT[dir]
            continue

        # Otherwise, new position is valid and we take the step.
        else:
            curr = new_pos

    # Return the answer.
    if ans:
        return len(seen)
    
    # Return other parameters for Star 2.
    else:
        return grid, seen, start

    
def star_2():
    """ Solution for Star 2.
    """
    # Use Star 1 code to obtain set of coordinates along original path.
    grid, original_seen, start = star_1(ans=False)

    # Record new obstacle locations.
    new_obs = set()

    # Try placing a new obstacle on every coordinate along original path except start.
    for coord in original_seen:
        # We can't place a new obstacle on the starting tile.
        if coord == start:
            continue

        # Add an obstacle and simulate guard movement.
        grid[coord[0]][coord[1]] = "#"
        is_cycle = False
        
        # Records current coordinates and direction.
        curr = start
        dir = (-1, 0)

        # Set of (coordinates, dir) to detect cycles.
        seen = set()

        # While current coordinates are still within the grid.
        while curr[0] in range(len(grid)) and curr[1] in range(len(grid[0])):
            # If combination of current coordinates and direction have been seen, a cycle has occurred.
            if (curr, dir) in seen:
                is_cycle = True
                break

            # Record coordinates and direction.
            else:
                seen.add((curr, dir))

            # Try moving one step in specified direction.
            new_pos = (curr[0] + dir[0], curr[1] + dir[1])

            # If new position is out of range, path ends.
            if not (new_pos[0] in range(len(grid)) and new_pos[1] in range(len(grid[0]))):
                break

            # If new position is an obstacle, turn right instead.
            elif grid[new_pos[0]][new_pos[1]] == "#":
                dir = RIGHT[dir]
                continue

            # Otherwise, new position is valid and we take the step.
            else:
                curr = new_pos

        # If a cycle was detected, add location to new_obs.
        if is_cycle:
            new_obs.add(coord)

        # Remove the obstacle.
        grid[coord[0]][coord[1]] = "."

    return len(new_obs)
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()