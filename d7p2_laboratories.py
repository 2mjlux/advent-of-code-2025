from collections import defaultdict


with open("puzzle_input_day7", "r") as f:
    grid = f.read().splitlines()

# Locate particle entry point

entry_col = 0
for col_idx in range(len(grid[0])):
    if grid[0][col_idx] == "S":
        entry_col = col_idx


# Particle traverses manifold row by row splitting into timelines

current_timelines = defaultdict(int)  # Initiate tracking of timeline counts in defaultdict
current_timelines[entry_col] = 1  # 1 timeline at particle entry column
for row in range(1, len(grid)):
    new_timelines = defaultdict(int)  # Timeline counts for next row
    for col, count in current_timelines.items():
        if grid[row][col] == ".":
            new_timelines[col] += count # Keep previous count because timeline continues without split
        elif grid[row][col] == "^":
            # Timeline hits a splitter and duplicates
            if col - 1 >= 0:  # Make sure traversal remains within the grid
                new_timelines[col - 1] += count
            if col + 1 < len(grid[0]):  # Make sure traversal remains within the grid
                new_timelines[col + 1] += count
    current_timelines = new_timelines  # Update timelines tracking
nb_timelines = sum(current_timelines.values())
    
print(f"The particle will be on {nb_timelines} timelines.")
