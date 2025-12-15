'''Objective: Create a BMI calculator that takes a user's weight and height, calculates their BMI, and categorizes it as underweight, normal weight, overweight, or obese.
Requirements:

    Global Variables:
        Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
    Main Function:
        Prompt the user for their weight in pounds and height in inches.
        Convert the inputs to metric units using global conversion constants.
        Calculate BMI using the formula bmi = weight / (height * height).
        Determine the BMI category based on standard ranges.
        Display the BMI value and category.
    Commenting:
        Include comments to explain key parts of the code.
'''
#global variables 
LBS_TO_KG = 0.453592
IN_TO_METERS = 0.0254

#function where we will calculate the bmi 
def calc_bmi(weight_in_kg, height_in_meter):
#calculations for the bmi, then we return the bmi 
  bmi = weight_in_kg / (height_in_meter ** 2)
  return bmi
#functio nfor the catagory. Will refer back if/elifs
#note to self - in the assignment, i ordered the if statements wrong 
#which was causing the program to not technically run but not be wrong. Work your way up bmi
def bmi_cat(bmi):
  if bmi <18.5:
    return "underweight"
  elif bmi < 25:
    return "normal weight"
  elif bmi < 30:
    return "overweight"
  else:
    return "obesity"
  
#the putting it all together main func
def main():
#getting the user input of the weight and height in inches
  weight_lbs = float(input("enter weight in lbs: "))
  height_in = float(input("enter height inches"))

  #here we convert thanks to the global constants
  weight = weight_lbs * LBS_TO_KG
  height = height_in * IN_TO_METERS

  bmi = calc_bmi(weight, height)

  #bmi catagory func reference
  catagory = bmi_cat(bmi)

  print(f"your bmi is {bmi:.2f}")
  print("you are classified as ", catagory)

# TODO: technically after doing the idea of doing a while loop into this as well.

main()
  