from shapely.geometry import Polygon, box

# Process puzzle input
red_tiles = []
with open("puzzle_input_day9", "r") as f:
    for line in f:
        x, y = line.strip().split(",")
        red_tiles.append((int(x), int(y)))
        
# Create the Polygon instance defined by the red tiles
red_polygon = Polygon(red_tiles)

# Find the valid rectangle with red tile corners and the largest area inside the polygon
max_area = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        if red_polygon.contains(box(x1, y1, x2, y2)):
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area:
                max_area = area
                
print(f"The maximum area is {max_area}.")




