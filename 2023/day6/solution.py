"""
Contains solutions for Day 6 stars.
Run on Python 3.8.3.
"""
import re

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    result = 1

    with open(INPUT_FILE) as file:
        # Extract race times.
        line = file.readline()
        times = re.findall(r"[0-9]+", line)

        # Extract race distances.
        line = file.readline()
        distances = re.findall(r"[0-9]+", line)

    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        wins = 0

        # Consider all possible times to hold the button down for.
        for j in range(time + 1):
            travelled = j * (time - j)
            # We win by holding down the button for this amount of time.
            if travelled > distance:
                wins += 1

        result *= wins

    return result
    
def star_2():
    """ Solution for Star 2.
    """
    no_wins = 0

    with open(INPUT_FILE) as file:
        # Extract race time.
        line = file.readline()
        times = re.findall(r"[0-9]+", line)
        time = int("".join(times))

        # Extract race distance.
        line = file.readline()
        distances = re.findall(r"[0-9]+", line)
        distance = int("".join(distances))

    for i in range(time):
        travelled = i * (time - i)

        # Count the number of times we lose.
        if travelled <= distance:
            no_wins += 1

        # We begin to win. We can stop counting.
        else:
            break

    # time + 1 represents the total number of possibilities (+1 to include 0)
    # multiply no_wins by 2 to account for the total number of losses
    return (time + 1) - (no_wins * 2)

def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()