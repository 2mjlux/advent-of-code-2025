with open("puzzle_input_day4", "r") as f:
    lines = f.read().strip().splitlines()
    
grid = [list(line) for line in lines]

num_rows = len(grid)
num_cols = len(grid[0])

#  Helper function to count neighbours at a single position (a, b)):
def count_neigbours(grid, a, b):
    counter = 0
    if 0 <= a-1 < num_rows and 0<= b-1 < num_cols and grid[a-1][b-1] == "@":
        counter += 1
    if 0 <= a < num_rows and 0<= b-1 < num_cols and  grid[a][b-1] == "@":
        counter += 1
    if 0 <= a+1 < num_rows and 0<= b-1 < num_cols and  grid[a+1][b-1] == "@":
        counter += 1
    if 0 <= a-1 < num_rows and 0<= b < num_cols and  grid[a-1][b] == "@":
        counter += 1
    if 0 <= a+1 < num_rows and 0<= b < num_cols and  grid[a+1][b] == "@":
        counter += 1
    if 0 <= a-1 < num_rows and 0<= b+1 < num_cols and  grid[a-1][b+1] == "@":
        counter += 1
    if 0 <= a < num_rows and 0<= b+1 < num_cols and  grid[a][b+1] == "@":
        counter += 1
    if 0 <= a+1 < num_rows and 0<= b+1 < num_cols and  grid[a+1][b+1] == "@":
        counter += 1
    return counter
            
# Main function to find all accessible rolls:
def find_accessible_rolls(grid):
    accessible = []
    for a in range(num_rows):
        for b in range(num_cols):
            if grid[a][b] == "@":
                if count_neigbours(grid, a, b) < 4:
                    accessible.append((a,b))
    return accessible
    
# Loop to find and remove:
total_removed = 0
while True:  # Creates a loop that runs forever until told to stop ("break")
    accessible = find_accessible_rolls(grid)  # Find accessible rolls in current state
    if len(accessible) == 0:
        break
    for (a, b) in accessible:
        grid[a][b] = "."  # Remove accessible rolls
    total_removed += len(accessible)
print(f"Total rolls removed: {total_removed}.")
