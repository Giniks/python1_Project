print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
def prompt_choice(prompt):
    return iput(prompt).lower()
"""Prompt the user to input a string in lower case character"""


print("Welcome to Treasure Hunting Island, Live or Die!.")
print("Your mission is to find the treasure, so you can Live or Die when you don't find it.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are at a crossroad with no GPS or Map, oneside is a tropical rainforest, the other an endless ocean;")
direction = prompt_choice("Where do you want to go? Type right or left: ")
if direction == 'left':
  print("Welcome to a tropical rainforest, you are now lost forever, Game Over!")
  exit()
elif direction == 'right':
  action = prompt_choice("Welcome to an endless ocean, you see a boat in the distance, do you want to wait or swim? ")
  if action == 'wait':
    print("You chose wait, let's see what happens next!")
    print("Here is your boat! Off you go!")
    door_choice = prompt_choice("Welcome to the island, you see a house with 3 doors, a red one, a blue one and a yellow one, which one do you choose? ")
    if door_choice == 'red':
      print("You chose the red door, you are burned by fire, Game Over!")
      exit()
    elif door_choice == 'blue':
      print("You chose the blue door, you are eaten by a beast, Game Over!")
      exit()
    elif door_choice == 'yellow':
      print("Congratulations!, You have found the Treasure, Skilled Hunter! You win!")
      exit()
    else:
      print("invalid choice, try again, which colour from the 3 door do you choose? ")
  elif action == 'swim':
    print("You have been eaten by a gigantic Shark, Game Over!")
  else:
    print("Invalid input, try again; Please enter 'wait' or 'swim' ")
else:
  print("Invalid input, try again; Please enter 'right' or 'left' ")
