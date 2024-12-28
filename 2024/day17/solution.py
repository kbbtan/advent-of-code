"""
Contains solutions for Day 17 stars.
Run on Python 3.12.8.
"""
INPUT_FILE = "input.txt"

def decode_combo(operand, registers):
    """ Decodes the value of a combo operand and returns its value.
    
        :param int operand: the combo operand of the instruction
        :param dict[str:int] registers: the current value of the three registers (A, B, C)

        :rtype: int
        :returns: the decoded literal value for the combo operand
    """
    if operand == 4:
        return registers["A"]
    
    elif operand == 5:
        return registers["B"]
    
    elif operand == 6:
        return registers["C"]
    
    else:
        return operand

def execute(opcode, operand, registers):
    """ Executes an instruction given its opcode and operand.
    
        :param int opcode: the three bit opcode of the instruction represented as an integer
        :param int operand: the operand of the instruction represented as an integer
        :param dict[str:int] registers: the current value of the three registers (A, B, C)

        :rtype: tuple(int, int)
        :returns: the next IP and the output, if any
    """
    next_ip = None
    output = None

    # adv instruction (A division).
    if opcode == 0:
        registers["A"] = int(registers["A"] / (2 ** decode_combo(operand, registers)))

    # bxl instruction (B XOR).
    elif opcode == 1:
        registers["B"] = registers["B"] ^ operand

    # bst instruction (B modulo).
    elif opcode == 2:
        registers["B"] = decode_combo(operand, registers) % 8

    # jnz instruction (jump instruction).
    elif opcode == 3:
        if registers["A"] != 0:
            next_ip = operand

    # bxc instruction (B XOR C).
    elif opcode == 4:
        registers["B"] = registers["B"] ^ registers["C"]

    # out instruction (output).
    elif opcode == 5:
        output = decode_combo(operand, registers) % 8

    # bdv instruction (B division).
    elif opcode == 6:
        registers["B"] = int(registers["A"] / (2 ** decode_combo(operand, registers)))

    # cdv instruction (C division).
    elif opcode == 7:
        registers["C"] = int(registers["A"] / (2 ** decode_combo(operand, registers)))

    return (next_ip, output)

def run_program(program, registers):
    """ This function takes a program and runs it given an initial set of registers.
    
        :param list[int] program: list of integers representing the computer program
        :param dict[str:int] registers: the current value of the three registers (A, B, C)

        :rtype: tuple[int]
        :returns: the outputs from the program
    """
    # Collect outputs.
    outputs = []

    # Initialize instruction pointer to 0.
    ip = 0

    # Perform execution of the program.
    while ip >= 0 and ip < len(program) - 1:
        # Read instruction (opcode and operand).
        opcode = program[ip]
        operand = program[ip + 1]

        # Execute operation.
        next_ip, output = execute(opcode, operand, registers)

        # Update IP.
        if next_ip != None:
            ip = next_ip
        else:
            ip += 2

        # Update output if any.
        if output != None:
            outputs.append(output)

    return outputs

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        # Read initial values stored at registers.
        A = int(file.readline().strip().split(": ")[1])
        B = int(file.readline().strip().split(": ")[1])
        C = int(file.readline().strip().split(": ")[1])

        # Skip blank line.
        file.readline()

        # Read program.
        program = list(map(int, file.readline().strip().split(": ")[1].split(",")))

        # Run program.
        outputs = run_program(program, {"A": A, "B": B, "C": C})

    return ",".join(map(str, outputs))
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        # Read initial values stored at registers.
        # Skip A.
        file.readline()
        B = int(file.readline().strip().split(": ")[1])
        C = int(file.readline().strip().split(": ")[1])

        # Skip blank line.
        file.readline()

        # Read program.
        program = list(map(int, file.readline().strip().split(": ")[1].split(",")))

    # Perform DFS to find the possible octets to generate the program.
    stack = [(0, len(program) - 1)]
    target_As = []

    while len(stack) > 0:
        curr_A, program_index = stack.pop()

        # We have reached the end of the traversal.
        if program_index == -1:
            target_As.append(curr_A)
            continue

        # Avoids edge case where A ends up being 0.
        start = 1 if program_index == len(program) - 1 else 0
        
        # Try each possible value for the octet.
        for value in range(start, 8):
            new_A = curr_A + (1 << (program_index * 3)) * value

            # Obtain outputs and check that the output matches the program at the index.
            outputs = run_program(program, {"A": new_A, "B": B, "C": C})
            if outputs[program_index] == program[program_index]:
                stack.append((new_A, program_index - 1))

    return min(target_As)
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()