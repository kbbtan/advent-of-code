"""
Contains solutions for Day 12 stars.
Run on Python 3.12.8.
"""
from collections import defaultdict, deque
import re

# Coordinate directions for moving up, right, down, left.

# Mapping for sides.
UP = "u"
DOWN = "d"
RIGHT = "r"
LEFT = "l"

D_4 = {
    UP: (-1, 0), 
    DOWN: (1, 0), 
    RIGHT: (0, 1), 
    LEFT: (0, -1)
}
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")

    price = 0
        
    # Mark plots which have been visited.
    # True if visited, False otherwise.
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # Start a new flood fill from this plot.
            if not visited[r][c]:
                stack = [(r, c)]
                plant = grid[r][c]
                area = 0
                perimeter = 0

                while len(stack) > 0:
                    curr = stack.pop()
                    curr_r, curr_c = curr

                    # Skip if this plot has been covered before.
                    if visited[curr_r][curr_c]:
                        continue
                    # Mark plot as visited and count its area.
                    else:
                        visited[curr_r][curr_c] = True
                        area += 1

                    # Search in 4 non-diagonal directions.
                    for side in D_4:
                        direction = D_4[side]
                        new_r, new_c = curr_r + direction[0], curr_c + direction[1]

                        # Taking this step goes out of bounds. Counts as a perimeter.
                        if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                            perimeter += 1
                            continue

                        # Taking this step goes to another plant. Also counts as a perimeter.
                        if grid[new_r][new_c] != plant:
                            perimeter += 1
                            continue

                        # Add next plot to the stack for flood fill.
                        stack.append((new_r, new_c))

                # Finished flooding the plant area.
                # Calculate cost for this region.
                price += perimeter * area

    return price
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")

    price = 0
        
    # Mark plots which have been visited.
    # True if visited, False otherwise.
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # Start a new flood fill from this plot.
            if not visited[r][c]:
                stack = [(r, c)]
                plant = grid[r][c]
                area = 0

                # Store sides indexed by the type of side ("u" / "d" / "r" / "l")
                # and with values as grid coordinates.
                sides = {UP: [], DOWN: [], RIGHT: [], LEFT: []}

                while len(stack) > 0:
                    curr = stack.pop()
                    curr_r, curr_c = curr

                    # Skip if this plot has been covered before.
                    if visited[curr_r][curr_c]:
                        continue
                    # Mark plot as visited and count its area.
                    else:
                        visited[curr_r][curr_c] = True
                        area += 1

                    # Search in 4 non-diagonal directions.
                    for side in D_4:
                        direction = D_4[side]
                        new_r, new_c = curr_r + direction[0], curr_c + direction[1]

                        # Taking this step goes out of bounds. Counts as a perimeter.
                        if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                            sides[side].append((curr_r, curr_c))
                            continue

                        # Taking this step goes to another plant. Also counts as a perimeter.
                        if grid[new_r][new_c] != plant:
                            sides[side].append((curr_r, curr_c))
                            continue

                        # Add next plot to the stack for flood fill.
                        stack.append((new_r, new_c))

                # Finished flooding the plant area.
                # Begin to calculate the number of sides.
                sides_num = 0
                for side in sides:
                    coords = sides[side]

                    # Merge sides horizontally.
                    if side == UP or side == DOWN:
                        coords = sorted(coords, key=lambda x: x[1])
                        coords = sorted(coords, key=lambda x: x[0])

                        for i in range(len(coords) - 1):
                            # There is a break in the side.
                            if coords[i + 1][0] != coords[i][0] or coords[i + 1][1] != coords[i][1] + 1:
                                sides_num += 1

                        sides_num += 1

                    # Merge sides vertically.
                    else:
                        coords = sorted(coords, key=lambda x: x[0])
                        coords = sorted(coords, key=lambda x: x[1])

                        for i in range(len(coords) - 1):
                            # There is a break in the side.
                            if coords[i + 1][1] != coords[i][1] or coords[i + 1][0] != coords[i][0] + 1:
                                sides_num += 1

                        sides_num += 1

                # Calculate cost for this region.
                price += sides_num * area

    return price
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()