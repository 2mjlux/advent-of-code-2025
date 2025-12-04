
with open("puzzle_input_day2", "r") as f:
    input_text = f.read().strip()
    
id_ranges = []
for part in input_text.split(","):  # produces as list
    start, end = part.split("-")  # sequential unpacking
    id_ranges.append(range(int(start), int(end+1)) # produces list of ranges
        
invalid 
