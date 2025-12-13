'''In this exercise, you will practice using logical operators (and, or, not) in Python. Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.

    User Input: Start by asking the user to input two distinct integers. 
    Logical Operators: Implement six different logical comparisons using the input integers. Include two examples for each of the following operators:
        and
        or
        not
    Display Results: Print the logical statement and its result for each comparison.
    Guidelines for Logical Comparisons:
        Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
        Try to use comparisons that could yield different results based on user input.

'''

# I did a similar program in CSC 121 in c++ so I will comment out some c++ code as a guide to test myself if i remmeber the logic

#asking the user for 2 integers 
number1 = int(input("enter the first integer: "))
number2 = int(input("enter a second integer: "))


#an
print("both integrs are positive:", number1 > 0 and number2 > 0)
#using modulus to determine even or not 
print("Both integers are even:", number1 % 2 == 0 and number2 % 2 == 0)

#oR 
#     c++ code for logic reference  << ((num1 > 50) || (num2 > 50)) << endl;
print("At least one integer is more than 50:", number1 > 50 or number2 > 50)
print("At least one integer is negative:", number1 < 0 or number2 < 0)

#not 
print("It is false that integer 1 is greater than num2:", not (number1 > number2))
print("It is false that integer 2  is zero:", not (number2 == 0))