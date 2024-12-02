"""
Contains solutions for Day 14 stars.
Run on Python 3.8.3.
"""
INPUT_FILE = "input.txt"

# Character constants.
EMPTY = "."
ROUND_ROCKS = "O"
CUBE_ROCKS = "#"

def star_1():
    """ Solution for Star 1.
    """
    # Represent the input as a 2D array.
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda row: list(row), grid))

    total_weight = 0

    # Loop through each column to move rounded rocks northwards.
    for c in range(len(grid[0])):
        north_index = 0

        for r in range(len(grid)):
            # If we have found a rounded rock.
            if grid[r][c] == ROUND_ROCKS:
                # Add the weight of the rounded rock after we move it northwards.
                total_weight += (len(grid) - north_index)

                # Advance north index.
                north_index = north_index + 1

            # If we have found a cubed rock.
            elif grid[r][c] == CUBE_ROCKS:
                # Advance north index.
                north_index = r + 1

    return total_weight
    
def star_2():
    """ Solution for Star 2.
    """
    def north(grid):
        """ Helper function to simulate tilting the dish north.
        """
        # Loop through each column to move rounded rocks northwards.
        for c in range(len(grid[0])):
            north_index = 0

            for r in range(len(grid)):
                # If we have found a rounded rock.
                if grid[r][c] == ROUND_ROCKS:
                    # Move the rounded rock up.
                    grid[r][c] = EMPTY
                    grid[north_index][c] = ROUND_ROCKS

                    # Advance north index.
                    north_index = north_index + 1

                # If we have found a cubed rock.
                elif grid[r][c] == CUBE_ROCKS:
                    # Advance north index.
                    north_index = r + 1

    def west(grid):
        """ Helper function to simulate tilting the dish west.
        """
        # Loop through each column to move rounded rocks westwards.
        for r in range(len(grid)):
            west_index = 0

            for c in range(len(grid[0])):
                # If we have found a rounded rock.
                if grid[r][c] == ROUND_ROCKS:
                    # Move the rounded rock left.
                    grid[r][c] = EMPTY
                    grid[r][west_index] = ROUND_ROCKS

                    # Advance west index.
                    west_index = west_index + 1

                # If we have found a cubed rock.
                elif grid[r][c] == CUBE_ROCKS:
                    # Advance west index.
                    west_index = c + 1

    def south(grid):
        """ Helper function to simulate tilting the dish south.
        """
        # Loop through each column to move rounded rocks southwards.
        for c in range(len(grid[0])):
            south_index = len(grid) - 1

            for r in range(len(grid) - 1, -1, -1):
                # If we have found a rounded rock.
                if grid[r][c] == ROUND_ROCKS:
                    # Move the rounded rock down.
                    grid[r][c] = EMPTY
                    grid[south_index][c] = ROUND_ROCKS

                    # Advance south index.
                    south_index = south_index - 1

                # If we have found a cubed rock.
                elif grid[r][c] == CUBE_ROCKS:
                    # Advance south index.
                    south_index = r - 1

    def east(grid):
        """ Helper function to simulate tilting the dish east.
        """
        # Loop through each column to move rounded rocks eastwards.
        for r in range(len(grid)):
            east_index = len(grid[0]) - 1

            for c in range(len(grid[0]) - 1, -1, -1):
                # If we have found a rounded rock.
                if grid[r][c] == ROUND_ROCKS:
                    # Move the rounded rock right.
                    grid[r][c] = EMPTY
                    grid[r][east_index] = ROUND_ROCKS

                    # Advance east index.
                    east_index = east_index - 1

                # If we have found a cubed rock.
                elif grid[r][c] == CUBE_ROCKS:
                    # Advance east index.
                    east_index = c - 1

    # Represent the input as a 2D array.
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda row: list(row), grid))

    # Store the grids we have seen so far and their step count.
    seen_grids = {}

    # Simulate 1000000000 cycles.
    step = 0
    while step < 1000000000:
        # If we have seen this grid before, we know that a loop has taken place.
        # We can use this by "repeating" the loop for as long as possible instead of simulating it again.
        if str(grid) in seen_grids:
            # Run the loop for as long as we can.
            loop_length = step - seen_grids[str(grid)]
            step += ((1000000000 - step) // loop_length) * loop_length

            # Simulate 1 cycle to break out of this loop.
            north(grid)
            west(grid)
            south(grid)
            east(grid)
            step += 1

        else:
            # Store the current grid for future use.
            seen_grids[str(grid)] = step

            # Simulate 1 cycle.
            north(grid)
            west(grid)
            south(grid)
            east(grid)

            # Advance to the next step.
            step += 1

    # Calculate the total weight for the resulting grid.
    total_weight = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == ROUND_ROCKS:
                total_weight += (len(grid) - r)

    return total_weight
    
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()