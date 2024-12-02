"""
Contains solutions for Day 21 stars.
Run on Python 3.8.3.
"""

INPUT_FILE = "input.txt"

# Constant for directions in grid.
DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

# Constants for grid character representations.
STARTING = "S"
ROCK = "#"

def star_1():
    """ Solution for Star 1.
    """
    def helper(coords, steps_left):
        """ This is a helper function to help recursively solve for subproblems.
        
            :param tuple coords: coordinates in the grid in format (row, column)
            :param int steps_left: the number of steps left to search
        """
        # If this subproblem has been seen before.
        if (coords, steps_left) in memo:
            return 
        else:
            memo.add((coords, steps_left))
        
        # Base case when there are no steps left.
        if steps_left == 0:
            possible_plots.add(coords)
            return
        
        # Continue searching in all four directions.
        for direction in DIRECTIONS:
            new_r = coords[0] + direction[0]
            new_c = coords[1] + direction[1]

            # If new coordinates are outside of bounds, ignore.
            if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                continue

            # If new coordinates hits a rock, ignore.
            if grid[new_r][new_c] == ROCK:
                continue

            # Update possible plots with those returned from subproblems.
            new_coords = (new_r, new_c)
            helper(new_coords, steps_left - 1)

    with open(INPUT_FILE) as file:
        grid = file.read().split()

    # Find the starting plot.
    starting_coords = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == STARTING:
                starting_coords = (r, c)
                break
        if starting_coords != None:
            break

    # Begin recursively searching for possible plots.
    possible_plots = set()
    memo = set()
    helper(starting_coords, 64)
    return len(possible_plots)
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split()

    # Record the shortest path to each plot in a grid.
    path_lengths = {}

    # Find the starting plot.
    starting_coords = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == STARTING:
                starting_coords = (r, c)
                break
        if starting_coords != None:
            break

    # Perform BFS to find the shortest path length to remaining plots.
    queue = [starting_coords]
    steps = 0

    while len(queue) > 0:
        new_queue = []

        for coords in queue:
            # Record path length.
            r, c = coords

            # Skip if prior path length recorded (we have visited this coordinate before).
            if coords in path_lengths:
                continue
            path_lengths[coords] = steps

            # Continue searching in all four directions.
            for direction in DIRECTIONS:
                new_r = r + direction[0]
                new_c = c + direction[1]

                # If new coordinates are outside of bounds, ignore.
                if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                    continue

                # If new coordinates hits a rock, ignore.
                if grid[new_r][new_c] == ROCK:
                    continue

                # Otherwise, add it to the next queue.
                new_queue.append((new_r, new_c))

        # Move onto the next layer.
        queue = new_queue
        steps += 1

    # Calculate each component of the formula described in the geometric solution.
    evens = len([1 for coords in path_lengths if path_lengths[coords] % 2 == 0])
    even_corners = len([1 for coords in path_lengths if path_lengths[coords] % 2 == 0 and path_lengths[coords] > 65])
    odds = len([1 for coords in path_lengths if path_lengths[coords] % 2 == 1])
    odd_corners = len([1 for coords in path_lengths if path_lengths[coords] % 2 == 1 and path_lengths[coords] > 65])
    N = round((26501365 - len(grid) / 2) / len(grid))
    
    return \
        ((N + 1) ** 2 * odds) \
        - ((N + 1) * odd_corners) \
        + ((N) ** 2 * evens) \
        + ((N) * even_corners)
        
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()