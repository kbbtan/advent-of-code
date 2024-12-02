"""
Contains solutions for Day 11 stars.
Run on Python 3.8.3.
"""
from collections import deque

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    # Represent the input as a 2D array.
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda row: list(row), grid))

    # Find empty rows.
    empty_rows = set()
    for r in range(len(grid)):
        empty = True

        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                empty = False
                break

        if empty:
            empty_rows.add(r)

    # Find empty columns.
    empty_columns = set()
    for c in range(len(grid[0])):
        empty = True

        for r in range(len(grid)):
            if grid[r][c] != ".":
                empty = False
                break

        if empty:
            empty_columns.add(c)

    # Find galaxies.
    galaxies = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                galaxies.add((r, c))

    # For each galaxy, find the shortest path to all other galaxies using BFS.
    total_length = 0
    for galaxy in galaxies:
        # Add galaxy as start node to queue.
        queue = deque([(galaxy, 0)])

        # Keep track of visited nodes.
        visited = set()

        # Perform BFS.
        while len(queue) > 0:
            coords, length = queue.popleft()
            r, c = coords

            # Node has been visited before.
            if coords in visited:
                continue

            else:
                visited.add(coords)

            # If we are at a galaxy, add the path length to the running total.
            if grid[r][c] == "#":
                total_length += length

            # Go in the four Manhattan directions.
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + direction[0], c + direction[1]

                # Check if out of bounds.
                if new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]):
                    continue

                # Calculate the path length increase.
                # Higher if we move through an expanded row / column.
                length_inc = 1
                if new_r in empty_rows:
                    length_inc += 1
                if new_c in empty_columns:
                    length_inc += 1

                # Add new node to the queue.
                queue.append(((new_r, new_c), length + length_inc))

    # Only counting each pair once.
    return total_length / 2
    
def star_2():
    """ Solution for Star 2.
    """
    # Represent the input as a 2D array.
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda row: list(row), grid))

    # Find empty rows.
    empty_rows = set()
    for r in range(len(grid)):
        empty = True

        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                empty = False
                break

        if empty:
            empty_rows.add(r)

    # Find empty columns.
    empty_columns = set()
    for c in range(len(grid[0])):
        empty = True

        for r in range(len(grid)):
            if grid[r][c] != ".":
                empty = False
                break

        if empty:
            empty_columns.add(c)

    # Find galaxies.
    galaxies = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                galaxies.add((r, c))

    # For each galaxy, find the shortest path to all other galaxies using BFS.
    total_length = 0
    for galaxy in galaxies:
        # Add galaxy as start node to queue.
        queue = deque([(galaxy, 0)])

        # Keep track of visited nodes.
        visited = set()

        # Perform BFS.
        while len(queue) > 0:
            coords, length = queue.popleft()
            r, c = coords

            # Node has been visited before.
            if coords in visited:
                continue

            else:
                visited.add(coords)

            # If we are at a galaxy, add the path length to the running total.
            if grid[r][c] == "#":
                total_length += length

            # Go in the four Manhattan directions.
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + direction[0], c + direction[1]

                # Check if out of bounds.
                if new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]):
                    continue

                # Calculate the path length increase.
                # Higher if we move through an expanded row / column.
                length_inc = 1
                if new_r in empty_rows:
                    length_inc += 999999
                if new_c in empty_columns:
                    length_inc += 999999

                # Add new node to the queue.
                queue.append(((new_r, new_c), length + length_inc))

    # Only counting each pair once.
    return total_length / 2
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()