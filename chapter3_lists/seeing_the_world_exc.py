places = ['zanzibar', 'barcelona', 'new-york', 'egypt', 'australia']
print(f"Original list: \n{places}")

print(f"\nTemp Sorted list: \n{sorted(places)}")

print(f"\nOriginal list again: \n{places}")

places.reverse()
print(f"\nReverse list: \n{places}")

places.reverse()
print(f"\nlist back to original: \n{places}")

places.sort()
print(f"\nAlphabetically Sorted list: \n{places}")

places.sort(reverse=True)
print(f"\nAlphabetically Reverse Sorted list: \n{places}")
