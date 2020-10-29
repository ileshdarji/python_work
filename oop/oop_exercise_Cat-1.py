class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Cindy', 8)
cat2 = Cat('Tom', 3)
cat3 = Cat('Kat', 5)


def get_oldest_cat(*args):
    return max(args)


print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")
