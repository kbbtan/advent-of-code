"""
Contains solutions for Day 8 stars.
Run on Python 3.12.8.
"""
from collections import defaultdict
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")

    # Find locations of all antennas in the grid.
    antenna_freqs = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                antenna_freqs[grid[r][c]].append((r, c))

    # Iterate through each pair of antennas with same frequencies to locate the antinodes.
    antinodes = set()
    for freq in antenna_freqs:
        antennas = antenna_freqs[freq]

        # Loop through every pair of antennas.
        for i in range(len(antennas) - 1):
            for j in range(i + 1, len(antennas)):
                antenna_1 = antennas[i]
                antenna_2 = antennas[j]

                # Calulate the difference between their locations.
                delta = (antenna_1[0] - antenna_2[0], antenna_1[1] - antenna_2[1])

                # Antinodes are located on either side of these antennas.
                antinode_1 = (antenna_1[0] + delta[0], antenna_1[1] + delta[1])
                antinode_2 = (antenna_2[0] - delta[0], antenna_2[1] - delta[1])

                # Check whether they still reside in the grid.
                if antinode_1[0] >= 0 and antinode_1[0] < len(grid) and antinode_1[1] >= 0 and antinode_1[1] < len(grid[0]):
                    antinodes.add(antinode_1)

                if antinode_2[0] >= 0 and antinode_2[0] < len(grid) and antinode_2[1] >= 0 and antinode_2[1] < len(grid[0]):
                    antinodes.add(antinode_2)

    # Return the number of antinodes found.
    return len(antinodes) 
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split("\n")

    # Find locations of all antennas in the grid.
    antenna_freqs = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                antenna_freqs[grid[r][c]].append((r, c))

    # Iterate through each pair of antennas with same frequencies to locate the antinodes.
    antinodes = set()
    for freq in antenna_freqs:
        antennas = antenna_freqs[freq]

        # Loop through every pair of antennas.
        for i in range(len(antennas) - 1):
            for j in range(i + 1, len(antennas)):
                antenna_1 = antennas[i]
                antenna_2 = antennas[j]

                # Calulate the difference between their locations.
                delta = (antenna_1[0] - antenna_2[0], antenna_1[1] - antenna_2[1])

                # Antinodes are located along the line formed between the antennas.
                while antenna_1[0] >= 0 and antenna_1[0] < len(grid) and antenna_1[1] >= 0 and antenna_1[1] < len(grid[0]):
                    antinodes.add(antenna_1)
                    antenna_1 = (antenna_1[0] + delta[0], antenna_1[1] + delta[1])

                while antenna_2[0] >= 0 and antenna_2[0] < len(grid) and antenna_2[1] >= 0 and antenna_2[1] < len(grid[0]):
                    antinodes.add(antenna_2)
                    antenna_2 = (antenna_2[0] - delta[0], antenna_2[1] - delta[1]) 

    # Return the number of antinodes found.
    return len(antinodes) 
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()