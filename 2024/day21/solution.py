"""
Contains solutions for Day 21 stars.
Run on Python 3.12.8.
"""
from functools import cache
from collections import deque

# Coordinate directions for moving up, right, down, left.
DIR = {
    "v": (1, 0), 
    ">": (0, 1), 
    "<": (0, -1), 
    "^": (-1, 0)
}
 
# Constants for representing keypads.
NUM_KEYPAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
DIR_KEYPAD = [[None, "^", "A"], ["<", "v", ">"]]

# Get mapping of buttons to their locations.
NUM_TO_LOC = {}
for r in range(len(NUM_KEYPAD)):
    for c in range(len(NUM_KEYPAD[0])):
        NUM_TO_LOC[NUM_KEYPAD[r][c]] = (r, c)
DIR_TO_LOC = {}
for r in range(len(DIR_KEYPAD)):
    for c in range(len(DIR_KEYPAD[0])):
        DIR_TO_LOC[DIR_KEYPAD[r][c]] = (r, c)

INPUT_FILE = "input.txt"

@cache
def find_shortest_path_length(target, curr_key, depth, num_dirs):
    """ Find the shortest path length to reach the target button from the curr_key.

        :param str target: the desired button on the number keypad to reach
        :param str curr_key: the current key we are on
        :param depth int: the keypad we are currently on
        :param num_dirs int: the number of directional keypads there are

        :rtype: int
        :returns: length of the key presses required
    """
    # The keypad we are currently on.
    if depth == 0:
        keypad, loc = NUM_KEYPAD, NUM_TO_LOC
    else:
        keypad, loc = DIR_KEYPAD, DIR_TO_LOC
    
    # Perform BFS to find the shortest path to the requested button.
    start, end = loc[curr_key], loc[target]
    queue = deque([(start, "")])
    shortest_found = False
    shortest_paths = []

    # Perform layer by layer to consider all shortest paths.
    while not shortest_found:
        new_queue = deque([])

        for state in queue:
            coords, path = state

            # Mark if a valid path to the end is found.
            if coords == end:
                shortest_found = True

                # Record list of viable shortest paths.
                shortest_paths.append(path + "A")

            # Attempt to traverse in four directions.
            for direction in DIR:
                new_r, new_c = coords[0] + DIR[direction][0], coords[1] + DIR[direction][1]

                # If out of bounds, skip.
                if new_r < 0 or new_r >= len(keypad) or new_c < 0 or new_c >= len(keypad[0]):
                    continue

                # If we hit an empty tile (represented by None), skip.
                if keypad[new_r][new_c] == None:
                    continue

                # Traverse while adding on to the path.
                new_queue.append(((new_r, new_c), path + direction))

        # Move onto the next layer of BFS.
        queue = new_queue

    # If we are at the manual keypad, there are no further keypads.
    if depth == num_dirs:
        shortest_path_length = len(shortest_paths[0])
    
    # Recursively loop through all candidate paths and figure out which subpath is shortest.
    else:
        shortest_path_length = float("inf")
        for path in shortest_paths:
            path_length = 0
            next_key = "A"

            for button in path:
                path_length += find_shortest_path_length(button, next_key, depth + 1, num_dirs)
                next_key = button

            if path_length < shortest_path_length:
                shortest_path_length = path_length

    return shortest_path_length

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        codes = file.read().split("\n")

    complexity = 0
    start_key = "A"

    # Figure out sequence of button presses for each code.
    for code in codes:
        total_length = 0

        for button in code:
            new_length = find_shortest_path_length(button, start_key, 0, 2)
            total_length += new_length
            start_key = button

        complexity += total_length * int(code[:-1])
            
    return complexity
    
def star_2():
    """ Solution for Star 2.
    """
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        codes = file.read().split("\n")

    complexity = 0
    start_key = "A"

    # Figure out sequence of button presses for each code.
    for code in codes:
        total_length = 0

        for button in code:
            new_length = find_shortest_path_length(button, start_key, 0, 25)
            total_length += new_length
            start_key = button

        complexity += total_length * int(code[:-1])
            
    return complexity
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()