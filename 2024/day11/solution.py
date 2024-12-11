"""
Contains solutions for Day 11 stars.
Run on Python 3.12.8.
""" 
INPUT_FILE = "input.txt"

def num_stones(stone, blinks, memo):
    """ Helper function to compute the number of stones after blinking
        blinks number of times for a specified stone.

        :param str stone: stone as specified in input
        :param int blinks: remaining blinks to perform
        :param dict memo: dictionary containing results of past subproblems
        
        :rtype: int
        :return: number of stones after blinking blinks times
    """
    # Subproblem has been solved before.
    if (stone, blinks) in memo:
        return memo[(stone, blinks)]
    
    # No more blinks remaining, one stone remains.
    if blinks == 0:
        return 1

    # Follow the algorithm to figure out how the stone is replaced.
    if stone == "0":
        new_stones = num_stones("1", blinks - 1, memo)

    elif len(stone) % 2 == 0:
        half_length = int(len(stone) / 2)
        new_stones = num_stones(stone[:half_length], blinks - 1, memo)
        new_stones += num_stones(str(int(stone[half_length:])), blinks - 1, memo)

    else:
        new_stones = num_stones(str(int(stone) * 2024), blinks - 1, memo)

    # Store result to use in the future.
    memo[(stone, blinks)] = new_stones
    return new_stones

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        line = file.read().strip()
        stones = line.split()

    memo = {}
    total = 0

    for stone in stones:
        total += num_stones(stone, 25, memo)

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        line = file.read().strip()
        stones = line.split()

    memo = {}
    total = 0

    for stone in stones:
        total += num_stones(stone, 75, memo)

    return total
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()