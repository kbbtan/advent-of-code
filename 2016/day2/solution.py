"""
Contains solutions for Day 2 stars.
Run on Python 3.12.8.
"""
# Define Keypads.
KEYPAD = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
KEYPAD_2 = [
    [None, None, "1", None, None],
    [None, "2", "3", "4", None],
    ["5", "6", "7", "8", "9"],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
]

# Directions in the grid.
DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")

    # Build up the code.
    bathroom_code = ""
    curr = (1, 1)

    for line in lines:
        for instruction in line:
            new_r = curr[0] + DIRECTIONS[instruction][0]
            new_c = curr[1] + DIRECTIONS[instruction][1]

            # If r or c steps out of bounds, ignore the step.
            if new_r < 0 or new_r >= len(KEYPAD) or new_c < 0 or new_c >= len(KEYPAD[0]):
                continue 

            # Otherwise, update the current position.
            else:
                curr = (new_r, new_c)

        # Record the code at the position we end up at.
        bathroom_code += KEYPAD[curr[0]][curr[1]]

    return bathroom_code
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")

    # Build up the code.
    bathroom_code = ""
    curr = (2, 0)

    for line in lines:
        for instruction in line:
            new_r = curr[0] + DIRECTIONS[instruction][0]
            new_c = curr[1] + DIRECTIONS[instruction][1]

            # If r or c steps out of bounds, ignore the step.
            if new_r < 0 or new_r >= len(KEYPAD_2) or new_c < 0 or new_c >= len(KEYPAD_2[0]):
                continue 

            # If r or c steps out of the keypad (steps into a None), ignore the step.
            elif KEYPAD_2[new_r][new_c] == None:
                continue

            # Otherwise, update the current position.
            else:
                curr = (new_r, new_c)

        # Record the code at the position we end up at.
        bathroom_code += KEYPAD_2[curr[0]][curr[1]]

    return bathroom_code
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()