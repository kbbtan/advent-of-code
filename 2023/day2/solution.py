"""
Contains solutions for Day 2 stars.
Run on Python 3.8.3.
"""
import re

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    given_cubes = {"red": 12, "green": 13, "blue": 14}
    total = 0
    game_id = 1

    with open(INPUT_FILE) as file:
        for line in file:
            valid = True

            # Separate the cubes shown at a given trial.
            trials = line.split(";")

            for trial in trials:
                # Use regex to extract each number of colored cubes shown at a given trial.
                trial_colors_shown = re.findall(r"([0-9]+) (red|green|blue)", trial)
                
                # Check each color to ensure that it is not more than what we know.
                for trial_color_shown in trial_colors_shown:
                    if given_cubes[trial_color_shown[1]] < int(trial_color_shown[0]):
                        valid = False
                        break

                # If we know a given trial is not valid, the whole game is not valid.
                if not valid:
                    break

            # If valid is still True, this game is valid and we sum its ID.
            if valid:
                total += game_id

            game_id += 1

    return total

def star_2():
    """ Solution for Star 2.
    """
    total = 0

    with open(INPUT_FILE) as file:
        for line in file:
            cubes_needed = {"red": 0, "green": 0, "blue": 0}

            # Separate the cubes shown at a given trial.
            trials = line.split(";")

            for trial in trials:
                # Use regex to extract each number of colored cubes shown at a given trial.
                trial_colors_shown = re.findall(r"([0-9]+) (red|green|blue)", trial)
                
                # Check each color to ensure that it is not more than what we know.
                for trial_color_shown in trial_colors_shown:
                    cubes_needed[trial_color_shown[1]] = max(cubes_needed[trial_color_shown[1]], int(trial_color_shown[0]))

            # Calculate the power of the cubes and add it to our total.
            total += cubes_needed["red"] * cubes_needed["green"] * cubes_needed["blue"]

    return total

def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()