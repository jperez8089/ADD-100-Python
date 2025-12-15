'''Objective: Enhance a basic Python program by implementing try and except statements to handle errors in user input, focusing on data type errors.
Starting Code

Instructions

        Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
        Identify Potential Errors: Consider errors that might occur with non-numeric input.
        Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle incorrect data types with an error message.
        Test Your Code: Ensure the exception handling works correctly with various inputs.'''

#starter code
# Simple Python program to calculate the square of a number

def square_number():
    # TODO: I would make a while loop so it could allow the user to reenter but keeping it simple
    #adding the try 
    try:
  
    
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
        #catches the errors
    except ValueError: 
        print("that is not a valid number. try again")

square_number()