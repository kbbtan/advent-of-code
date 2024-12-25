"""
Contains solutions for Day 22 stars.
Run on Python 3.12.8.
"""
from collections import deque, defaultdict

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        secret_numbers = list(map(int, file.read().split("\n")))

    total = 0

    # Compute the next secret number for our list of secret numbers.
    for secret_number in secret_numbers:
        curr = secret_number

        # Perform the prodecure interatively for 2000 iterations.
        for _ in range(2000):
            curr = (curr ^ (curr * 64)) % 16777216
            curr = (curr ^ int(curr / 32)) % 16777216
            curr = (curr ^ (curr * 2048)) % 16777216

        total += curr

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        secret_numbers = list(map(int, file.read().split("\n")))

    # Record the number of bananas obtained for each four price change sequence.
    total_bananas = defaultdict(int)

    # Compute the sequence of price changes for each secret number.
    for secret_number in secret_numbers:
        seen_sequences = set()
        curr = secret_number
        prev_price = curr % 10
        price_changes = deque([])

        # Compute the initial four price changes.
        for _ in range(4):
            curr = (curr ^ (curr * 64)) % 16777216
            curr = (curr ^ int(curr / 32)) % 16777216
            curr = (curr ^ (curr * 2048)) % 16777216
            curr_price = curr % 10

            price_changes.append(curr_price - prev_price)
            prev_price = curr_price

        # Record total for this sequence of price changes.
        total_bananas[tuple(price_changes)] += curr_price
        seen_sequences.add(tuple(price_changes))

        # Compute the price changes for all future iterations.
        for _ in range(2000 - 4):
            curr = (curr ^ (curr * 64)) % 16777216
            curr = (curr ^ int(curr / 32)) % 16777216
            curr = (curr ^ (curr * 2048)) % 16777216
            curr_price = curr % 10

            price_changes.popleft()
            price_changes.append(curr_price - prev_price)
            prev_price = curr_price

            # If sequence has been seen before, we would have sold previously.
            if tuple(price_changes) in seen_sequences:
                continue
            else:
                # Record total for this sequence of price changes.
                total_bananas[tuple(price_changes)] += curr_price
                seen_sequences.add(tuple(price_changes))

    # Identify max bananas among all possible sequences.
    max_bananas = -1
    for sequence in total_bananas:
        max_bananas = max(max_bananas, total_bananas[sequence])

    return max_bananas
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()