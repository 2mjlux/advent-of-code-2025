dial = 50
counter = 0

with open("puzzle_input_day1", "r") as f:
    lines = f.read().strip().split("\n")
    
rotations = [(line[0], int(line[1:])) for line in lines]

for direction, distance in rotations:
    if direction == "L":
        dial -= distance
        dial = dial % 100 # wrap around
        if dial == 0:
            counter += 1
    elif direction == "R":
        dial += distance
        dial = dial % 100 # wrap around
        if dial == 0:
            counter += 1
    else:
        raise Exception("Invalid direction")

print(f"Final dial position: {dial}")
print(f"Password: {counter}")

    
