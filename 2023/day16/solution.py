"""
Contains solutions for Day 16 stars.
Run on Python 3.8.3.
"""
INPUT_FILE = "input.txt"

# Character mappings to represent directions.
UP = "U"
RIGHT = "R"
DOWN = "D"
LEFT = "L"

# Define a mapping for future directions based on the tile character and direction of light.
NEIGHBORS = {
    # Empty spaces.
    (".", UP): [(-1, 0, UP)],
    (".", RIGHT): [(0, 1, RIGHT)],
    (".", DOWN): [(1, 0, DOWN)],
    (".", LEFT): [(0, -1, LEFT)],

    # Mirrors.
    ("/", UP): [(0, 1, RIGHT)],
    ("/", RIGHT): [(-1, 0, UP)],
    ("/", DOWN): [(0, -1, LEFT)],
    ("/", LEFT): [(1, 0, DOWN)],
    ("\\", UP): [(0, -1, LEFT)],
    ("\\", RIGHT): [(1, 0, DOWN)],
    ("\\", DOWN): [(0, 1, RIGHT)],
    ("\\", LEFT): [(-1, 0, UP)],

    # Splitters.
    ("|", UP): [(-1, 0, UP)],
    ("|", RIGHT): [(-1, 0, UP), (1, 0, DOWN)],
    ("|", DOWN): [(1, 0, DOWN)],
    ("|", LEFT): [(-1, 0, UP), (1, 0, DOWN)],
    ("-", UP): [(0, 1, RIGHT), (0, -1, LEFT)],
    ("-", RIGHT): [(0, 1, RIGHT)],
    ("-", DOWN): [(0, 1, RIGHT), (0, -1, LEFT)],
    ("-", LEFT): [(0, -1, LEFT)],
}

def star_1():
    """ Solution for Star 1.
    """
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda row: list(row), grid))

    energized_tiles = set()
    seen_states = set()
    stack = [(0, 0, RIGHT)]

    # Search through the grid.
    while len(stack) > 0:
        state = stack.pop()
        coords = state[:2]
        direction = state[2]
        tile = grid[state[0]][state[1]]

        # Check if state has been seen.
        if state in seen_states:
            continue
        else:
            seen_states.add(state)

        # Record tile as energized.
        if coords not in energized_tiles:
            energized_tiles.add(coords)

        # Continue search.
        for neighbor in NEIGHBORS[(tile, direction)]:
            new_coords = (coords[0] + neighbor[0], coords[1] + neighbor[1])

            # If new location is out of the grid.
            if new_coords[0] < 0 or new_coords[0] >= len(grid) or new_coords[1] < 0 or new_coords[1] >= len(grid[0]):
                continue

            # Add new state into stack.
            stack.append((new_coords[0], new_coords[1], neighbor[2]))

    return len(energized_tiles)

def star_2():
    """ Solution for Star 2.
    """
    def energized_search(starter_state):
        """ Helper function to perform search for energized tiles given a starter state.
        
            :param tuple starter_state: starting state (r, c, direction)
            :rtype: int
            :return: number of energized tiles
        """
        energized_tiles = set()
        seen_states = set()
        stack = [starter_state]

        # Search through the grid.
        while len(stack) > 0:
            state = stack.pop()
            coords = state[:2]
            direction = state[2]
            tile = grid[state[0]][state[1]]

            # Check if state has been seen.
            if state in seen_states:
                continue
            else:
                seen_states.add(state)

            # Record tile as energized.
            if coords not in energized_tiles:
                energized_tiles.add(coords)

            # Continue search.
            for neighbor in NEIGHBORS[(tile, direction)]:
                new_coords = (coords[0] + neighbor[0], coords[1] + neighbor[1])

                # If new location is out of the grid.
                if new_coords[0] < 0 or new_coords[0] >= len(grid) or new_coords[1] < 0 or new_coords[1] >= len(grid[0]):
                    continue

                # Add new state into stack.
                stack.append((new_coords[0], new_coords[1], neighbor[2]))

        return len(energized_tiles)
    
    with open(INPUT_FILE) as file:
        grid = file.read().split()
        grid = list(map(lambda row: list(row), grid))

    most_energized_tiles = 0

    # Check the top row.
    for j in range(len(grid[0])):
        most_energized_tiles = max(most_energized_tiles, energized_search((0, j, DOWN)))

    # Check the bottom row.
    for j in range(len(grid[0])):    
        most_energized_tiles = max(most_energized_tiles, energized_search((len(grid) - 1, j, UP)))

    # Check the left column.
    for i in range(len(grid)):
        most_energized_tiles = max(most_energized_tiles, energized_search((i, 0, RIGHT)))
    
    # Check the right column.
    for i in range(len(grid)):
        most_energized_tiles = max(most_energized_tiles, energized_search((i, len(grid[0]) - 1, LEFT)))

    return most_energized_tiles
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()