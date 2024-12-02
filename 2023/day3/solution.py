"""
Contains solutions for Day 3 stars.
Run on Python 3.8.3.
"""

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    total = 0
    adjacent_traverse = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    schematic = []

    # Convert the schematic into a 2D array representing an undirected graph.
    with open(INPUT_FILE) as file:
        for line in file:
            schematic.append(list(line.strip()))

    for r in range(len(schematic)):
        for c in range(len(schematic[0])):
            # If a symbol is detected, check adjacent characters.
            if not schematic[r][c].isdigit() and schematic[r][c] != ".":
                for traverse in adjacent_traverse:
                    new_r, new_c = r + traverse[0], c + traverse[1]

                    # Check that we are not traversing out of bounds.
                    if new_r < 0 or new_r >= len(schematic) or new_c < 0 or new_c >= len(schematic[0]):
                        continue

                    # If a digit is detected, traverse digits until the number is uncovered.
                    if schematic[new_r][new_c].isdigit():
                        number_string = schematic[new_r][new_c]
                        schematic[new_r][new_c] = "."

                        # Traverse to the left.
                        curr_digit_c = new_c - 1
                        while curr_digit_c >= 0:
                            # No more digits to discover.
                            if not schematic[new_r][curr_digit_c].isdigit():
                                break
                                
                            number_string = schematic[new_r][curr_digit_c] + number_string
                            schematic[new_r][curr_digit_c] = "."
                            curr_digit_c -= 1

                        # Traverse to the right.
                        curr_digit_c = new_c + 1
                        while curr_digit_c < len(schematic[0]):
                            # No more digits to discover.
                            if not schematic[new_r][curr_digit_c].isdigit():
                                break
                                
                            number_string = number_string + schematic[new_r][curr_digit_c]
                            schematic[new_r][curr_digit_c] = "."
                            curr_digit_c += 1

                        # Add the uncovered number to the total.
                        total += int(number_string)

    return total

def star_2():
    """ Solution for Star 2.
    """
    def traverse_number(schematic, new_r, new_c):
        """ Helper function to uncover numbers by traversing through the schematic.
            Starts at (new_r, new_c).
        """
        changed_indices = []
        number_string = schematic[new_r][new_c]
        changed_indices.append((new_r, new_c, schematic[new_r][new_c]))
        schematic[new_r][new_c] = "."

        # Traverse to the left.
        curr_digit_c = new_c - 1
        while curr_digit_c >= 0:
            # No more digits to discover.
            if not schematic[new_r][curr_digit_c].isdigit():
                break
                
            number_string = schematic[new_r][curr_digit_c] + number_string
            changed_indices.append((new_r, curr_digit_c, schematic[new_r][curr_digit_c]))
            schematic[new_r][curr_digit_c] = "."
            curr_digit_c -= 1

        # Traverse to the right.
        curr_digit_c = new_c + 1
        while curr_digit_c < len(schematic[0]):
            # No more digits to discover.
            if not schematic[new_r][curr_digit_c].isdigit():
                break
                
            number_string = number_string + schematic[new_r][curr_digit_c]
            changed_indices.append((new_r, curr_digit_c, schematic[new_r][curr_digit_c]))
            schematic[new_r][curr_digit_c] = "."
            curr_digit_c += 1

        return number_string, changed_indices

    total = 0
    adjacent_traverse = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    schematic = []

    # Convert the schematic into a 2D array representing an undirected graph.
    with open(INPUT_FILE) as file:
        for line in file:
            schematic.append(list(line.strip()))

    for r in range(len(schematic)):
        for c in range(len(schematic[0])):
            # If a star symbol is detected, check adjacent characters.
            if schematic[r][c] == "*":
                changed_indices = []
                number_string_1, number_string_2 = None, None
                valid_gear = True

                for traverse in adjacent_traverse:
                    new_r, new_c = r + traverse[0], c + traverse[1]

                    # Check that we are not traversing out of bounds.
                    if new_r < 0 or new_r >= len(schematic) or new_c < 0 or new_c >= len(schematic[0]):
                        continue

                    # If a digit is detected, check that we have the capacity for more numbers.
                    if schematic[new_r][new_c].isdigit():
                        # The star is adjacent to more than 2 numbers and is no longer a valid gear.
                        if number_string_1 and number_string_2:
                            valid_gear = False
                            break

                        # One number has been previously discovered. Store the new number in number_string_2.
                        elif number_string_1:
                            number_string_2, more_changed_indices = traverse_number(schematic, new_r, new_c)
                            changed_indices.extend(more_changed_indices)

                        # No numbers have been previously discovered. Store the new number in number_string_1.
                        else:
                            number_string_1, more_changed_indices = traverse_number(schematic, new_r, new_c)
                            changed_indices.extend(more_changed_indices)

                # Add the gear ratio to the total if this star is a valid gear.
                if number_string_1 and number_string_2 and valid_gear:
                    total += int(number_string_1) * int(number_string_2)

                # Change schematic back to its original state.
                for changed_indice in changed_indices:
                    schematic[changed_indice[0]][changed_indice[1]] = changed_indice[2]

    return total

def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()