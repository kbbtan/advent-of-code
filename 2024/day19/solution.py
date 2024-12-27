"""
Contains solutions for Day 19 stars.
Run on Python 3.12.8.
"""
from functools import cache

INPUT_FILE = "input.txt"

@cache
def is_possible(pattern, towels):
    """ Helper function to check if a pattern is possible given the available towels.
    
        :param str pattern: the target pattern
        :param tuple[str] towels: the towels available

        :rtype: bool
        :returns: if the pattern is possible
    """
    # Base case where the pattern is complete.
    if pattern == "":
        return True
    
    # Check if each towel can be placed first in the pattern.
    possible = False
    for towel in towels:
        if pattern[:len(towel)] == towel:
            possible = possible or is_possible(pattern[len(towel):], towels)

    return possible

@cache
def num_arrangements(pattern, towels):
    """ Helper function to check the number of possible arrangements given the available towels.
    
        :param str pattern: the target pattern
        :param tuple[str] towels: the towels available

        :rtype: bool
        :returns: if the pattern is possible
    """
    # Base case where the pattern is complete.
    if pattern == "":
        return 1
    
    # Check if each towel can be placed first in the pattern.
    possible_arrangements = 0
    for towel in towels:
        if pattern[:len(towel)] == towel:
            possible_arrangements += num_arrangements(pattern[len(towel):], towels)

    return possible_arrangements

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        # Read list of towels.
        towels = tuple(map(lambda towel: towel.strip(), file.readline().split(",")))

        # Skip a line.
        file.readline()

        # Read remaining lines for desired patterns.
        patterns = file.read().split()

    possible = 0

    for pattern in patterns:
        if is_possible(pattern, towels):
            possible += 1
    
    return possible
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        # Read list of towels.
        towels = tuple(map(lambda towel: towel.strip(), file.readline().split(",")))

        # Skip a line.
        file.readline()

        # Read remaining lines for desired patterns.
        patterns = file.read().split()

    possible_arrangements = 0

    for pattern in patterns:
        possible_arrangements += num_arrangements(pattern, towels)
    
    return possible_arrangements
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()