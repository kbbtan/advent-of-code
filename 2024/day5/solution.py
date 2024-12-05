"""
Contains solutions for Day N stars.
Run on Python 3.12.8.
"""
from collections import defaultdict
import re
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    # Represent the page ordering rules as a graph.
    # graph[x] == {y} indicates that y should come after x.
    graph = defaultdict(lambda: set())
    total = 0

    with open(INPUT_FILE) as file:
        line = file.readline()

        # Read the first section of the input.
        # Page ordering rules section.
        while line:
            # End of the section.
            if line == "\n":
                line = file.readline()
                break

            # Record rule in the graph.
            numbers = re.findall(r"(\d+)\|(\d+)", line)[0]
            graph[numbers[0]].add(numbers[1])

            line = file.readline()

        # Read the second section of the input.
        # Pages to produce section.
        while line:
            numbers = re.findall(r"\d+", line)
            in_order = True

            # Iterate through pairs in the page.
            for i in range(len(numbers) - 1):
                for j in range(i+1, len(numbers)):
                    # Detects if two pages are out of order.
                    if numbers[i] in graph[numbers[j]]:
                        in_order = False
                        break

            # Add the middle page number if the pages are in order.
            if in_order:
                total += int(numbers[int(len(numbers) / 2)])

            line = file.readline()

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    # Represent the page ordering rules as a graph.
    # graph[x] == {y} indicates that y should come after x.
    graph = defaultdict(lambda: set())
    total = 0

    with open(INPUT_FILE) as file:
        line = file.readline()

        # Read the first section of the input.
        # Page ordering rules section.
        while line:
            # End of the section.
            if line == "\n":
                line = file.readline()
                break

            # Record rule in the graph.
            numbers = re.findall(r"(\d+)\|(\d+)", line)[0]
            graph[numbers[0]].add(numbers[1])

            line = file.readline()

        # Read the second section of the input.
        # Pages to produce section.
        while line:
            numbers = re.findall(r"\d+", line)
            in_order = True

            # Iterate through pairs in the page.
            for i in range(len(numbers) - 1):
                for j in range(i+1, len(numbers)):
                    # Detects if two pages are out of order.
                    if numbers[i] in graph[numbers[j]]:
                        # Swap them to put them in the right order.
                        numbers[i], numbers[j] = numbers[j], numbers[i]
                        in_order = False

            # Add the sorted middle page number if the original pages were not in order.
            if not in_order:
                total += int(numbers[int(len(numbers) / 2)])

            line = file.readline()

    return total
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()