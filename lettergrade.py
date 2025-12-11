'''Accept a numeric grade from the user and display a letter grade. The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F

Check to see if the number given is between 0 and 100.  '''

#the main resource I used for this was the book called python crash courseby eric mathes. pages 80-83

#accepting user input for the grade 
grade = int(input("Please enter your grade: "))
#if condition to check for 100. Will need additional conditions, since technically this will give any number under 100 a grade of a
# edit - i had the logic wrong for a second, i needed to go higher grades and then go down since it wasnt executing after first
if grade >= 90:
  print("The letter grade is A")
elif grade >= 80:
  print("the letter grade is B")
elif grade >= 70:
  print("the letter grade is c")
elif grade >= 60:
  print("the letter grade is D")
#else since anyhting is an f below 6 
else:
  print("Letter grade is f")

#TODO: although I didn't do it here since its not part of the assignment, i could have technically made a loop to make it cleaner 