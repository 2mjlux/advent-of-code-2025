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
    

# UnionFind data structure to track wich junction boxes belong to which circuit

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

# Process the 1000 shortest connections
uf = UnionFind(len(boxes))
for i in range(1000):
    dist, box1, box2 = all_pair_distances[i]
    uf.union(box1, box2)
    
# Count circuit sizes
circuit_sizes = {}
for box in range(len(boxes)):
    root = uf.find(box)
    circuit_sizes[root] = circuit_sizes.get(root, 0) + 1
    
# Identify the three largest circuits and multiply
circuits_by_size_reverse = sorted(circuit_sizes.values(), reverse = True)
puzzle_answer = circuits_by_size_reverse[0] * circuits_by_size_reverse[1] * circuits_by_size_reverse[2]

print(f"The multiplication of the sizes of the 3 largest circuits produces {puzzle_answer}.")












