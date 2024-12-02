"""
Contains solutions for Day 13 stars.
Run on Python 3.8.3.
"""

INPUT_FILE = "input.txt"

# Character Constants.
ROCK = "#"
ASH = "."

def star_1():
    """ Solution for Star 1.
    """
    # Stores each puzzle as a 2D array.
    puzzles = []

    with open(INPUT_FILE) as input_file:
        line = input_file.readline()
        puzzle = []

        # Loop through each line of the input.
        while len(line) > 0:
            # Remove trailing newline.
            line = line.strip()

            # We have reached the end of a puzzle.
            if line == "":
                # Store the current puzzle and start recording the next one.
                puzzles.append(puzzle)
                puzzle = []

            # We are still in our current puzzle.
            else:
                puzzle.append(list(line))

            line = input_file.readline()

        # Append the last puzzle stored.
        puzzles.append(puzzle)

    # Start solving for each puzzle.
    result = 0

    for puzzle in puzzles:
        # Generate bit representation for each row and column.
        row_bits = [0 for r in range(len(puzzle))]
        col_bits = [0 for c in range(len(puzzle[0]))]
        for r in range(len(puzzle)):
            for c in range(len(puzzle[0])):
                # Represent rocks as 1.
                if puzzle[r][c] == ROCK:
                    row_bits[r] += 1 << c
                    col_bits[c] += 1 << r

        # Try all possible vertical mirrors.
        for c in range(len(puzzle[0]) - 1):
            left_bits = 0
            right_bits = 0
            left = c
            right = c + 1
            offset = 0

            # Sweep out on each side of the mirror to store the reflections as bits.
            while left >= 0 and right < len(puzzle[0]):
                left_bits += col_bits[left] << (offset * len(puzzle))
                right_bits += col_bits[right] << (offset * len(puzzle))

                # Continue sweeping.
                left -= 1
                right += 1
                offset += 1

            # If the reflections are equal, a mirror is found.
            if left_bits == right_bits:
                result += c + 1

        # Try all possible horizontal mirrors.
        for r in range(len(puzzle) - 1):
            left_bits = 0
            right_bits = 0
            left = r
            right = r + 1
            offset = 0

            # Sweep out on each side of the mirror to store the reflections as bits.
            while left >= 0 and right < len(puzzle):
                left_bits += row_bits[left] << (offset * len(puzzle[0]))
                right_bits += row_bits[right] << (offset * len(puzzle[0]))

                # Continue sweeping.
                left -= 1
                right += 1
                offset += 1

            # If the reflections are equal, a mirror is found.
            if left_bits == right_bits:
                result += 100 * (r + 1)

    return result
    
def star_2():
    """ Solution for Star 2.
    """
    # Stores each puzzle as a 2D array.
    puzzles = []

    with open(INPUT_FILE) as input_file:
        line = input_file.readline()
        puzzle = []

        # Loop through each line of the input.
        while len(line) > 0:
            # Remove trailing newline.
            line = line.strip()

            # We have reached the end of a puzzle.
            if line == "":
                # Store the current puzzle and start recording the next one.
                puzzles.append(puzzle)
                puzzle = []

            # We are still in our current puzzle.
            else:
                puzzle.append(list(line))

            line = input_file.readline()

        # Append the last puzzle stored.
        puzzles.append(puzzle)

    # Start solving for each puzzle.
    result = 0

    for puzzle in puzzles:
        # Generate bit representation for each row and column.
        row_bits = [0 for r in range(len(puzzle))]
        col_bits = [0 for c in range(len(puzzle[0]))]
        for r in range(len(puzzle)):
            for c in range(len(puzzle[0])):
                # Represent rocks as 1.
                if puzzle[r][c] == ROCK:
                    row_bits[r] += 1 << c
                    col_bits[c] += 1 << r

        # Try all possible vertical mirrors.
        for c in range(len(puzzle[0]) - 1):
            left_bits = 0
            right_bits = 0
            left = c
            right = c + 1
            offset = 0

            # Sweep out on each side of the mirror to store the reflections as bits.
            while left >= 0 and right < len(puzzle[0]):
                left_bits += col_bits[left] << (offset * len(puzzle))
                right_bits += col_bits[right] << (offset * len(puzzle))

                # Continue sweeping.
                left -= 1
                right += 1
                offset += 1

            # If the reflections are off by exactly one character, a smudged mirror is found.
            difference = left_bits ^ right_bits
            if bin(difference).count("1") == 1:
                result += c + 1

        # Try all possible horizontal mirrors.
        for r in range(len(puzzle) - 1):
            left_bits = 0
            right_bits = 0
            left = r
            right = r + 1
            offset = 0

            # Sweep out on each side of the mirror to store the reflections as bits.
            while left >= 0 and right < len(puzzle):
                left_bits += row_bits[left] << (offset * len(puzzle[0]))
                right_bits += row_bits[right] << (offset * len(puzzle[0]))

                # Continue sweeping.
                left -= 1
                right += 1
                offset += 1

            # If the reflections are off by exactly one character, a smudged mirror is found.
            difference = left_bits ^ right_bits
            if bin(difference).count("1") == 1:
                result += 100 * (r + 1)

    return result
    
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()