"""
Contains solutions for Day 1 stars.
Run on Python 3.8.3.
"""

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    total = 0

    with open(INPUT_FILE) as file:
        for line in file:
            first_digit, last_digit, curr_digit = None, None, None

            # Loop through the line, keeping track of digits that we come across.
            for c in line:
                if c.isdigit():
                    curr_digit = c

                    # If first_digit is None, this is the first one we have come across.
                    if not first_digit:
                        first_digit = curr_digit

            # Record the last digit we came across after the loop has completed.
            last_digit = curr_digit

            # Concatenate the digits and add them to the total.
            total += int(first_digit + last_digit)

    return total

def star_2():
    """ Solution for Star 2.
    """
    def identify_digit(line, start):
        """ Helper function which returns a digit representation of the digit
            starting at index start.

            Returns None if no digit is found.
        """
        # Digit is identified and we can return it.
        if line[start].isdigit():
            return line[start]
        
        # Search through the possible words to check if there is a digit starting
        # at index start.
        word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        for i in range(len(word_digits)):
            word = word_digits[i]
            end = start + len(word)

            if line[start:end] == word:
                return str(i + 1)
            
        # If this point is reached, no digit has been found.
        return None

    total = 0

    with open(INPUT_FILE) as file:
        for line in file:
            first_digit, last_digit, curr_digit = None, None, None

            # Loop through the line, keeping track of digits that we come across.
            for i in range(len(line)):
                digit = identify_digit(line, i)
                if digit:
                    curr_digit = digit

                    # If first_digit is None, this is the first one we have come across.
                    if not first_digit:
                        first_digit = curr_digit

            # Record the last digit we came across after the loop has completed.
            last_digit = curr_digit

            # Concatenate the digits and add them to the total.
            total += int(first_digit + last_digit)

    return total

def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()