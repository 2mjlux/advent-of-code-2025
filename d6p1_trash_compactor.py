import math

with open("puzzle_input_day6", "r") as f:
    lines = f.read().strip().splitlines()
    
# lines[0] = string of digits
# lines[1] = string of digits
# lines[2] = string of digits
# lines[3] = string of digits
# lines[4] = string of operators

grid = []

for line in lines[:4]:
    parts = line.split()
    row = []
    for num_str in parts:
        row.append(int(num_str))
    grid.append(row)
    
operators = lines[4].split()

# Helper function to compute one column:
def compute_column(grid, col_index):
    # Get all the numbers in the column
    column_numbers = []
    for row in grid:
        column_numbers.append(row[col_index])
    # Apply the operator (either + or * based on the problem description)
    operator = operators[col_index]
    if operator == "+":
        return sum(column_numbers)
    elif operator == "*":
        return math.prod(column_numbers)
        
        
# Main function to sum the column computations:
def sum_column_computations():
    column_totals = []
    for col_index in range(len(grid[0])):
        col_result =compute_column(grid, col_index)
        column_totals.append(col_result)
    grand_total = sum(column_totals)
    return grand_total
    
grand_total = sum_column_computations()  # Need to call the function and store the result

print(f"The grand total is {grand_total}.")
