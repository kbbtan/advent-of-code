"""
Contains solutions for Day 9 stars.
Run on Python 3.8.3.
"""
import re

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    def predict_values(values):
        """ Recursive function to help predict the new values.
                values: list of integers representing the current values
        """
        end_reached = True
        differences = []

        # Calculate differences.
        for i in range(1, len(values)):
            difference = values[i] - values[i - 1]

            if difference != 0:
                end_reached = False

            differences.append(difference)

        # If the end is reached, we can start to predict up the recursive stack.
        # The last value of this step will be equal to the rest of the values.
        if end_reached:
            return values[-1]
        
        # Otherwise, we continue down the recursive stack.
        else:
            last_value = predict_values(differences)

            # Use the last value to predict this step's last value.
            new_last_value = values[-1] + last_value
            return new_last_value

    total = 0

    with open(INPUT_FILE) as file:
        for line in file:
            # Extract initial values.
            values = re.findall(r"-{0,1}[0-9]+", line)
            
            # Convert to integers to opreate on.
            values = list(map(lambda value: int(value), values))

            # Obtain the total of the new values recursively.
            final_last_value = predict_values(values)
            total += final_last_value

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    def predict_values(values):
        """ Recursive function to help predict the new values.
                values: list of integers representing the current values
        """
        end_reached = True
        differences = []

        # Calculate differences.
        for i in range(1, len(values)):
            difference = values[i] - values[i - 1]

            if difference != 0:
                end_reached = False

            differences.append(difference)

        # If the end is reached, we can start to predict up the recursive stack.
        # The first value of this step will be equal to the rest of the values.
        if end_reached:
            return values[0]
        
        # Otherwise, we continue down the recursive stack.
        else:
            first_value = predict_values(differences)

            # Use the first to predict this step's first value.
            new_first_value = values[0] - first_value
            return new_first_value

    total = 0

    with open(INPUT_FILE) as file:
        for line in file:
            # Extract initial values.
            values = re.findall(r"-{0,1}[0-9]+", line)
            
            # Convert to integers to opreate on.
            values = list(map(lambda value: int(value), values))

            # Obtain the total of the new values recursively.
            final_last_value = predict_values(values)
            total += final_last_value

    return total
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solutsion for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()