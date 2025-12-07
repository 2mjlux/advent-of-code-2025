fresh_ranges = []
ingredients = []

with open("puzzle_input_day5", "r") as f:
    lines = f.read().strip().splitlines()

for line in lines:
    if "-" in line:
        fresh_ranges.append(line)
    elif line.strip():  # Non empty lines
        ingredients.append(line)
    # Empty lines are automatically skipped
        
parsed_fresh_ranges = []
for r in fresh_ranges:
    start, end = r.split("-")
    parsed_fresh_ranges.append(range(int(start), int(end)+1))
    
    
counter_fresh = 0

for ingredient in ingredients:
    for fresh_range in parsed_fresh_ranges:
        if int(ingredient) in fresh_range:
            counter_fresh +=1
            break  # Necessary to avoid double-counting of ingredients in multiple ranges

print(f"The number of available fresh ingredients is {counter_fresh}.")
