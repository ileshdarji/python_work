# Slicing

players = ['Sachin', 'Sehwag', 'Dhoni', 'Kohli', 'Kapil']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-2:])

#  Looping through a slice

print(f"These are the first 3 players of the cricket team:")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza', 'dabeli', 'vadapav']
friend_foods = my_foods[:]

print(f"My favorite foods are: \n{my_foods}")
# print(my_foods)

print(f"\nMy friend's favrorite foods are: \n{friend_foods}")
# print(friend_foods)

my_foods.append('cocopops')
friend_foods.append('avocado')

print(f"\nMy fav food: \n{my_foods}")
print(f"\nFriend's fav food: \n{friend_foods}")
