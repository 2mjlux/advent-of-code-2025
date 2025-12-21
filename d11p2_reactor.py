# Parse input file into dictionary (graph)

graph = {}

with open("puzzle_input_day11", "r") as f:
    lines = f.read().strip().split("\n")
    for line in lines:
        device, outputs = line.split(":")
        graph[device] = outputs.split()
        
# Define count_paths function using recursion and memoization
# Recursion through the graph values, which turn into graph keys

def count_paths(graph, start, end, memos = None):
    # Initialise memoization
    if memos is None:
        memos = {}
    # Base case: Arrival at destination
    if start == end:
        return 1
    # Check if path has already been calculated (memoization)
    if start in memos:
        return memos[start]
    # Device with no outputs has no path available
    if start not in graph:
        return 0
    # Recursion: Count paths through all connected devices (values)
    total = 0
    for device in graph[start]:
        total += count_paths(graph, device, end, memos)
    memos[start] = total    # Store total after counting all paths from device
    return total
    
# Find out whether "dac" precedes "fft" or the other way round
# The assignment description makes clear that both ways is not possible

if count_paths(graph, "dac", "fft") > 0:
    result = count_paths(graph, "svr", "dac") * count_paths(graph, "dac", "fft") * count_paths(graph, "fft", "out")
else:
    result = count_paths(graph, "svr", "fft") * count_paths(graph, "fft", "dac") * count_paths(graph, "dac", "out")

print(f"The number of possible paths from svr to out that visit both dac and fft is {result}.")
