"""
Contains solutions for Day 23 stars.
Run on Python 3.12.8.
"""
from collections import defaultdict
 
INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    graph = defaultdict(set)

    with open(INPUT_FILE) as file:
        # Construct the adjacency list for the graph.
        line = file.readline().strip()
        while line:
            # Add edges.
            com1, com2 = line.split("-")
            graph[com1].add(com2)
            graph[com2].add(com1)

            line = file.readline().strip()

    connected = 0

    # Brute force all possible combination of three computers.
    for com1 in graph:
        for com2 in graph[com1]:
            for com3 in graph[com2]:
                # If none of the computers start with t, ignore this combination.
                if not (com1[0] == "t" or com2[0] == "t" or com3[0] == "t"):
                    continue

                # If they are interconnected, record it.
                if com1 in graph[com3]:
                    connected += 1

    # Divide by 6 due to over-counting.
    # For each combination of 3 computers, there are 6 possible ways to arrange them,
    # which are each counted by a naive brute-force algorithm.
    return connected / 6
    
def star_2():
    """ Solution for Star 2.
    """
    graph = defaultdict(set)

    with open(INPUT_FILE) as file:
        # Construct the adjacency list for the graph.
        line = file.readline().strip()
        while line:
            # Add edges.
            com1, com2 = line.split("-")
            graph[com1].add(com2)
            graph[com2].add(com1)

            line = file.readline().strip()

    largest_clique = set()

    # Brute force all possible combination of three computers.
    for com1 in graph:
        for com2 in graph[com1]:
            for com3 in graph[com2]:
                # If they do not form a clique, skip.
                if com1 not in graph[com3]:
                    continue

                # Form a clique with the three computers.
                clique = set((com1, com2, com3))

                # Try to add as many remaining computers as possible to the clique.
                for new_com in graph:
                    in_clique = True

                    # Check that the new computer has a connection to all computers already in the clique.
                    for old_com in clique:
                        if old_com not in graph[new_com]:
                            in_clique = False
                            break

                    # Add to clique.
                    if in_clique:
                        clique.add(new_com)

                # If the size of the clique is larger than what we've seen, record it.
                if len(clique) > len(largest_clique):
                    largest_clique = clique

    # Recover the password format.
    return ",".join(sorted(largest_clique))
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()