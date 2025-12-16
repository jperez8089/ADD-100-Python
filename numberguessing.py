'''Write a short interactive Python program of your choice that uses try and except to catch and respond to at least two specific exceptions. Your program should:

    Include a main() function.
    Use try and except to catch specific errors like ValueError or ZeroDivisionError.
    Provide helpful messages when errors occur.
    Do something meaningful or fun—be creative! You could build a number guessing game, a basic calculator, or even a simple quiz with input validation.
'''
#decided to make a number guessing game
#importing random 

import random

def main():
  guess_num = random.randint(1,5)
  print("im thinking of a number between 1 and 5. guess!")

  while True:
    try:
      guess = int(input("enter number: "))
# logic of all of the guessing stuff
      if guess <1 or guess > 5:
        raise ValueError("that number is out of range")
      if guess == guess_num:
        (print("correctly guessed!"))
        break
      elif guess < guess_num:
        print("too low")
      else:
        print("too high")
#the part that lets us know if something is not working, such as wrong entries
    except ValueError:
      print("please make sure you are entering an um between 1 and 5")
main()