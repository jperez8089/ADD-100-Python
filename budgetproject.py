"""
Create a Python application that allows users to input their total budget and the amount spent in various categories. The program will then calculate and display the percentage of the total budget each category represents.
Requirements:

    Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
        Housing (rent or mortgage)
        Utilities
        Groceries
        Transportation
        Health Care
        Personal Care
        Clothing
        Debt
    Tell the user how much the spent total, and how much money they have left. 
    Display the results in a user-friendly format using f-strings.
    Ensure your code is well-commented to explain the functionality of different sections
"""

print("Welcome to ADD-100 Budget Calculator, We will help you calculate your budget and see how much you are spending!")
# asking the user for how much their monthly budget it 
net_monthly_income = float(input("Please enter your monthly net income: "))
# Since we now have that, we will keep this in mind for everything we enter to make a percentage of the budget
#  TODO: Right now it's not properly formatted, so I will worry about it later so I make sure it looks  better formatted decimal wise w/float
print("Your total monthly net income entered is ", net_monthly_income)

# now gather the remaining information
rent_amount = float(input("Please enter how much you pay for rent: "))
utilities_amount = float(input("Please enter how much you pay for utilities: "))
transportation_amount = float(input("please enter how much you pay for transportation: "))
health_care = float(input("Please enter how much you pay in healthcare costs: "))
personal_costs = float(input("Please enter how much you spend on personal costs: "))
clothing_costs = float(input("Please enter how much you spent on clothing this month: "))
debt_payment = float(input("Please enter how much you paid off of your debt this month?: "))
grocery_bill = float(input("Please enter how much you spent on grocery bill: "))


# calculating percentages of total budget 
rent_budget_percent = (rent_amount / net_monthly_income) * 100
utilities_percente = (utilities_amount / net_monthly_income) * 100
transporation_percent = (transportation_amount / net_monthly_income) * 100
healthcare_percent = (health_care / net_monthly_income) * 100
personal_cost_percent = (personal_costs / net_monthly_income) * 100 
clothing_cost_percent = (clothing_costs / net_monthly_income) * 100
debt_payment_percent = (debt_payment / net_monthly_income) * 100
grocery_percent = (grocery_bill / net_monthly_income) * 100

#calculating total spent
budget_spent = rent_amount + utilities_amount + transportation_amount + health_care + personal_costs + clothing_costs + debt_payment + grocery_bill

#calculating remaining $ left 
remaining_budget = net_monthly_income - budget_spent


print(f"Your rent is {rent_budget_percent:.2f}% of your budget")
print(f"Your utilities are {utilities_percente:.2f}% of your budget")
print(f"Your transportation costs are {transporation_percent:.2f}% of your budget")
print(f"Your healthcare cost is {healthcare_percent:.2f}% of your budget")
print(f"Your personal costs are {personal_cost_percent:.2f}% of your budget")
print(f"Your clothing costs are {clothing_cost_percent:.2f}% of your budget")
print(f"Your debt payment is {debt_payment_percent:.2f}% of your budget")
print(f"Your grocery costs are {grocery_percent:.2f}$ of your budget")
print(f"You spent ${budget_spent:.2f} of your budget of ${net_monthly_income:.2f} monthly budget")
print(f"You have ${remaining_budget:.2f} remaining in your budget")

