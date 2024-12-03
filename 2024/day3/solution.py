"""
Contains solutions for Day 3 stars.
Run on Python 3.8.3.
"""
import re

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")

    total = 0

    for line in lines:
        # Find all valid multiply instructions in the program.
        instructions = re.findall(r"mul\((\d+),(\d+)\)", line)

        # Apply each multiply instruction to add to the total.
        for instruction in instructions:
            total += int(instruction[0]) * int(instruction[1])

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")

    total = 0
    # We start the program with mul instructions enabled.
    toggle = True

    for line in lines:
        # Find all valid multiply / do / don't instructions in the program.
        instructions = re.findall(r"(?:mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\))", line)

        for instruction in instructions:
            # If there is a do instruction, turn the toggle on.
            if instruction[2] == "do":
                toggle = True

            # If there is a don't instruction, turn the toggle off.
            elif instruction[3] == "don't":
                toggle = False
            
            # Otherwise, this is a multiply instruction.
            # Only apply it if the toggle is currently on.
            elif toggle:
                total += int(instruction[0]) * int(instruction[1])

    return total
    

    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()