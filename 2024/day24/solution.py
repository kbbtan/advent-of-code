"""
Contains solutions for Day 24 stars.
Run on Python 3.12.8.
"""
import re
 
INPUT_FILE = "input.txt"

def signal(wire, gates, values):
    """ Computes the signal for a wire given the gates available.
    
        :param str wire: an alphanumeric string representing the name of the wire
        :param dict[str:tuple[str]]: a dictionary containing the wire as the key and a tuple of strings representing
            the gate's instructions as (wire, logic_gate, wire)
        :param dict[str:int] values: a dictionary containing the pre-computed signals of certain wires
        :rtype: int
        :returns: integer 1/0 representing the signal of the wire
    """
    # The value of the wire is already known.
    if wire in values:
        return values[wire]
    
    # Follow the gate to compute the wire's signal.
    gate = gates[wire]
    prev_1 = signal(gate[0], gates, values)
    prev_2 = signal(gate[2], gates, values)

    if gate[1] == "AND":
        out = prev_1 & prev_2

    elif gate[1] == "OR":
        out = prev_1 | prev_2

    elif gate[1] == "XOR":
        out = prev_1 ^ prev_2

    # Record the computed signal value.
    values[wire] = out
    return out

def star_1():
    """ Solution for Star 1.
    """
    values = {}
    gates = {}
    output_wires = []
    output = 0

    with open(INPUT_FILE) as file:
        value_lines, gate_lines = file.read().split("\n\n")
        value_lines = value_lines.split("\n")
        gate_lines = gate_lines.split("\n")

    # Transform the known signal values into a wire:value dictionary.
    for line in value_lines:
        line_parts = re.findall(r"(.+?): (\d)", line)[0]
        values[line_parts[0]] = int(line_parts[1])

    # Transform the gates into a wire:(prev_wire, logic_gate, prev_wire) dictionary.
    for line in gate_lines:
        line_parts = re.findall(r"(.+?) (.+?) (.+?) -> (.+)", line)[0]
        gates[line_parts[3]] = (line_parts[0], line_parts[1], line_parts[2])

        # Record the output wires that we have.
        if line_parts[3][0] == "z":
            output_wires.append(line_parts[3])

    # Sort the output wires to compute bits in order.
    output_wires = sorted(output_wires)

    # Compute the decimal output.
    for i in range(len(output_wires)):
        output += signal(output_wires[i], gates, values) * (2 ** i)

    return output
    
def star_2():
    """ Solution for Star 2.
    """
    values = {}
    gates = {}
    output_wires = []
    x_bits = []
    y_bits = []
    output_bits = []

    with open(INPUT_FILE) as file:
        value_lines, gate_lines = file.read().split("\n\n")
        value_lines = value_lines.split("\n")
        gate_lines = gate_lines.split("\n")

    # Transform the known signal values into a wire:value dictionary.
    for line in value_lines:
        line_parts = re.findall(r"(.+?): (\d)", line)[0]
        values[line_parts[0]] = int(line_parts[1])

        # Record the x and y bits.
        # The input given is already in order.
        if line_parts[0][0] == "x":
            x_bits.append(values[line_parts[0]])
        if line_parts[0][0] == "y":
            y_bits.append(values[line_parts[0]])

    # Transform the gates into a wire:(prev_wire, logic_gate, prev_wire) dictionary.
    for line in gate_lines:
        line_parts = re.findall(r"(.+?) (.+?) (.+?) -> (.+)", line)[0]
        gates[line_parts[3]] = (line_parts[0], line_parts[1], line_parts[2])

        # Record the output wires that we have.
        if line_parts[3][0] == "z":
            output_wires.append(line_parts[3])

    # INSERT HERE TO SWAP GATES MANUALLY.
    # Example: gates["z01"], gates["z02"] = gates["z02"], gates["z01"]

    # Sort the output wires to compute bits in order.
    output_wires = sorted(output_wires)

    # Compute the binary output.
    for i in range(len(output_wires)):
        output_bits.append(signal(output_wires[i], gates, values))

    # Compute the sum of x and y (target output).
    target_output = 0
    for i in range(len(x_bits)):
        target_output += x_bits[i] * (2 ** i)
        target_output += y_bits[i] * (2 ** i)
    target_output_bits = list(map(lambda x: int(x), bin(target_output)[2:][::-1]))

    # Help for debugging.
    print(output_bits)
    print(target_output_bits)

    # Insert gates swapped here.
    # Example: swapped = ["z01", "z02", ..., "z08"]
    swapped = []
    return ",".join(sorted(swapped))
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()