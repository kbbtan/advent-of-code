"""
Contains solutions for Day 10 stars.
Run on Python 3.12.8.
"""
# Coordinate directions for moving up, right, down, left.
D_4 = [(1, 0), (0, 1), (0, -1), (-1, 0)]
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")
        grid = list(map(lambda line: list(map(lambda x: int(x), list(line))), grid))

    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Start new search.
            if grid[i][j] == 0:
                stack = [(i, j)]
                ends = set()

                while len(stack) > 0:
                    curr = stack.pop()

                    # If we reach a 9, add it to our set of ends.
                    if grid[curr[0]][curr[1]] == 9:
                        ends.add(curr)

                    # Search out in possible directions.
                    for dir in D_4:
                        next_i = curr[0] + dir[0]
                        next_j = curr[1] + dir[1]

                        # Within bounds check.
                        if not(next_i >= 0 and next_i < len(grid) and next_j >= 0 and next_j < len(grid[0])):
                            continue

                        # Next step must be one higher.
                        if grid[next_i][next_j] != grid[curr[0]][curr[1]] + 1:
                            continue

                        # Add to traverse.
                        stack.append((next_i, next_j))

                # Score is the unique number of endings reached.
                total += len(ends)

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")
        grid = list(map(lambda line: list(map(lambda x: int(x), list(line))), grid))

    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Start new search.
            if grid[i][j] == 0:
                stack = [(i, j)]

                while len(stack) > 0:
                    curr = stack.pop()

                    # Everytime a 9 is reached, it represents a new unique path.
                    if grid[curr[0]][curr[1]] == 9:
                        total += 1

                    # Search out in possible directions.
                    for dir in D_4:
                        next_i = curr[0] + dir[0]
                        next_j = curr[1] + dir[1]

                        # Within bounds check.
                        if not(next_i >= 0 and next_i < len(grid) and next_j >= 0 and next_j < len(grid[0])):
                            continue

                        # Next step must be one higher.
                        if grid[next_i][next_j] != grid[curr[0]][curr[1]] + 1:
                            continue

                        # Add to traverse.
                        stack.append((next_i, next_j))

    return total
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()