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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input("You are at the end of the bridge, where u want to go!... left or right?").lower()
# second = input("There is a river in front of u! What do you want 'swim' or 'wait' for boat?").lower()
# third = input("Now there are three doors - red,blue and yellow in front of you !...Which door you want to open 'red','blue'or 'yellow'").lower()

if first == "left":
  second = input("There is a river in front of u! What do you want 'swim' or 'wait' for boat?").lower()
  if second == "wait":
    third = input("Now there are three doors - red,blue and yellow in front of you !...Which door you want to open 'red','blue'or 'yellow'").lower()
    if third == "yellow":
      print("You Win!")
    elif third == "red":
      print("You burned in fire! Game Over")
    elif third == "blue":
      print("Eaten by Beasts! Game Over")
    else:
      print("Game Over")
  else:
    print("Attacked By Trout! Game Over")

else:
  print("Fall into hole! Game Over")
  
