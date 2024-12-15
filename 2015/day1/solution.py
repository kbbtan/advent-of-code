"""
Contains solutions for Day N stars.
Run on Python 3.12.8.
"""
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        instructions = file.read().strip()

    floor = 0

    # Trace each parenthesis instruction.
    for instruction in instructions:
        if instruction == "(":
            floor += 1

        elif instruction == ")":
            floor -= 1

    return floor
    
def star_2():
    with open(INPUT_FILE) as file:
        instructions = file.read().strip()

    floor = 0

    # Trace each parenthesis instruction.
    for i in range(len(instructions)):
        instruction = instructions[i]

        if instruction == "(":
            floor += 1

        elif instruction == ")":
            floor -= 1

        # Terminate if floor -1 is reached.
        if floor == -1:
            break

    # Last index is the position which causes Santa to enter the basement.
    return i + 1
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()