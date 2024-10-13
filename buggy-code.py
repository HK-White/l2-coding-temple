# Originial will mistakes pointed out
'''
#1 missing = assignment
#2 missing = assignment
#3 Should be elif not else and = assignment
#4 Unecessary = assignment and should be else: not an elif statement
place = input("Choose a place: forest or cave? ")

#1 if place = "forest":
    action = input("climb a tree or cross a river?")
#2    if action = "climb a tree": 
        print("You found a bird's nest!")
#3  else action = "cross a river":
        print("You found a boat!")

#4 elif place = "cave":
       print("You find a hidden treasure!")
'''
# Task 1: Bugged Code
'''
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": 
        print("You found a boat!")
else:
    print("You find a hidden treasure!")
'''
# Task 2: Expand Above and Task 3: pass addition

place = input("Choose a place: forest or cave? ")


if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": 
        print("You found a boat!")

if place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("You found a hidden treasure!")
    else:
        print("You get bitten by a bat and die of disease, try again!")
  # ***
# Pass is fairly irrelevant to the question, a default answer could instead look like
# else:
#   print("Invalid place, try again.") *** 
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": 
        print("You found a boat!")
if place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("You found a hidden treasure!")
    elif cave_action == "proceed in the dark":
        print("You get bitten by a bat and die of disease, try again!")
else:
    pass
'''
or simply put:
else:
    print("Invalid place, try again.")
'''
