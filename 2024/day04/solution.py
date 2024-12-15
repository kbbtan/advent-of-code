"""
Contains solutions for Day N stars.
Run on Python 3.12.8.
"""
# Coordinate directions including corners.
D_8 = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")
    
    # Define acceptable XMAS input.
    XMAS = "XMAS"
    total = 0

    # Search through the grid.
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            # We come across an X, start search in all eight directions.
            if grid[i][j] == XMAS[0]:

                # For each direction.
                for dir in D_8:
                    d_i, d_j = dir
                    yes = True

                    # Go three steps in that direction to check for the rest of XMAS.
                    for k in range(1, 4):
                        new_i = i + (d_i * k)
                        new_j = j + (d_j * k)

                        # If new coordinates are out of bounds, break.
                        if not (new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid)):
                            yes = False
                            break

                        # If new coordinates do not match required letter, break.
                        if grid[new_i][new_j] != XMAS[k]:
                            yes = False
                            break

                    if yes:
                        total += 1
                    
    return total
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")

    total = 0

    # Search through the entire grid.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If an A is found, search for the X-MAS diagonals.
            if grid[i][j] == "A":
                # Define coordinates for all immediate diagonals.
                lu_i, lu_j = i - 1, j - 1
                ru_i, ru_j = i - 1, j + 1
                ld_i, ld_j = i + 1, j - 1
                rd_i, rd_j = i + 1, j + 1

                # If any coordinate is out of bounds, continue.
                if not (lu_i >= 0 and lu_i < len(grid) and ru_i >= 0 and ru_i < len(grid) and ld_i >= 0 and ld_i < len(grid) and rd_i >= 0 and rd_i < len(grid) and \
                    lu_j >= 0 and lu_j < len(grid[0]) and ru_j >= 0 and ru_j < len(grid[0]) and ld_j >= 0 and ld_j < len(grid[0]) and rd_j >= 0 and rd_j < len(grid[0])):
                    continue

                # If lu - rd diagonal is not valid, continue.
                if not (grid[lu_i][lu_j] == "M" and grid[rd_i][rd_j] == "S") and not (grid[lu_i][lu_j] == "S" and grid[rd_i][rd_j] == "M"):
                    continue

                # If ru - ld diagonal is not valid, continue.
                if not (grid[ru_i][ru_j] == "M" and grid[ld_i][ld_j] == "S") and not (grid[ru_i][ru_j] == "S" and grid[ld_i][ld_j] == "M"):
                    continue

                # If this point is reached all checks have passed.
                total += 1

    return total
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()