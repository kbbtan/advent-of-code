"""
Contains solutions for Day 4 stars.
Run on Python 3.8.3.
"""
import re

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    total = 0

    with open(INPUT_FILE) as file:
        for line in file:
            matches = 0

            # Extract our numbers and the winning numbers.
            separated_numbers = line.split("|")
            our_numbers = re.findall(r"[0-9]+", separated_numbers[1])

            # Convert winning numbers into a set for efficiency.
            # Also ignore the first number as it represents the card number.
            winning_numbers = re.findall(r"[0-9]+", separated_numbers[0])
            winning_numbers = set(winning_numbers[1:])

            for number in our_numbers:
                # Number is a match.
                if number in winning_numbers:
                    matches += 1

            # Calculate the score based on the number of matches.
            if matches >= 1:
                total += 2 ** (matches - 1)

    return total

def star_2():
    """ Solution for Star 2.
    """
    scratchcard_count = {}

    # Initialize the count of each scratchcard to be 1.
    with open(INPUT_FILE) as file:
        line_num = 1

        for line in file:
            scratchcard_count[line_num] = 1
            line_num += 1

    with open(INPUT_FILE) as file:
        for line in file:
            matches = 0

            # Extract our numbers, the winning numbers and the scratchcard number.
            separated_numbers = line.split("|")
            our_numbers = re.findall(r"[0-9]+", separated_numbers[1])

            # Convert winning numbers into a set for efficiency.
            # Also ignore the first number as it represents the card number.
            winning_numbers = re.findall(r"[0-9]+", separated_numbers[0])
            scratchcard_num = int(winning_numbers[0])
            winning_numbers = set(winning_numbers[1:])

            for number in our_numbers:
                # Number is a match.
                if number in winning_numbers:
                    matches += 1

            # Duplicate subsequent scratchcards based on matches and number of current scratchcards.
            for i in range(matches):
                scratchcard_count[scratchcard_num + i + 1] += scratchcard_count[scratchcard_num]

    # Count total number of scratchcards.
    return sum(scratchcard_count.values())

def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()