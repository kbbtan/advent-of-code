"""
Contains solutions for Day 9 stars.
Run on Python 3.12.8.
"""
from collections import defaultdict
import heapq

INPUT_FILE = "input.txt"
EMPTY = "."

def build_disk(instructions):
    """ Helper function to build a disk list from the given string of instructions.
    
        :param str instructions: line of instructions given by the input
        :rtype list:
        :return: list representing a disk
    """
    id = 0
    file = True
    disk = []

    # Build the disk from the given instructions.
    for c in instructions:
        num = int(c)

        # Insert a file.
        if file:
            disk += [int(id)] * num
            id += 1

        # Insert empty space.
        else:
            disk += [EMPTY] * num

        # Swap between file and empty block instructions.
        file = not file

    return disk

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        instructions = file.read()

    # Build disk from instructions.
    disk = build_disk(instructions)

    # Get a pointer to the first block of empty space.
    empty_ptr = 0
    while empty_ptr < len(disk):
        if disk[empty_ptr] == EMPTY:
            break
        empty_ptr += 1

    # Get a pointer to the last block containing a file.
    file_ptr = len(disk) - 1
    while file_ptr >= 0:
        if disk[file_ptr] != EMPTY:
            break
        file_ptr -= 1

    while file_ptr > empty_ptr:
        # Move last file block to the first empty block.
        disk[empty_ptr] = disk[file_ptr]
        disk[file_ptr] = EMPTY

        # Update pointers to point to their next empty / file block respectively.
        while disk[empty_ptr] != EMPTY:
            empty_ptr += 1

        while disk[file_ptr] == EMPTY:
            file_ptr -= 1

    # Calculate checksum from formula.
    checksum = 0
    for i in range(len(disk)):
        # Since all file blocks are moved left, 
        # there are no file blocks after the first empty block is found.
        if disk[i] == EMPTY:
            break
            
        checksum += i * disk[i]

    return checksum
    
def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        instructions = file.read()

    # Build disk from instructions.
    disk = build_disk(instructions)

    # Build a dictionary for the empty blocks in the disk.
    # Keys are the block length pointing to a min-heap.
    # Min-heaps contain (start, end) of each block, sorted by their start index.
    empty_blocks = defaultdict(list)
    largest_empty_block_size = -1
    start, end = 0, 0

    # Keep finding empty blocks from start of disk.
    while start < len(disk):
        # Start of new empty block.
        if disk[start] == EMPTY:
            # Find end of empty block.
            end = start + 1
            while end < len(disk):
                if disk[end] != EMPTY:
                    break
                end += 1

            # Add block into dictionary.
            heapq.heappush(empty_blocks[end - start], (start, end))
            largest_empty_block_size = max(largest_empty_block_size, end - start)

            # Move start pointer past the empty block.
            start = end
            continue

        start += 1

    # Keep finding file blocks from end of disk.
    start, end = len(disk) - 1, len(disk) - 1
    while end >= 0:
        # End of new file block.
        if disk[end] != EMPTY:
            # Find start of file block.
            start = end - 1
            while start >= 0:
                if disk[start] != disk[end]:
                    break
                start -= 1

            # Find first empty block from start of disk by iterating through the possible block lengths.
            file_block_size = end - start
            empty_block_size = file_block_size
            first_empty_block_size, first_empty_start = None, len(disk)

            # Search for all empty blocks larger than file block.
            while empty_block_size <= largest_empty_block_size:
                empty_block_list = empty_blocks[empty_block_size]

                if len(empty_block_list) > 0:
                    empty_block = empty_blocks[empty_block_size][0]
                    empty_start, empty_end = empty_block

                    # If this empty block is further left than the one we currently have.
                    # And the new empty block is to the left of the file block.
                    if empty_start < first_empty_start and empty_end <= start + 1:
                        first_empty_start = empty_start
                        first_empty_block_size = empty_block_size

                empty_block_size += 1

            # If there are no possible empty blocks, it is not possible to allocate this file.
            if first_empty_block_size != None:
                # Allocate the file to the first empty block.
                first_empty_block = heapq.heappop(empty_blocks[first_empty_block_size])
                first_empty_block_start, first_empty_block_end = first_empty_block
                for i in range(file_block_size):
                    disk[first_empty_block_start + i] = disk[start + i + 1]
                    disk[start + i + 1] = EMPTY

                # If there is a smaller empty block leftover, add it back to the heap.
                remaining_block_size = first_empty_block_size - file_block_size
                if remaining_block_size > 0:
                    heapq.heappush(empty_blocks[remaining_block_size], (first_empty_block_start + file_block_size, first_empty_block_end))

            # Move end to the start of the file block.
            end = start
            continue

        end -= 1
    
    # Calculate checksum from formula.
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        checksum += i * disk[i]

    return checksum
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()