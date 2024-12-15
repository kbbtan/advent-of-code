"""
Contains solutions for Day N stars.
Run on Python 3.12.8.
"""
from collections import defaultdict, deque
import re

# Coordinate directions for moving up, right, down, left.
D_4 = [(1, 0), (0, 1), (0, -1), (-1, 0)]
# Coordinate directions including corners.
D_8 = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")
        numbers = [list(map(lambda x: int(x), re.findall(r"-?\d+", line))) for line in lines]
    
def star_2():
    """ Solution for Star 2.
    """
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()