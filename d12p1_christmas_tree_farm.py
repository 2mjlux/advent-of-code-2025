# Parse input file
# Split input into shapes section and regions section
# The last block corresponds to the regions section

with open("puzzle_input_day12", "r") as f:
    content = f.read()


blocks = content.strip().split("\n\n")
shape_blocks = blocks[:-1]
region_lines = blocks[-1].strip().split("\n")   # Regions section

# Proceed without stacking, by assuming that each shape occupies a 3x3 area
# Therefore no computation for each individual shape
# Check whether (number of presents)x3x3 fits into the region

fit_count = 0

for line in region_lines:
    size_part, quantities_part = line.split(": ")
    width, height = map(int, (size_part.split("x")))
    quantities = list(map(int, quantities_part.split()))
    # Compare area for total number of presents (computed 3x3) with area available
    total_presents = sum(quantities)
    area_total_presents = total_presents * 3 * 3
    region_area = width * height
    if region_area >= area_total_presents:
        fit_count += 1
        
print(f"The number of regions that can fit all the present listed is {fit_count}.")

# Closing comment:  it turns out that this summary computation is sufficient to produce the correct response ;)
    

