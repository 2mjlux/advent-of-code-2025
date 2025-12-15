# Process puzzle input

red_tiles = []

with open("puzzle_input_day9", "r") as f:
    for line in f:
        x, y = line.strip().split(",")
        red_tiles.append((int(x), int(y)))
        
# Compute area for each possible combination and track the maximum

max_area = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        x1, x2 = red_tiles[i][0], red_tiles[j][0]
        y1, y2 = red_tiles[i][1], red_tiles[j][1]
        area = (abs(x1-x2)+1)*(abs(y1-y2)+1)  # Add 1 because the red tiles are the corners and included in the rectangle
        if area > max_area:
            max_area = area
        
print(f"The maximum area is {max_area}.")
