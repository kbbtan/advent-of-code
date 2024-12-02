"""
Contains solutions for Day 12 stars.
Run on Python 3.8.3.
"""

INPUT_FILE = "input.txt"

# Character representations for the input.
DAMAGED = "#"
OPERATIONAL = "."

def subproblem(record, group_records, memo):
    """ Defines a function to solve subproblems recursively for Star 1.

        :param str record: the current record to solve for
        :param Tuple[int] group_records: the current list of continguous damaged groups
        :param Dict[Tuple] memo: dictionary for memoization
    """        
    # If we have seen this state before, just use the result.
    if (record, group_records) in memo:
        return memo[(record, group_records)]
    
    # We have reached the end of the record.
    if len(record) == 0:
        # We have completed the record while allocating all required damaged groups.
        if len(group_records) == 0:
            return 1
        
        # Otherwise, we have unallocated damaged groups.
        else:
            return 0
    
    sub_arrangements = 0

    # The current spring is operational. We can just skip it and move on to the next character.
    if record[0] == OPERATIONAL:
        sub_arrangements += subproblem(record[1:], group_records, memo)

    # The current spring is damaged. Check ahead to see if it fits the requirements.
    elif record[0] == DAMAGED:
        # There are no groups left to allocate.
        if len(group_records) == 0:
            return 0
        
        # Extract the length of the required group.
        group_length = group_records[0]

        # The group size exceeds the remaining record length.
        if len(record) < group_length:
            return 0
        
        # It is not possible for there to be a group (operational spring in the way).
        if OPERATIONAL in record[:group_length]:
            return 0
        
        # The character after the damaged group (if it exists) is still damaged.
        if len(record) > group_length and record[group_length] == DAMAGED:
            return 0
        
        # Otherwise, this group is valid and we continue to look for more groups.
        sub_arrangements += subproblem(record[group_length+1:], group_records[1:], memo)

    # The current spring is a ?. Try both branches above.
    else:
        # Case where it is operational.
        sub_arrangements += subproblem(record[1:], group_records, memo)
        memo[(record, group_records)] =  sub_arrangements

        # Case where it is damaged (refer to above for detailed explanations).
        if len(group_records) == 0:
            return sub_arrangements
        group_length = group_records[0]
        if len(record) < group_length:
            return sub_arrangements
        if OPERATIONAL in record[:group_length]:
            return sub_arrangements
        if len(record) > group_length and record[group_length] == DAMAGED:
            return sub_arrangements
        sub_arrangements += subproblem(record[group_length+1:], group_records[1:], memo)
    
    # Record result for future memo.
    memo[(record, group_records)] =  sub_arrangements

    return sub_arrangements

def star_1():
    """ Solution for Star 1.
    """
    memo = {}

    # Store the puzzle inputs.
    puzzles = []
    with open(INPUT_FILE) as file:
        line = file.readline().strip()

        while line:
            # Extract puzzle fields and convert damaged groups to integers.
            record, group_records_line = line.split()
            group_records = tuple(map(lambda x: int(x), group_records_line.split(",")))
            puzzles.append((record, group_records))

            line = file.readline().strip()
            
    total_arrangements = 0

    for puzzle in puzzles:
        record, group_records = puzzle
        
        puzzle_arrangements = subproblem(record, group_records, memo)
        total_arrangements += puzzle_arrangements

    return total_arrangements
    
def star_2():
    """ Solution for Star 2.
    """
    memo = {}

    # Store the puzzle inputs.
    puzzles = []
    with open(INPUT_FILE) as file:
        line = file.readline().strip()

        while line:
            # Extract puzzle fields and convert damaged groups to integers.
            record, group_records_line = line.split()
            group_records = tuple(map(lambda x: int(x), group_records_line.split(",")))

            # Unfold the puzzle input by expanding it.
            expanded_record = "?".join([record for _ in range(5)])
            expanded_group_records = group_records * 5

            puzzles.append((expanded_record, expanded_group_records))

            line = file.readline().strip()
            
    total_arrangements = 0

    for puzzle in puzzles:
        record, group_records = puzzle
        
        puzzle_arrangements = subproblem(record, group_records, memo)
        total_arrangements += puzzle_arrangements

    return total_arrangements
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()