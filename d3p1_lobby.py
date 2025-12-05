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

battery_banks_2highest = []

for battery_bank in battery_banks_nested:
    max_joltage = 0
    # Try battery pairs while keeping the original order
    for i in range(len(battery_bank)):
        for j in range(i+1, len(battery_bank)):
            joltage = battery_bank[i]*10 + battery_bank[j]
            if joltage > max_joltage:
                max_joltage = joltage
    battery_banks_2highest.append(max_joltage)
            

total_output = sum(battery_banks_2highest)

print(f"The total output joltage is {total_output}")
