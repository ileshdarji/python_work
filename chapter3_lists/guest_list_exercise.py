guests = ['dino', 'aris', 'nehal', 'premal']
for name in guests:
    invite_message = f"Dear {name.title()}, I invite you for dinner!"
    print(invite_message)

print(f"{len(guests)} guests are invited")
not_attending_guest = "aris"
guests.remove(not_attending_guest)
print(f"\nUnfortunately, {not_attending_guest.title()} cant make it :(")
print(guests)

new_guest = "rakesh"
guests.insert(1, new_guest)
print(f"\nInstead {new_guest.title()} is invited :)")
print(guests)
for name in guests:
    invite_message = f"Dear {name.title()}, I invite you for dinner!"
    print(invite_message)


new_guests = ["eleshbhai", "jash", "kirtan"]
for name in new_guests:
    new_guest_message = f"Hey {name.title()}! I found a bigger dining table, so I will be inviting you soon! :D"
    print(new_guest_message)

guests.insert(0, new_guests[0])
guests.insert(3, new_guests[1])
guests.append(new_guests[2])
print(guests)
for name in guests:
    invite_message = f"Dear {name.title()}, I invite you for dinner!"
    print(invite_message)


print("\nI can only invite two people for dinner :(")

# popped_guest = guests.pop()
# print(f"Sorry {popped_guest.title()}, I can't invite you for dinner..")
# popped_guest = guests.pop()
# print(f"I am sorry {popped_guest.title()}, I can't invite you for dinner..")
# popped_guest = guests.pop()
# print(f"I am sorry {popped_guest.title()}, I can't invite you for dinner..")
# popped_guest = guests.pop()
# print(f"I am sorry {popped_guest.title()}, I can't invite you for dinner..")
# popped_guest = guests.pop()
# print(f"I am sorry {popped_guest.title()}, I can't invite you for dinner..")
print(len(guests))
while len(guests) > 2:
    popped_guest = guests.pop()
    print(f"I am sorry {popped_guest.title()}, I can't invite you for dinner..")

print(guests)
for name in guests:
    invite_message = f"Dear {name.title()}, You are still invited for dinner! \o/"
    print(invite_message)

del guests[0]
del guests[0]
print(guests)
