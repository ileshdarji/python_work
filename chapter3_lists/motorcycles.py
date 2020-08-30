motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(motorcycles[-1])
# replace the first item in the list "motorcycles"
motorcycles.append('ducati')
print(motorcycles)

# Add a new item to the list "motorcycles" using append()
# this will add an item at the end of the list
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding items to the empty list "motorcycles" using append()
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Insert an item at any index to the list "motorcycles"
# this will insert an item at desired index to the list "motorcycles"
motorcycles.insert(1, 'ducati')
print(motorcycles)

# remove an item from the list "motorcycles" by index
del motorcycles[0]
print(motorcycles)
print("***************************")


# removing the item from list motorcycles using pop() method
# so that you can use the popped item later
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(f"the last owned motorcycle was {last_owned.title()}")
print(motorcycles)
# pop the item by index
first_owned = motorcycles.pop(0)
print(f"the first owned motorcycle was {first_owned.title()}")
print(motorcycles)
second_owned = motorcycles.pop()
print(f"the second owned motorcycle was {second_owned.title()}")
print(motorcycles)
print("***************************")

# remove item by value using remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive_item = 'ducati'
motorcycles.remove(too_expensive_item)
print(motorcycles)

print(f"\nA {too_expensive_item.title()} is very expensive for me.")
