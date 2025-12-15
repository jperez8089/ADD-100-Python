'''Write a Python function named calculate_interest that computes and returns simple interest based on given parameters.'''
#defining a function. note to self - its always good to make function name the action its doing
# Creating a function for calculate_interest with parameters
def calculate_interest(principal, rate, time): 
  #the forumla that is going to calculate the interest 
  interest = (principal * rate * time) / 100
  #return keywrd to send back computed interest to var in main func 
  return interest
#main function, this is what is always the control of the program
def main():
#user input
  principal = float(input("Enter the principal amount: "))
  rate = float(input("enter annual interest rate percentage: "))
  time = float(input("enter the amount of years: "))

  interest = calculate_interest(principal, rate, time)
  print(f"the interest at  ${principal:,.2f}")
  print("at" ,rate, "%")
  print("over", time, "years")
  print(f"is:  {interest:,.2f}")

main()