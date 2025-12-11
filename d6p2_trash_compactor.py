import math

with open("puzzle_input_day6", "r") as f:
    grid = f.read().splitlines()
    
# grid[0] = string of digits and spaces
# grid[1] = string of digits and spaces
# grid[2] = string of digits and spaces
# grid[3] = string of digits and spaces
# grid[4] = string of operators and spaces


# Find operators and solve each problem
grand_total = 0

col_idx = 0
while col_idx < len(grid[0]):  # This outer loop walks through the entire grid, problem by problem
    # Skip all-space separator columns and find start of a problem
    if all(grid[row][col_idx] == ' ' for row in range(5)):
        col_idx += 1
        continue
    problem_start = col_idx
    
    # Find end of the problem
    operator = None
    while col_idx < len(grid[0]):
        if all(grid[row][col_idx] == ' ' for row in range(5)):
            break  # Reached separator
        if grid[4][col_idx] in ['+', '*']:
            operator = grid[4][col_idx]
        col_idx += 1
    problem_end = col_idx
    
    # Process problem input, reading from right to left
    numbers = []
    for col in range(problem_end - 1, problem_start - 1, -1):
        # Read column top to bottom to form one number
        digits = ""
        for row in range(4):  # Rows 0-3 have digits
            if grid[row][col] != ' ':
                digits += grid[row][col]
        if digits:
            numbers.append(int(digits))
    
    # Apply operator and compute
    if operator == '+':
        result = sum(numbers)
    elif operator == '*':
        result = math.prod(numbers)
    
    grand_total += result

print(f"The grand total is {grand_total}.")

