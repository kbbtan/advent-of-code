"""
Contains solutions for Day 7 stars.
Run on Python 3.12.8.
"""
import re
from itertools import product
 
INPUT_FILE = "input.txt"

CONCAT = 1
MULTIPLY = 2
ADD = 3
OPERATORS = (MULTIPLY, ADD)
OPERATORS_CONCAT = (MULTIPLY, ADD, CONCAT)

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")
        lines = list(map(lambda x: list(map(lambda y: int(y), re.findall(r"\d+", x))), lines))

    total = 0

    for line in lines:
        target = line[0]
        values = line[1:]

        # Find all possible products of operators.
        operator_products = product(OPERATORS, repeat=len(values) - 1)

        # Implement the equation.
        for operators in operator_products:
            curr_equation = values[0]

            for i in range(0, len(values) - 1):
                if operators[i] == MULTIPLY:
                    curr_equation *= values[i + 1]

                else:
                    curr_equation += values[i + 1]

            # We can stop checking once one combination satisfies the target.
            if curr_equation == target:
                total += target
                break

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        lines = file.read().split("\n")
        lines = list(map(lambda x: re.findall(r"\d+", x), lines))

    total = 0

    for line in lines:
        target = line[0]
        values = line[1:]

        # Find all possible products of operators.
        concat_products = product(OPERATORS_CONCAT, repeat=len(values) - 1)

        # Implement the equation.
        for operators in concat_products:
            curr_equation = values[0]

            for i in range(0, len(values) - 1):
                if operators[i] == MULTIPLY:
                    curr_equation = str(int(curr_equation) * int(values[i + 1]))

                elif operators[i] == ADD:
                    curr_equation = str(int(curr_equation) + int(values[i + 1]))

                else:
                    curr_equation += values[i + 1]

            # We can stop checking once one combination satisfies the target.
            if curr_equation == target:
                total += int(target)
                break

    return total
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()