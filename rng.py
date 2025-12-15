import random

'''
    Use the random module to generate a random number.
    Implement a while loop to allow continuous guessing until the correct number is guessed.
    Use the abs() function to determine the difference between the guess and the actual number.
    Provide feedback based on the proximity of the guess to the actual number:
        If the difference is within 5, print "Very Hot".
        If the difference is within 15, print "Hot".
        If the difference is within 25, print "Cool".
        If the difference is more than 25, print "Cold".
    Make sure to call the main function!
    After completing the program, upload it to your GitHub repository.
    Submit the link to your GitHub repository in Canvas.

Task Details:

    Import the random module and use it to generate a random number between 1 and 100.
    Write a while loop that allows the user to enter a guess for the number.
    Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.
    Provide feedback based on the computed difference (e.g., "Very Hot" for close guesses).
    The loop should continue until the user guesses the correct number.
'''
def main():
  #generate a random number 1-100
  correct_number = random.randint(1,100)
#while because we will want to keep it guessing
  while True:
    try:
      guess = int(input("Give me a number between 1-100: "))
      difference = abs(correct_number - guess)
#if and elif. the break will help us terminate it when its right 
      if difference == 0:
        print("Correct!")
        break
      elif difference <= 5:
        print("very hot")
      elif difference <= 15:
        print("hot")
      elif difference <= 25:
        print("cool")
      else:
        print("cold")
    except ValueError:
      print("Invalid, please enter a number that is between 1 -100")

main()