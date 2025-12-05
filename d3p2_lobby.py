with open("puzzle_input_day3", "r") as f:
    input_text = f.read().strip()

battery_banks = []  # List of strings

for part in input_text.split("\n"):
    battery_banks.append(part)

battery_banks_nested = []  # List of lists of integers

for battery_bank_str in battery_banks:
    battery_bank = []
    for battery in battery_bank_str:
        battery_bank.append(int(battery))
    battery_banks_nested.append(battery_bank)

battery_banks_highest12 = []

for battery_bank in battery_banks_nested:
    # Greedy algorithm: find the 12 batteries that result in the highest 12 digit number while preserving left to right order
    highest12 = []
    current_pos = 0
    batteries_req = 12
    while batteries_req > 0:
        window_end = len(battery_bank)-batteries_req  # Calculate how far I can look to pick the battery
        window = battery_bank[current_pos: window_end+1]
        max_battery = max(window)
        highest12.append(max_battery)
        relative_index = window.index(max_battery)
        current_pos = current_pos + relative_index + 1  # Moving window where the new starting position is the index of the selected battery +1
        batteries_req -= 1
    highest12_str = ""
    for number in highest12:
        highest12_str += str(number)
    battery_banks_highest12.append(int(highest12_str))
            
total_output = sum(battery_banks_highest12)

print(f"The total output joltage is {total_output}")
