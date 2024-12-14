"""
Contains solutions for Day 14 stars.
Run on Python 3.12.8.
"""
import re
import statistics
 
INPUT_FILE = "input.txt"

# Number of iterations (seconds).
SECONDS = 100

# Dimensions of the space.
GRID_R = 103
HALF_R = GRID_R // 2
GRID_C = 101
HALF_C = GRID_C // 2

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")
        values = [list(map(lambda x: int(x), re.findall(r"-?\d+", line))) for line in lines]

    # Stores final dimensions for the robots.
    final_positions = []

    for value in values:
        c, r, dc, dr = value
        r = (r + dr * SECONDS) % GRID_R
        c = (c + dc * SECONDS) % GRID_C
        final_positions.append((r, c))

    # Figure out which quadrant each robot is in.
    top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0
    for final_position in final_positions:
        r, c = final_position

        # Top-Left Quadrant.
        if r < HALF_R and c < HALF_C:
            top_left += 1

        # Top-Right Quadrant.
        elif r < HALF_R and c > HALF_C:
            top_right += 1

        # Bottom-Left Quadrant.
        elif r > HALF_R and c < HALF_C:
            bottom_left += 1

        # Bottom-Right Quadrant.
        elif r > HALF_R and c > HALF_C:
            bottom_right += 1
        
    return top_left * top_right * bottom_left * bottom_right
    
def star_2(show_tree=False):
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")
        values = [list(map(lambda x: int(x), re.findall(r"-?\d+", line))) for line in lines]

    # Stores the positions and velocities of the robots.
    positions_r, positions_c, velocities_r, velocities_c = [], [], [], []
    for value in values:
        c, r, dc, dr = value
        positions_r.append(r)
        positions_c.append(c)
        velocities_r.append(dr)
        velocities_c.append(dc)

    # Keep looping over more iterations until we see a repeat.
    t = 0
    seen = set()
    min_variance, min_grid, min_t = float("inf"), None, -1

    while (tuple(positions_r), tuple(positions_c)) not in seen:
        # Add these positions to the ones we've already seen.
        seen.add((tuple(positions_r), tuple(positions_c)))
        
        # Perform one update of positions.
        new_positions_r, new_positions_c = [], []
        for i in range(len(positions_r)):
            new_positions_r.append((positions_r[i] + velocities_r[i]) % GRID_R)
            new_positions_c.append((positions_c[i] + velocities_c[i]) % GRID_C)
        
        # Move to the next iteration.
        t += 1
        positions_r = new_positions_r
        positions_c = new_positions_c

        # If we find a new minimum variance,
        # update the new minimum variance with its cooresponding grid and time interval.
        new_variance = statistics.variance(positions_r) + statistics.variance(positions_c)
        if new_variance < min_variance:
            min_variance = new_variance
            min_t = t

            grid = [["." for c in range(GRID_C)] for _ in range(GRID_R)]
            for i in range(len(positions_r)):
                grid[positions_r[i]][positions_c[i]] = "#"
            min_grid = grid

    if show_tree:
        for row in min_grid:
            print("".join(row))

    return min_t
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()