"""
Contains solutions for Day N stars.
Run on Python 3.8.3.
"""
from collections import defaultdict, deque
import re

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")
        numbers = list(map(lambda x: list(map(lambda y: int(y), re.findall(r"\d", x))), lines))
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")
        numbers = list(map(lambda x: list(map(lambda y: int(y), re.findall(r"\d", x))), lines))
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()