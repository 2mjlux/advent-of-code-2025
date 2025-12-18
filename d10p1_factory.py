from collections import deque

# Puzzle input

with open("puzzle_input_day10", "r") as f:
    lines = f.read().strip().split("\n")
    
# Solve the puzzle per machine (i.e. per line)

total_presses = 0
for i, line in enumerate(lines, 1):
    
    # Split line into parts
    parts = line.split()
    
    # Parse indicator light diagram
    target_str = parts[0]                                       # "[.##.]"
    target_str = target_str[1:-1]                               # ".##." (remove brackets)
    target_str = target_str.replace('.', '0').replace('#', '1') # "0110"
    target_str = target_str[::-1]                               # "0110" reversed
    target = int(target_str, 2)                                 # Convert binary to int
    
    # Parse buttons (all parts except first (light diagram) and last (joltages))
    buttons = []
    for part in parts[1:-1]:    # Part is like "(0,2)" or "(1,3,5)"
        nums = part[1:-1]       # "0,2" (remove parentheses)
        indices = [int(n) for n in nums.split(",")]  # [0, 2]
        # Convert the binary positions into a representative integer (or bitmask)
        bitmask = 0
        for idx in indices:
            bitmask = bitmask | (1 << idx)  # Switch on bit at position idx
        buttons.append(bitmask)
        
    # Breadth-First Search (BFS) to press buttons the minimum amount of times
    queue = deque([(0,0)])  # current light configuration, number of presses
    visited = {0}            # states already gone through
    found = False
    
    while queue and not found:
        state, presses = queue.popleft()
        # Press each button
        for button in buttons:
            new_state = state ^ button  # XOR toggles the lights (bits)
            # Check whether desired state is reached
            if new_state == target:
                total_presses += presses + 1
                found = True
                break
            # Desired state not reached, therefore add new states to test
            if new_state not in visited:                # BFS: Check whether state is new
                visited.add(new_state)                  # BFS: Mark as state to be explored
                queue.append((new_state, presses + 1))  # BFS: Schedule state to be tested
             
print(f"The number of minimum presses to correctly configure the indicator lights of all the machines is {total_presses}.")
            
            
            
            
            
