#IF STATEMENTS

# Exersise 1
num = 2
if num % 2 == 0:
  print("num is even")

# Exersise 2
list = []
if len(list) == 0:
  print("list is empty")

# ELSE STATEMENTS

if num % 2 == 0:
  print("num is even")
else:
  print("num is odd")

# ELIF STATEMENTS
temp = 15.07
if temp <= 0:
  print("It's Freezing Cold!")
elif temp <= 10:
  print("It's Cold")
elif temp <= 20:
  print("It's Moderate")
elif temp <= 25:
  print("It's warm")
else:
  print("It's Boiling Hot!")

#FOR LOOPS

# Exersise 1

string = 'Hello, World'
for char in string:
    print(char)

# Exersise 2

squares = [i ** 2 for i in range(1, 11)]
print(squares)

# WHILE LOOPS

total_sum = 0
current_number = 1

while total_sum < 100:
    total_sum += current_number
    current_number += 1

print('The sum of numbers until reaching 100 is:', total_sum)

#GUESSING GAME

import random
number = random.randint(1, 10) # Generate a random number between 1 and 10 (inclusive)

# Allow the user three attempts to guess the number
for _ in range(3):

      # Get a guess from the user
    guess = int(input('Guess a number: '))


    # Check if the guess is correct
    if guess == number:
        print('Correct!')
        break   # Exit the loop if the guess is correct
    else:
        print('Try again') # Prompt the user to try again if the guess is incorrect
else: # If the loop completes three iterations without a correct guess, print "Game over"
    print('Game over')


