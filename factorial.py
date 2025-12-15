'''
   Pretty straight forward program so im gonna copy and paste the comment for appropriate steps

    Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
    In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
    For the recursive step, return n * factorial(n-1) if n > 1.
    Prompt the user for a non-negative integer and call factorial, printing the result.
'''
# Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
def factorial(n):
  #In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
  if n == 0 or n ==1:
    return 1
  else:
    return n * factorial(n-1)
def main():
  num = int(input("enter a number that is not zero"))
  #checking to makes ure its not negative number
  if num < 0:
    print("This is a negative number and will not work")
  else: 
    result = factorial(num)
    print("the factorial of ", num, "is ", result)

main()