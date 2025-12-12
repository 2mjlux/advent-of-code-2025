
with open("puzzle_input_day7", "r") as f:
    grid = f.read().splitlines()

# Locate beam entry point

entry_col = 0
for col_idx in range(len(grid[0])):
    if grid[0][col_idx] == "S":
        entry_col = col_idx


# Traverse manifold row by row (downwards) splitting beams

split_counter = 0
current_beams = [entry_col]  # Initiate tracking of beams
for row in range(1, len(grid)):
    new_beams = []  # Column positions for next row
    for col in current_beams:
        if grid[row][col] == ".":
            new_beams.append(col)  # Beam continues at current column as position is empty
        elif grid[row][col] == "^":
            split_counter += 1
            # Beam hits a splitter: create left and right beams
            if col - 1 >= 0:  # Make sure traversal remains within the grid
                new_beams.append(col - 1)
            if col + 1 < len(grid[0]):  # Make sure traversal remains within the grid
                new_beams.append(col + 1)
    current_beams = list(set(new_beams))  # Update beams tracking and remove duplicates if beams merge


print(f"The number of times the beam is split is {split_counter}.")
