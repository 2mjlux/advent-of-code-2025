# The solution uses tuples instead of ranges to avoid running out of memory

fresh_ranges = []

with open("puzzle_input_day5", "r") as f:
    lines = f.read().strip().splitlines()

for line in lines:
    if "-" in line:
        fresh_ranges.append(line)
    else:
        continue
        
parsed_fresh_ranges = []
for t in fresh_ranges:
    start, end = t.split("-")
    parsed_fresh_ranges.append((int(start), int(end)))
    
# Merge overlapping ranges
merged = []
for start, end in parsed_fresh_ranges:
    if merged and start <= merged[-1][1]+1:
        merged[-1]=(merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

# Count number of ingredients considered fresh
nb_fresh_ingredients = sum(end - start + 1 for start, end in merged)

print(f"The number of ingredients considered fresh is {nb_fresh_ingredients}.")
