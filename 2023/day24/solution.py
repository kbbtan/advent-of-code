"""
Contains solutions for Day 24 stars.
Run on Python 3.8.3.
"""
from sympy import Point, Line
from sympy import Matrix, linsolve, symbols

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    lines = []

    with open(INPUT_FILE) as file:
        line = file.readline().strip()

        while line:
            # Extract parameters from the input strings.
            sections = line.split("@")
            params_str = sections[0].split(",") + sections[1].split(",")
            x, y, z, dx, dy, dz = list(map(lambda x: int(x.strip()), params_str))

            # Convert into lines with their associated points.
            lines.append(((Line(Point(x, y), Point(x + dx, y + dy))), Point(x, y), Point(x + dx, y + dy)))

            # Move to the next line.
            line = file.readline().strip()

    num_intersections = 0

    # Check for intersections between the lines.
    for i in range(len(lines) - 1):
        for j in range(i+1, len(lines)):
            line, p1, p2 = lines[i]
            line2, p12, p22 = lines[j]
            intersections = line.intersection(line2)

            # An intersection does not exist.
            if len(intersections) == 0:
                continue

            # The intersection is not within the bounding box.
            intersect = intersections[0]
            x, y = intersect.coordinates
            if x < 200000000000000 or x > 400000000000000 or y < 200000000000000 or y > 400000000000000:
                continue

            # The intersection was in the past.
            # Check if intersecting point is closer to p1 (original point) than to p2 (future point).
            if intersect.distance(p1) < intersect.distance(p2) or intersect.distance(p12) < intersect.distance(p22):
                continue

            num_intersections += 1

    return num_intersections
    
def star_2():
    """ Solution for Star 2.
    """
    lines = []

    with open(INPUT_FILE) as file:
        line = file.readline().strip()

        # Sample five lines from the input space.
        for _ in range(5):
            # Extract parameters from the input strings.
            sections = line.split("@")
            params_str = sections[0].split(",") + sections[1].split(",")
            params = list(map(lambda x: int(x.strip()), params_str))

            lines.append(params)

            # Move to the next line.
            line = file.readline().strip()
    
    # Construct sequence of four equations to solve for all variables.
    X, Y, Z, DX, DY, DZ = symbols("X, Y, Z, DX, DY, DZ")
    equations1 = []
    equations2 = []
    x, y, z, dx, dy, dz = lines[0]
    for i in range(1, len(lines)):
        xp, yp, zp, dxp, dyp, dzp = lines[i]

        # Construct each sequence of equations.
        equations1.append([dyp - dy, dx - dxp, y - yp, xp - x, xp * dyp - yp * dxp - x * dy + y * dx])
        equations2.append([dzp - dz, dx - dxp, z - zp, xp - x, xp * dzp - zp * dxp - x * dz + z * dx])

    # Construct augmented matrices.
    aug1 = Matrix(equations1)
    aug2 = Matrix(equations2)

    # Solve for unknowns.
    ans_X, ans_Y, ans_DX, ans_DY = linsolve(aug1, X, Y, DX, DY).args[0]
    ans_X, ans_Z, ans_DX, ans_DZ = linsolve(aug2, X, Z, DX, DZ).args[0]

    # Return answer format (sum of initial position).
    return ans_X + ans_Y + ans_Z
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()