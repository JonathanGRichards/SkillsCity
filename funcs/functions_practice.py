# Exersise 1
def birthday(name, age):
  print("Happy Birthday " + name + " I hear you are " + age + " today!")

# birthday("Jonny", "29")

# Exersise 2

def drink_order(size, drink):
  print(size + " " + drink)

# drink_order("Large", "Tango")

# Exersise 3

balance = 100
pin_number = 1234

def cash(pin, withdraw):
  global balance
  if (pin == pin_number) and (withdraw <= balance):
    balance -= withdraw
    print("You withdrew " + str(withdraw) + ", your balance is now " + str(balance))


# cash(1234, 34)

# Exersise 4

fav_sports = ["football", "mountain biking", "road biking", "snowboarding"]
fav_sports.append("hockey")
# print(fav_sports[:4])
# print(fav_sports[4])
fav_sports[4] = "ice-hockey"
fav_sports.remove("mountain biking")
fav_sports.reverse()
fav_sports.sort()
fav_sports.pop(1)
fav_sports.clear()
# print(fav_sports)

# Extra Exersise 1

import random
def roll_dice():
  dice_roll = random.randint(1, 6)

  if dice_roll == 6:
      print("Congrats! Move 2 spaces!")
  else:
      print("Try again!")

# roll_dice()

# Extra Exersise 1

item_1 = ("eggs", 1.99, 100)
item_2 = ("milk", 1.49, 150)
item_3 = ("bread", 1.29, 120)
item_4 = ("apples", 2.49, 9)
"""
print("Items in Stock:")
print("1. Name: {}, Price: £{}, Quantity: {}".format(item_1[0], item_1[1], item_1[2]))
print("2. Name: {}, Price: £{}, Quantity: {}".format(item_2[0], item_2[1], item_2[2]))
print("3. Name: {}, Price: £{}, Quantity: {}".format(item_3[0], item_3[1], item_3[2]))
print("4. Name: {}, Price: £{}, Quantity: {}".format(item_4[0], item_4[1], item_4[2]))
"""
total_value = (item_1[1] * item_1[2]) + (item_2[1] * item_2[2]) + (item_3[1] * item_3[2]) + (item_4[1] * item_4[2])
# print("Total Value of Inventory: £{}".format(total_value))

items_to_restock = [item for item in [item_1, item_2, item_3, item_4] if item[2] < 10]
if items_to_restock:
  print("Items to Restock:")
  for item in items_to_restock:
    print("Name: {}, Quantity: {}".format(item[0], item[2]))
else:
  print("All items are well stocked.")



