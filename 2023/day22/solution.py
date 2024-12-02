"""
Contains solutions for Day 22 stars.
Run on Python 3.8.3.
"""

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    # List of bricks.
    # Each brick is represented by its start and end coordinates.
    bricks = []

    # Grids in the x, y plane representing the highest z-coordinate being occupied, as well as the brick occupying it.
    highest = [[0 for _ in range(10)] for _ in range(10)]
    highest_brick = [[None for _ in range(10)] for _ in range(10)]

    with open(INPUT_FILE) as file:
        line = file.readline().strip()

        while line:
            # Parse out coordinates.
            start, end = line.split("~")
            start = tuple(map(lambda x: int(x), start.split(",")))
            end = tuple(map(lambda x: int(x), end.split(",")))

            # Append brick to our list of bricks.
            bricks.append((start, end))

            # Move to next line.
            line = file.readline().strip()

    # Sort bricks in order of ascending Z coordinate.
    bricks = sorted(bricks, key=lambda x: x[0][2])

    # Keep track of which bricks cannot be disintegrated.
    no_disintegrate = set()

    for i in range(len(bricks)):
        start, end = bricks[i]
        x, y, z = start
        X, Y, Z = end
        resting_on = set()

        # For each block in the brick, move it down as far as possible and check which bricks they are resting on.
        if x != X:
            # Determine the highest blocking block(s).
            max_highest = -1
            for j in range(x, X+1):
                max_highest = max(max_highest, highest[j][y])

            # Add them to the resting_on set.
            for j in range(x, X+1):
                if highest[j][y] == max_highest:
                    resting_on.add(highest_brick[j][y])

            # Update values with the current block.
            for j in range(x, X+1):
                highest[j][y] = max_highest + 1
                highest_brick[j][y] = i
        
        elif y != Y:
            # Determine the highest blocking block(s).
            max_highest = -1
            for j in range(y, Y+1):
                max_highest = max(max_highest, highest[x][j])

            # Add them to the resting_on set.
            for j in range(y, Y+1):
                if highest[x][j] == max_highest:
                    resting_on.add(highest_brick[x][j])

            # Update values with the current block.
            for j in range(y, Y+1):
                highest[x][j] = max_highest + 1
                highest_brick[x][j] = i

        # Handles both cases where z != Z and when it is a single block.
        else:
            resting_on.add(highest_brick[x][y])
            highest[x][y] += (Z - z + 1)
            highest_brick[x][y] = i


        # If there is only one brick the current brick is resting on, the brick below cannot be disintegrated.
        if len(resting_on) == 1 and None not in resting_on:
            no_disintegrate.add(resting_on.pop())

    # Return the number of bricks that can be disintegrated.
    return len(bricks) - len(no_disintegrate)
    
def star_2():
    """ Solution for Star 2.
    """
    
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()