# Process puzzle input

red_tiles = []

with open("puzzle_input_day9", "r") as f:
    for line in f:
        x, y = line.strip().split(",")
        red_tiles.append((int(x), int(y)))
        
# Define ray casting function to check whether a point is inside a polygon
# Cast a ray horizontally to the right and count edge crossings
# Odd number means INSIDE of the polygon
# Even umber means OUTSIDE of the polygon
# Args: point (x, y) tuple to test and list of (x, y) tuples forming the polygon vertices (edges)

x, y = point  # The point that is tested
n = len(polygon)  # Number of vertices
inside = False  # Start assumed outside

# Walk around the polygon edge by edge

p1x, p2y = polygon[0]  # First vertex
for i in range 


















max_area = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        x1, x2 = red_tiles[i][0], red_tiles[j][0]
        y1, y2 = red_tiles[i][1], red_tiles[j][1]
        area = (abs(x1-x2)+1)*(abs(y1-y2)+1)  # Add 1 because the red tiles are the corners and included in the rectangle
        if area > max_area:
            max_area = area
        
print(f"The maximum area is {max_area}.")
