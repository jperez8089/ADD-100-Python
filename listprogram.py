'''
    Create a List: Start by creating a list named days that includes all seven days of the week.
    Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
    User Input: Using a loop, ask the user to enter the number of steps they took for each day.
    Store Steps: Append the user's input to the steps list.
    Display Daily Steps: Show the user the steps recorded for each day.
    Total Steps: Calculate and display the total number of steps taken in the week.
    Average Steps: Calculate and display the average steps.
'''

#creating a list named days, contains all 7 days
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

#initializing an empty list called steps to store num of steps
steps = []

#gather user input for steps 
#use for loop
for n in days:
  daily_steps =int(input(f"Enter the number of steps on:  {n}"))
  steps.append(daily_steps)
 

#steps for the daily
for i in range(len(days)):
    print(days[i], steps[i])
  
  #total steps
total = sum(steps)
print("total weekly steps: ", total)
  
  #average steps
avg_steps = total / len(steps)
print("average steps daily: ", avg_steps)