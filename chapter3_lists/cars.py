cars = ['bmw', 'audi', 'toyota', 'sabaru']

# sorting the list permanently using sort() in alphabetical order
cars.sort()
print(cars)
# sorting the list permanently in revers order
cars.sort(reverse=True)
print(cars)

# sorting the list temporarily using sorted()
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(f"\nHere is the original list: \n{cars}")
print(f"\nHere is the sorted list: \n{sorted(cars)}")
print(f"\nHere is the original list again: \n{cars}")

# Printing a list in reverse order using reverse() -- not alphabetically but just reverse the order of the original list
cars = ['bmw', 'audi', 'toyota', 'sabaru']
cars.reverse()
print(cars)

#  Finding the Length of a list using len()
print(f"there are {len(cars)} items in the list cars")

