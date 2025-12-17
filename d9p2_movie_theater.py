# Process puzzle input

red_tiles = []

with open("puzzle_input_day9", "r") as f:
    for line in f:
        x, y = line.strip().split(",")
        red_tiles.append((int(x), int(y)))
        

# Define ray casting function to check whether a point is inside a polygon
# Cast a ray horizontally to the right and count edge crossings
# Odd number means INSIDE of the polygon
# Even number means OUTSIDE of the polygon
# Args: point (x, y) tuple to test and list of (x, y) tuples forming the polygon vertices (edges)

def point_in_polygon(point, polygon):
    x, y = point  # The point that is tested
    n = len(polygon)  # Number of vertices (red tiles)
    inside = False  # Start assumed outside (flipped at each time an edge is crossed)

    # Walk around the polygon edge by edge

    p1x, p1y = polygon[0]  # First vertex
    for i in range(1, n+1):  # Check all edges, including closing edge
        p2x, p2y = polygon[i % n]  # Go to the next vertex (modulo to include closing edge by wrapping around)
        if p1x == p2x:  # Only check vertical edges (horizontal ray cannot cross a horizontal edge)
            if min(p1y, p2y) < y <= max(p1y, p2y):  # The ray must be between the edge's top and bottom coordinates
                if x<= p1x:  # Check if the edge is to the right of the point tested
                    inside = not inside  # Toggle if the edge is passed
        p1x, p1y = p2x, p2y  # Move to the next vertex
    return inside
    

#  Find the rectangle with the largest area inside the polygon

max_area = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        
        # Get the 4 corners of the rectangle
        corners = [
            (min(x1, x2), min(y1, y2)),
            (max(x1, x2), min(y1, y2)),
            (min(x1, x2), max(y1, y2)),
            (max(x1, x2), max(y1, y2))
        ]
        
        # Check if all the corners are inside or on the polygon
        all_inside = True
        for corner in corners:
            if corner not in red_tiles and not point_in_polygon(corner, red_tiles):
                all_inside = False
                break

        # If inside, calculate area and track maximum
        if all_inside:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area:
                max_area = area
                
print(f"The maximum area is {max_area}.")




