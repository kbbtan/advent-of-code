"""
Contains solutions for Day 2 stars.
Run on Python 3.8.3.
"""
from collections import defaultdict, deque

INPUT_FILE = "input.txt"

def validate_levels(levels):
    """ Helper function to check if a given array of levels is valid.
    
        :param list levels: list of integers representing a set of levels for a report
        :rtype: bool
        :returns: True if levels is valid
    """
    # Check the direction from the first two levels.
    if levels[1] > levels[0]:
        increasing = True
    elif levels[1] < levels[0]:
        increasing = False
    else:
        return False
    
    # Check each level pairwise to ensure that they follow both direction and difference bounds.
    valid = True
    for i in range(len(levels) - 1):
        abs_diff = abs(levels[i + 1] - levels[i])

        # If increasing but the levels are decreasing / outside of bounds.
        if increasing and not (levels[i + 1] > levels[i] and abs_diff >= 1 and abs_diff <= 3):
            valid = False
            break

        # If decreasing but the levels are decreasing / outside of bounds.
        elif not increasing and not (levels[i + 1] < levels[i] and abs_diff >= 1 and abs_diff <= 3):
            valid = False
            break

    # If valid is still True, checks have passed for each pair of levels.
    return valid

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")

    records = []

    # Parse the records into integers.
    for line in lines:
        levels = line.split()
        levels = list(map(lambda x: int(x), levels))
        records.append(levels)

    total = 0

    # Check if each record is valid.
    for levels in records:
        if validate_levels(levels):
            total += 1

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")

    records = []

    # Parse the records into integers.
    for line in lines:
        levels = line.split()
        levels = list(map(lambda x: int(x), levels))
        records.append(levels)

    total = 0

    # Check if each record is valid.
    for levels in records:
        if validate_levels(levels):
            total += 1

        # If original record is not valid, try removing each level and check again.
        else:
            for i in range(len(levels)):
                levels_remove = levels.copy()
                levels_remove.pop(i)

                if validate_levels(levels_remove):
                    total += 1
                    break

    return total
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()