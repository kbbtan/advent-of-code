"""
Contains solutions for Day 8 stars.
Run on Python 3.8.3.
"""
import re
import math

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    graph = {}

    with open(INPUT_FILE) as file:
        # Store instructions.
        instructions = file.readline().strip()
        
        # Dummy read a line to skip the blank line.
        file.readline()
        line = file.readline()

        # Store nodes in an adjacency graph.
        while line:
            values = re.findall(r"[A-Z]+", line)
            graph[values[0]] = values[1:]

            line = file.readline()

    # Keep tracing through the steps from AAA until we reach ZZZ.
    steps = 0
    curr = "AAA"
    instruction_index = 0

    while curr != "ZZZ":
        steps += 1

        # Take a step in the direction indicated in the instructions.
        if instructions[instruction_index] == "L":
            curr = graph[curr][0]

        else:
            curr = graph[curr][1]

        # Loop around if we reach the end of the instruction set.
        instruction_index = (instruction_index + 1) % len(instructions)

    return steps

def star_2():
    """ Solution for Star 2.
    """
    def lcm(num1, num2):
        """ This helper function finds the lowest common multiple of num1 and num2.
        """
        return abs(num1 * num2) // math.gcd(num1, num2)

    graph = {}
    curr_nodes = []

    with open(INPUT_FILE) as file:
        # Store instructions.
        instructions = file.readline().strip()
        
        # Dummy read a line to skip the blank line.
        file.readline()
        line = file.readline()

        # Store nodes in an adjacency graph.
        while line:
            values = re.findall(r"[A-Z0-9]+", line)
            graph[values[0]] = values[1:]

            # Also add it to our start nodes if it ends with A.
            if values[0][-1] == "A":
                curr_nodes.append(values[0])

            line = file.readline()

    # Find the number of steps for each node to first reach a node ending in Z.
    # This is also the length of the cycle for each node
    # (i.e. each node takes the same amount of steps to return to Z).
    nodes_steps = []
    for i in range(len(curr_nodes)):
        instruction_index = 0
        steps = 0

        while curr_nodes[i][-1] != "Z":
            steps += 1

            # Take a step in the appropriate direction.
            if instructions[instruction_index] == "L":
                curr_nodes[i] = graph[curr_nodes[i]][0]

            else:
                curr_nodes[i] = graph[curr_nodes[i]][1]

            # Loop around if we reach the end of the instruction set.
            instruction_index = (instruction_index + 1) % len(instructions)

        nodes_steps.append(steps)

    # We can take the lowest common multiple of all of these steps to find the first
    # step where all the nodes are aligned on their respective "ending in Z" node.
    combined_lcm = nodes_steps[0]

    for i in range(1, len(nodes_steps)):
        combined_lcm = lcm(combined_lcm, nodes_steps[i])

    return combined_lcm
    
def main():
    """ Contains driver code for running solutions.
    """
    # print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()