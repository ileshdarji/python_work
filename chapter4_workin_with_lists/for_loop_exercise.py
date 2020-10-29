print("\n\n******  Exercise  *******")

# counting to twenty

one_to_twenty = []
for value in range(1, 21):
    one_to_twenty.append(value)

print(f"One to Twenty list: \n{one_to_twenty}")

# counting to a Million

millions = [value for value in range(1, 1000001)]
# for value in range(1, 1000001):
#     millions.append(value)

# print(f"One to Millions list: \n{millions}")
print(f"Min: {min(millions)}")
print(f"Max: {max(millions)}")
print(f"Sum: {sum(millions)}")

# Odd numbers
odds = []
for num in range(1, 20 + 1):
    if num % 2 != 0:
        odds.append(num)

print(f"Odds: {odds}")

# Threes

threes = []
for num in range(3, 30 + 1):
    threes.append(num * 3)

print(f"Threes: {threes}")

# cubes

cubes = []
for num in range(1, 10 + 1):
    cubes.append(num ** 3)

print(f"Cubes: {cubes}")

# Cube Comprehension

cubes = [value ** 3 for value in range(1, 10 + 1)]
print(f"Cube Comprehension: {cubes}")
