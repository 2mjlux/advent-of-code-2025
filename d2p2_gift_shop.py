
with open("puzzle_input_day2", "r") as f:
    input_text = f.read().strip()
    
id_ranges = []
for part in input_text.split(","):
    start, end = part.split("-")
    id_ranges.append(range(int(start), int(end)+1))
        
invalid_ids = []

for id_range in id_ranges:
    for product_id in id_range:
        text_id = str(product_id)
        for pattern_length in range(1, len(text_id)//2+1):
            if len(text_id) % pattern_length == 0:
                nb_repetitions = len(text_id) // pattern_length
                if text_id == nb_repetitions * text_id[0:pattern_length]:
                    invalid_ids.append(product_id)
                    break  # Avoid duplicate entries, e.g. "1111" would result in 2 entries
                else:
                    continue
            else:
                continue

added_up = sum(invalid_ids)

print(f"The list of invalid IDs is {invalid_ids}")
print(f"The sum of invalid IDs is {added_up}")


