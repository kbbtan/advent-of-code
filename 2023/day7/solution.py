"""
Contains solutions for Day 7 stars.
Run on Python 3.8.3.
"""
from collections import defaultdict
import functools

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    # Stores tuples of (hand, bid) in lists ordered by increasing strength of the type of the hand.
    types = [[], [], [], [], [], [], []]

    with open(INPUT_FILE) as file:
        for line in file:
            # Extract tuples of (hand, bid) from the line.
            values = line.strip().split()
            # Convert bid to an integer to work with.
            values[1] = int(values[1])

            # Count the number of each label in the hand.
            labels = defaultdict(int)
            for card in values[0]:
                labels[card] += 1

            # Determine the type of hand based off of the number of each labels we have.
            # Place the (hand, bid) tuple into the correct list in types.

            # Only have one card label. Five of a kind.
            if len(labels) == 1:
                types[6].append(values)

            # Have two card labels. 
            elif len(labels) == 2:
                # One label has four cards. Four of a kind.
                if 4 in labels.values():
                    types[5].append(values)

                # Full house otherwise.
                else:
                    types[4].append(values)

            # Have three card labels.
            elif len(labels) == 3:
                # One label has three cards. Three of a kind.
                if 3 in labels.values():
                    types[3].append(values)

                # Two pair otherwise.
                else:
                    types[2].append(values)

            # Have four card labels. One pair.
            elif len(labels) == 4:
                types[1].append(values)

            # High card otherwise.
            else:
                types[0].append(values)
    
    # Sort the tuples in each list using relative card strength.
    SORT_ORDER = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    def compare(values_1, values_2):
        hand_1, hand_2 = values_1[0], values_2[0]
        for i in range(len(hand_1)):
            if hand_1[i] != hand_2[i]:
                return SORT_ORDER[hand_1[i]] - SORT_ORDER[hand_2[i]]
            
        return 0

    for hand_type in types:
        hand_type.sort(key=functools.cmp_to_key(compare))

    # Calculate the total winnings of each hand.
    total_winnings = 0
    curr_rank = 1

    for hand_type in types:
        for values in hand_type:
            total_winnings += values[1] * curr_rank
            curr_rank += 1

    return total_winnings

def star_2():
    """ Solution for Star 2.
    """
    # Stores tuples of (hand, bid) in lists ordered by increasing strength of the type of the hand.
    types = [[], [], [], [], [], [], []]

    with open(INPUT_FILE) as file:
        for line in file:
            # Extract tuples of (hand, bid) from the line.
            values = line.strip().split()
            # Convert bid to an integer to work with.
            values[1] = int(values[1])

            # Count the number of each label in the hand.
            labels = defaultdict(int)
            for card in values[0]:
                labels[card] += 1

            # Determine the type of hand based off of the number of each labels we have.
            # Place the (hand, bid) tuple into the correct list in types.

            # Only have one card label. Five of a kind.
            if len(labels) == 1:
                types[6].append(values)

            # Have two card labels. 
            elif len(labels) == 2:
                # One label has four cards.
                if 4 in labels.values():
                    # If the odd card out is a joker, becomes five of a kind.
                    if labels["J"] == 1 or labels["J"] == 4:
                        types[6].append(values)

                    # Otherwise, four of a kind.
                    else:
                        types[5].append(values)

                # One label has three cards.
                else:
                    # If the out card out is a joker, becomes five of a kind.
                    if labels["J"] == 2 or labels["J"] == 3:
                        types[6].append(values)

                    # Otherwise, full house.
                    else:
                        types[4].append(values)

            # Have three card labels.
            elif len(labels) == 3:
                # One label has three cards. 
                if 3 in labels.values():
                    # If one of the out cards out is a joker, becomes four of a kind.
                    if labels["J"] == 3 or labels["J"] == 1:
                        types[5].append(values)

                    # Otherwise, three of a kind.
                    else:
                        types[3].append(values)

                # Two labels have two cards with one label having one card.
                else:
                    # If there is one joker, becomes a full house.
                    if labels["J"] == 1:
                        types[4].append(values)

                    # If there are two jokers, becomes four of a kind.
                    elif labels["J"] == 2:
                        types[5].append(values)

                    # Two pair otherwise.
                    else:
                        types[2].append(values)

            # Have four card labels.
            elif len(labels) == 4:
                # If one of the odd cards out is a joker, becomes three of a kind.
                if labels["J"] == 2 or labels["J"] == 1:
                    types[3].append(values)

                # One pair otherwise.
                else:
                    types[1].append(values)

            # Have five card labels.
            else:
                # If one of the cards is a joker, becomes a one pair.
                if labels["J"] == 1:
                    types[1].append(values)

                # High card otherwise.
                else:
                    types[0].append(values)
    
    # Sort the tuples in each list using relative card strength.
    SORT_ORDER = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    def compare(values_1, values_2):
        hand_1, hand_2 = values_1[0], values_2[0]
        for i in range(len(hand_1)):
            if hand_1[i] != hand_2[i]:
                return SORT_ORDER[hand_1[i]] - SORT_ORDER[hand_2[i]]
            
        return 0

    for hand_type in types:
        hand_type.sort(key=functools.cmp_to_key(compare))

    # Calculate the total winnings of each hand.
    total_winnings = 0
    curr_rank = 1

    for hand_type in types:
        for values in hand_type:
            total_winnings += values[1] * curr_rank
            curr_rank += 1

    return total_winnings
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()