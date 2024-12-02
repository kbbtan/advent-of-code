"""
Contains solutions for Day 15 stars.
Run on Python 3.8.3.
"""

INPUT_FILE = "input.txt"

# Character Constants.
REMOVE = "-"


def star_1():
    """ Solution for Star 1.
    """
    # Read the sequence of steps from input.
    with open(INPUT_FILE) as file:
        sequence = file.readline().strip()

    total = 0

    # Perform the HASH algorithm as defined on each step.
    for step in sequence.split(","):
        result = 0

        for c in step:
            result += ord(c)
            result *= 17
            result %= 256

        total += result

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    # Read the sequence of steps from input.
    with open(INPUT_FILE) as file:
        sequence = file.readline().strip()

    # Create a list to store the boxes' information.
    # Each box is represented by a list, containing lens in the format [label, focal length].
    boxes = [[] for i in range(256)]

    for step in sequence.split(","):
        i = 0

        # Store the label and calculate its hash.
        hash = 0
        label = ""
        while step[i] != "-" and step[i] != "=":
            label += step[i]
            hash += ord(step[i])
            hash *= 17
            hash %= 256
            i += 1

        # Determine the type of step this is.
        step_type = step[i]
        i += 1
        
        # If this is a remove step.
        if step_type == REMOVE:
            # Identify the box associated with the hash of this lens.
            current_lens = boxes[hash]

            # Loop through the lens in the box to find the lens. 
            for j in range(len(current_lens)):
                # If the lens is found, remove it.
                if current_lens[j][0] == label:
                    current_lens.pop(j)
                    break

        # Otherwise, try to either replace or add the new lens to the box.
        else:
            # Read the focal length of the lens that needs to go into the box.
            focal_length = int(step[i:])

            # Identify the box associated with the hash of this lens.
            current_lens = boxes[hash]

            # Try to find and replace the respective lens.
            replaced = False
            for j in range(len(current_lens)):
                # If the same label already exists in the box, replace its focal length.
                if current_lens[j][0] == label:
                    current_lens[j][1] = focal_length
                    replaced = True
                    break

            # If lens is not found, append it to the end of the list.
            if not replaced:
                current_lens.append([label, focal_length])

    # Calculate the total focusing power of the lens following the formula given.
    total_focusing_power = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            total_focusing_power += (i + 1) * (j + 1) * boxes[i][j][1]

    return total_focusing_power
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()