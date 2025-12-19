# This solution uses linear programming

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

# Puzzle input

with open("puzzle_input_day10", "r") as f:
    lines = f.read().strip().split("\n")

# Parse lines

total_presses = 0
    
for i, line in enumerate(lines, 1):
    # Split line into parts
    parts = line.split()
    
    # Parse joltages (targets)
    joltages_str = parts[-1][1:-1]  # "[1:-1]" to remove braces
    joltages = [int(x) for x in joltages_str.split(",")]
    num_counters = len(joltages)
    
    # Parse buttons
    buttons = []
    for part in parts[1:-1]:
        nums = part[1:-1]   # This is a button with the joltage counters impacted
        indices = [int(n) for n in nums.split(",")] # The indices identify the joltage counters impacted
        buttons.append(indices)
    num_buttons = len(buttons)

    # Build matrix that represents all buttons

    A = np.zeros((num_counters, num_buttons))   # Create empty matrix structure
    for button_idx, button in enumerate(buttons):
        for counter_idx in button:
            A[counter_idx][button_idx] = 1  # Set position in matrix to one, meaning this button impacts this counter

    # Set objective of minimising button presses

    c = np.ones(num_buttons)    # np.ones() creates array of 1s
                                # num_buttons = 6 (example)
                                # Creates: [1, 1, 1, 1, 1, 1]
                                # Means: minimize 1*x₀ + 1*x₁ + 1*x₂ + ... = sum of x

    # Set constraints

    b_lower = np.array(joltages)
    b_upper = np.array(joltages)    # np.array() converts Python list to numpy array
                                    # b_lower and b_upper both identical because we want equality
    constraints = LinearConstraint(A, b_lower, b_upper) # LinearConstraint is SciPy object
                                                        # Means "b_lower <= A*x <= b_upper"
                                                        # In this case b_lower == b_upper, therefore: A*x = b (equality)
                                                        
    # Set bounds

    bounds = Bounds(lb = 0, ub = np.inf)    # bounds is a SciPy object
                                            # Means "0 <= x <= infinity"
                                            
    # Solve the challenge

    result = milp(
        c = c,
        constraints = constraints,
        bounds = bounds,
        integrality = np.ones(num_buttons)
    )
    # function: milp = Mixed Integer Linear Programmer solver
    # milp returns a results object with attributes success, fun and x
    # result.success: True or False
    # result.fun: optimal objective value (minimum presses)
    # result.x: optimal x values (how many times to press each button)
    # parameter: integrality = np.ones(num_buttons) because all numbers (presses) must be integers

    # Obtain the result

    if result.success:
        min_presses = int(round(result.fun))
        print(f"Machine {i}: {min_presses} minimum button presses.")
        total_presses += min_presses
    else:
        print(f"Machine {i}: failed to find a solution.")
    
print(f"The total of all minimum presses is {total_presses}.")













