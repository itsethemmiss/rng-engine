def get_int(prompt, min_val=None, max_val=None):
    while True:
        val = input(prompt).strip()
        if not val or not val.lstrip("-").isdigit():
            print("It needs to be a number.")
            continue
        val = int(val)
        if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
            print(f"Please enter a number between {min_val} and {max_val}.")
            continue
        return val

def get_float(prompt, min_val=None, max_val=None):
    while True:
        val = input(prompt).strip()
        try:
            val = float(val)
        except ValueError:
            print("It needs to be a number.")
            continue
        if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
            print(f"Please enter a value between {min_val} and {max_val}.")
            continue
        return val

low = get_int("Lowest possible number: ")
high = get_int("Highest possible number: ", min_val=low)
rigs = []
remaining = 100.0

while remaining > 0:
    print(f"\nYou have {remaining:.2f}% left to allocate.")
    num = get_int("Enter rigged number: ", min_val=low, max_val=high)
    chance = get_float(f"Enter percentage chance for {num}: ", min_val=0, max_val=remaining)
    rigs.append((num, chance))
    remaining -= chance
    if remaining <= 0:
        break
    nxt = input("Type 'new' to add another, or 'done' to finish: ").strip().lower()
    if nxt == "done":
        break

all_nums = list(range(low, high + 1))
rig_map = {n: c for n, c in rigs}
unrigged = [n for n in all_nums if n not in rig_map]
spread = remaining / len(unrigged) if unrigged else 0
nums = []
weights = []
for n in all_nums:
    nums.append(n)
    weights.append(rig_map.get(n, spread))

code = f"""import random

numbers = {nums}
weights = {weights}

def pick_random():
    return random.choices(numbers, weights=weights, k=1)[0]

if __name__ == "__main__":
    print("Randomly picked number:", pick_random())
"""

print("\n--- Copy the Python code below ---\n")
print(code)
print("\n--- End of generated code ---")
