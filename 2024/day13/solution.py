"""
Contains solutions for Day 13 stars.
Run on Python 3.12.8.
"""
import decimal
import re
 
INPUT_FILE = "input.txt"

# Set decimal precision to check for integer answers.
decimal.getcontext().prec = 50

# Cost for the different buttons.
COST_A = 3
COST_B = 1

def star_1():
    """ Solution for Star 1.
    """
    total_tokens = 0

    with open(INPUT_FILE) as file:
        line = file.readline()

        while line:
            # Read one test case.
            X_A, Y_A = tuple(map(lambda val: int(val), re.findall(r"\d+", line)))
            line = file.readline()
            X_B, Y_B = tuple(map(lambda val: int(val), re.findall(r"\d+", line)))
            line = file.readline()
            X, Y = tuple(map(lambda val: int(val), re.findall(r"\d+", line)))
            line = file.readline()
            line = file.readline()

            # Solve the system of linear equations using Gaussian Elimination.
            A = (X - (Y / Y_B * X_B)) / (X_A - (Y_A / Y_B * X_B))
            B = (Y - (Y_A * A)) / Y_B

            A = decimal.Decimal(A)
            B = decimal.Decimal(B)
            
            # If an integer solution is possible.
            if abs(round(A) - A) < 0.000001:
                total_tokens += COST_A * round(A) + COST_B * round(B)

    return total_tokens

def star_2():
    """ Solution for Star 2.
    """
    total_tokens = 0

    with open(INPUT_FILE) as file:
        line = file.readline()

        while line:
            # Read one test case.
            X_A, Y_A = tuple(map(lambda val: int(val), re.findall(r"\d+", line)))
            line = file.readline()
            X_B, Y_B = tuple(map(lambda val: int(val), re.findall(r"\d+", line)))
            line = file.readline()
            X, Y = tuple(map(lambda val: int(val), re.findall(r"\d+", line)))
            line = file.readline()
            line = file.readline()

            # Modify X and Y as stated in the problem.
            X += 10000000000000
            Y += 10000000000000

            # Solve the system of linear equations using Gaussian Elimination.
            A = (X - (Y / Y_B * X_B)) / (X_A - (Y_A / Y_B * X_B))
            B = (Y - (Y_A * A)) / Y_B

            A = decimal.Decimal(A)
            B = decimal.Decimal(B)
            
            # If an integer solution is possible.
            if abs(round(A) - A) < 0.0001:
                total_tokens += COST_A * round(A) + COST_B * round(B)

    return total_tokens
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()