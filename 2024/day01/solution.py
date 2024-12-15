"""
Contains solutions for Day 1 stars.
Run on Python 3.8.3.
"""
from collections import defaultdict

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")

    # Collect the numbers into their respective left and right lists.
    left = []
    right = []
    for line in lines:
        values = line.split()
        left.append(int(values[0]))
        right.append(int(values[1]))

    # Sort the numbers in ascending order.
    left.sort()
    right.sort()

    # Sum up their differences.
    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")

    # Continue to collect left numbers into a list, 
    # but use a defaultdict to collect the counts of numbers in the right list.
    left = []
    right = defaultdict(int)
    for line in lines:
        values = line.split()
        left.append(int(values[0]))
        right[int(values[1])] += 1

    # Collect the sum of left numbers multiplied by their count in the right list.
    total = 0
    for i in range(len(left)):
        total += left[i] * right[left[i]]

    return total
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()