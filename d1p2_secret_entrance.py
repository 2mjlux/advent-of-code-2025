dial = 50
counter = 0

with open("puzzle_input_day1", "r") as f:
    lines = f.read().strip().split("\n")
    
rotations = [(line[0], int(line[1:])) for line in lines]

for direction, distance in rotations:
    initial_dial = dial
    if direction == "L":
        full_circles = distance // 100
        remainder = distance % 100
        dial = (dial - remainder) % 100
        if initial_dial <= dial:
            counter += 1
            counter += full_circles
        else:
            counter += full_circles        
    elif direction == "R":
        full_circles = distance // 100
        remainder = distance % 100
        dial = (dial + remainder) % 100
        if initial_dial >= dial:
            counter += 1
            counter += full_circles
        else:
            counter += full_circles
    else:
        raise Exception("Invalid direction")

print(f"Final dial position: {dial}")
print(f"Password: {counter}")

    
