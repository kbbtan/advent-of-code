"""
Contains solutions for Day 17 stars.
Run on Python 3.8.3.
"""
import heapq

INPUT_FILE = "input.txt"

# Constants to represent directions movements in coordinates.
DIRECTION_TO_COORDS = {
    "u": (-1, 0),
    "r": (0, 1),
    "d": (1, 0),
    "l": (0, -1)
}

# Represents possible future directions based on direction we enter the grid from.
POSSIBLE_DIRECTIONS = {
    "v": ["l", "r"],
    "h": ["u", "d"],
    None: ["l", "r", "u", "d"]
}

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda x: list(x), grid))

        for r in range(len(grid)):
            grid[r] = list(map(lambda x: int(x), grid[r]))

    # Initialize min-heap for Dijkstra.
    seen_states = {}
    heap = []
    heapq.heappush(heap, (0, (0, 0), None))
    
    # Perform the Dijkstra algorithm.
    while len(heap) > 0:
        curr_state = heapq.heappop(heap)

        # Extract information.
        cost = curr_state[0]
        coords = curr_state[1]
        last_direction = curr_state[2]

        # If we have reached the end we can just return the heat loss.
        if coords == (len(grid) - 1, len(grid[0]) - 1):
            return cost
        
        # Continue searching in the possible directions.
        for direction in POSSIBLE_DIRECTIONS[last_direction]:
            # Move three steps in each turn direction.
            new_cost = cost
            movement_r = DIRECTION_TO_COORDS[direction][0]
            movement_c = DIRECTION_TO_COORDS[direction][1]

            for i in range(1, 4):
                # Obtain new coords.
                new_r = coords[0] + (movement_r * i)
                new_c = coords[1] + (movement_c * i)

                # Invalid if the new coords are out of bounds.
                if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                    break

                if direction == "l" or direction == "r":
                    new_direction = "h"
                else:
                    new_direction = "v"

                new_cost += grid[new_r][new_c]
                new_state = (new_cost, (new_r, new_c), new_direction)
    
                # If this state has not been seen before record it.
                if (new_r, new_c, new_direction) not in seen_states:
                    heapq.heappush(heap, new_state)
                    seen_states[((new_r, new_c, new_direction))] = new_cost

                # If this state improves the path cost at the state record it.
                elif seen_states[(new_r, new_c, new_direction)] > new_cost:
                    heapq.heappush(heap, new_state)
                    seen_states[((new_r, new_c, new_direction))] = new_cost


    # If this point reached the end was not found.
    return None


def star_2():
    """ Solution for Star 2.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda x: list(x), grid))

        for r in range(len(grid)):
            grid[r] = list(map(lambda x: int(x), grid[r]))

    # Initialize min-heap for Dijkstra.
    seen_states = {}
    heap = []
    heapq.heappush(heap, (0, (0, 0), None))
    
    # Perform the Dijkstra algorithm.
    while len(heap) > 0:
        curr_state = heapq.heappop(heap)

        # Extract information.
        cost = curr_state[0]
        coords = curr_state[1]
        last_direction = curr_state[2]

        # If we have reached the end we can just return the heat loss.
        if coords == (len(grid) - 1, len(grid[0]) - 1):
            return cost
        
        # Continue searching in the possible directions.
        for direction in POSSIBLE_DIRECTIONS[last_direction]:
            # Move three steps in each turn direction.
            new_cost = cost
            movement_r = DIRECTION_TO_COORDS[direction][0]
            movement_c = DIRECTION_TO_COORDS[direction][1]

            for i in range(1, 11):
                # Obtain new coords.
                new_r = coords[0] + (movement_r * i)
                new_c = coords[1] + (movement_c * i)

                # Invalid if the new coords are out of bounds.
                if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                    break

                new_cost += grid[new_r][new_c]

                # Only add valid state if at least 4 steps have been traveled:
                if i >= 4:
                    if direction == "l" or direction == "r":
                        new_direction = "h"
                    else:
                        new_direction = "v"
                    
                    new_state = (new_cost, (new_r, new_c), new_direction)
        
                    # If this state has not been seen before record it.
                    if (new_r, new_c, new_direction) not in seen_states:
                        heapq.heappush(heap, new_state)
                        seen_states[((new_r, new_c, new_direction))] = new_cost

                    # If this state improves the path cost at the state record it.
                    elif seen_states[(new_r, new_c, new_direction)] > new_cost:
                            heapq.heappush(heap, new_state)
                            seen_states[((new_r, new_c, new_direction))] = new_cost


    # If this point reached the end was not found.
    return None
    
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()