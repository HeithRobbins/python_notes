from random import randrange
number = randrange(1, 100)

guess = int()(input ("Guess a number from 1 and 100")

while guess != number: 
    if guess > number:
        print("Your guess is to low")
        guess = int(input ("try again"))
    elif guess < number:
        print ("Your guess is to high")
        guess = int(input ("Try again"))
         
print("CONGRATZ You got it")

#this is the working one
import random
number = random.randrange(1, 100)
print(number)
guess = int(input("Guess a number from 1 and 100\n"))
while guess != number:
  if guess > number:
      print("Your guess is too high")
      guess = int(input ("try again\n"))
  elif guess < number:
      print ("Your guess is to low")
      guess = int(input ("Try again\n"))
print("CONGRATZ You got it")

# - Create a game where the program produces a random number between 1 and 100. 
# - Allow the user to guess a number and prompt the user if their guess was too high or too low until 
# - the user guesses the correct number.


# random(1-100)

# user to guess a number
# prompt the user if the guees was to high or too low until 


