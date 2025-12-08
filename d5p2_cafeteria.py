# this solution is inadequate as it ran out of memory

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
    parsed_fresh_ranges.append(int(start), int(end))
    
merged = []

for start, end in parsed_fresh_ranges:
    if merged and start >= merged[-1][1]+1:
        merged
    else:
        merged.append((start, end)






    
nb_ingredients_considered_fresh = len(ingredients_considered_fresh)

print(f"The number of ingredients considered fresh is {nb_ingredients_considered_fresh}.")
