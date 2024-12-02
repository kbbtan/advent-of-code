"""
Contains solutions for Day 19 stars.
Run on Python 3.8.3.
"""
import re

INPUT_FILE = "input.txt"

# Character Constants.
ACCEPT = "A"
REJECT = "R"

def star_1():
    """ Solution for Star 1.
    """
    workflows = {}
    parts = []

    with open(INPUT_FILE) as file:
        line = file.readline()

        # Read the workflows.
        while line:
            # If we hit a single newline, we have finished reading the workflows.
            if line == "\n":
                # Continue onto the next line.
                line = file.readline().strip()
                break

            # Strip newline character.
            line = line.strip()

            # Extract the workflow name and the rules.
            match = re.search(r"(.+)\{(.+)\}", line)
            workflows[match.group(1)] = match.group(2).split(",")

            # Continue to next line.
            line = file.readline()

        while line:
            part = {}

            # Extract the part properties.
            match = re.search(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}", line)
            part["x"] = int(match.group(1))
            part["m"] = int(match.group(2))
            part["a"] = int(match.group(3))
            part["s"] = int(match.group(4))
            
            parts.append(part)

            # Continue to next line.
            line = file.readline().strip()

    total = 0

    # Run each part through the series of workflows.
    for part in parts:
        # Extract part information.
        x = part["x"]
        m = part["m"]
        a = part["a"]
        s = part["s"]

        # Start from the "in" workflow.
        workflow = "in"

        while True:
            # If we have reached the "accept" workflow, add its rating.
            if workflow == ACCEPT:
                total += x + m + a + s
                break

            # If we have reached the "reject" workflow, just ignore.
            elif workflow == REJECT:
                break

            # Perform the steps of the current workflow.
            steps = workflows[workflow]

            for i in range(len(steps)):
                # If the last step is reached, just go to that workflow.
                if i == len(steps) - 1:
                    workflow = steps[i]

                # Otherwise, check if the condition is reached and go to that workflow.
                else:
                    condition, next_workflow = steps[i].split(":")

                    if eval(condition):
                        workflow = next_workflow
                        break

    return total
    
def star_2():
    """ Solution for Star 2.
    """
    def intersect_conditions(conditions, condition):
        """ Helper function to intersect condition into our current range of conditions.
            :param Dict conditions: dictionary of conditions over all four ratings
            :param str condition: string representing condition in input
        """
        # Less than condition.
        if "<" in condition:
            rating, limit = condition.split("<")
            limit = int(limit)

            # No limits exist yet.
            if conditions[rating] == None:
                conditions[rating] = [1, limit-1]

            # Otherwise, adjust limits as needed.
            else:
                current_limits = conditions[rating]

                # The limit is lower than the current limits. Not possible to intersect.
                if limit <= current_limits[0]:
                    return False
                
                # The limit is in between the current limits.
                elif limit > current_limits[0] and limit <= current_limits[1]:
                    current_limits[1] = limit - 1

                # Otherwise, the limit does not restrict the current limits.

        # More than condition.
        else:
            rating, limit = condition.split(">")
            limit = int(limit)

            # No limits exist yet.
            if conditions[rating] == None:
                conditions[rating] = [limit+1, 4000]

            # Otherwise, adjust limits as needed.
            else:
                current_limits = conditions[rating]

                # The limit is higher than the current limits. Not possible to intersect.
                if limit >= current_limits[1]:
                    return False
                
                # The limit is in between the current limits.
                elif limit < current_limits[1] and limit >= current_limits[0]:
                    current_limits[0] = limit + 1

                # Otherwise, the limit does not restrict the current limits.

        # Successfully modified the limits.
        return True

    workflows = {}

    with open(INPUT_FILE) as file:
        line = file.readline()

        # Read the workflows.
        while line:
            # If we hit a single newline, we have finished reading the workflows.
            if line == "\n":
                # Continue onto the next line.
                line = file.readline().strip()
                break

            # Strip newline character.
            line = line.strip()

            # Extract the workflow name and the rules.
            match = re.search(r"(.+)\{(.+)\}", line)
            workflows[match.group(1)] = match.group(2).split(",")

            # Continue to next line.
            line = file.readline()

    # Use a stack to traverse the workflows.
    stack = [("in", {"x": None, "m": None, "a": None, "s": None})]

    while len(stack) > 0:
        curr_node = stack.pop()
        workflow = curr_node[0]
        conditions = curr_node[1]

        # If we have reached the "accept" workflow, take note of its conditions.
        if workflow == ACCEPT:
            continue

        # If we have reached the "reject" workflow, just ignore.
        elif workflow == REJECT:
            continue

        steps = workflows[workflow]

        for i in range(len(steps)):
            # If this is the last step, we just need to traverse to the next workflow.
            if i == len(steps) - 1:
                stack.append((steps[i], conditions))

            # Otherwise, take note of this set of conditions.
            else:
                new_conditions = conditions.copy()
                condition, next_workflow = steps[i].split(":")

                # Traverse to the next workflow with the new conditions if the new range is viable.
                if intersect_conditions(new_conditions, condition):
                    stack.append((next_workflow, new_conditions))

                # Skip this step by inversing the new conditions if the new range is viable.
                pass
    
def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()