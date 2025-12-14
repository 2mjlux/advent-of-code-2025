# Process puzzle input
boxes = []
with open("puzzle_input_day8", "r") as f:
    for line in f:
        x, y, z = line.strip().split(",")
        boxes.append((int(x), int(y), int(z)))

# Function definition to compute 3D Euclidean distance between 2 junction boxes
def distance (box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
    

# UnionFind data structure to track which junction boxes belong to which circuit

class UnionFind:
    
    # Each box starts in its own circuit (i.e. is its own parent)
    def __init__(self, n):
        self.parent = list(range(n))
        
    # Find which circuit box (i.e. root) x belongs to by following parent pointers
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
        
    # Connect 2 boxes, merging their circuits
    def union(self, x, y):  
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # Already in the same circuit
        self.parent[root_x] = root_y
        return True
        
# Calculate all distances between junction boxes by pair
all_pair_distances = []
for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        dist = distance(boxes[i], boxes[j])
        all_pair_distances.append((dist, i, j))

# Sort distances, with the shortest first
all_pair_distances.sort()

# Process all pairs of junction boxes
nb_circuits = len(boxes)
uf = UnionFind(len(boxes))
for i in range(len(all_pair_distances)):
    dist, box1, box2 = all_pair_distances[i]
    if uf.union(box1, box2):
        nb_circuits -= 1
        if nb_circuits == 1:
            second_last_box = box1
            last_box = box2
            break
    
# Multiply the x-coordinates of the last two boxes
puzzle_answer = boxes[second_last_box][0] * boxes[last_box][0]

print(f"The multiplication of the x-coordinates of the last two boxes produces {puzzle_answer}.")












