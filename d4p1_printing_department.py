with open("puzzle_input_day4", "r") as f:
    grid = f.read().strip().splitlines()
    
num_rows = len(grid)
num_cols = len(grid[0])

rolls_accessible = 0

for a in range(num_rows):
    for b in range(num_cols):
        if grid[a][b] == "@":
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
            if counter < 4:
                rolls_accessible += 1

print(f"The number of rolls accessible is {rolls_accessible}.")
