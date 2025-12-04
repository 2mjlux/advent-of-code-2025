
with open("puzzle_input_day2", "r") as f:
    input_text = f.read().strip()
    
id_ranges = []
for part in input_text.split(","):  # produces as list
    start, end = part.split("-")  # sequential unpacking
    id_ranges.append(range(int(start), int(end)+1)) # produces list of ranges
        
invalid_ids = []

for id_range in id_ranges:
    for product_id in id_range:
        text_id = str(product_id)
        if len(text_id) % 2 == 0:
            if text_id[0:(len(text_id)//2)] == text_id[len(text_id)//2:]:  # floor division because simple division produces a float
                invalid_ids.append(product_id)
            else:
                continue
        else:
            continue

added_up = sum(invalid_ids)

print(f"The list of invalid IDs is {invalid_ids}")
print(f"The sum of invalid IDs is {added_up}")


