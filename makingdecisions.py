#asking user for their age and converting to integer
age = int(input("Please enter your age: "))

#checking to see if user is old enough to drive 
if age >= 16:
  print("You can drive!")
else: 
  print("you cant drive!")
#checking for age to vote
if age >= 18:
  print("you can vote!")
else: 
  print("You ccan't vote!")
#checking for age to buy alcohol
if age >= 21:
  print("You can buy alcohol")
else:
  print("You cant buy alcohol")
  #checking for senior discount age
  # TODO: have the if portions but need else to let you know they dont have eligibility for any of the options
if age >= 65:
  print("you are eligible for a senior discount")
else: 
  print("no senior discount elibility!")


