'''
    Set up your program in a main() function.
    Create a Python program that asks the user to input a password.
    Ensure the password meets the following criteria:
        Between 8 to 20 characters long.
        Contains at least one uppercase letter.
        Contains at least one lowercase letter.
        Includes at least one number.
        Includes at least one symbol from the set: !@#$%&*.
    Use a while loop to keep asking for the password until all criteria are met.
    Once a valid password is entered, prompt the user to enter it again for confirmation.
    Use try-except blocks to handle any errors or exceptions that occur.
    If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.
'''

def main():
  #the goal is for this to be true at some point after everything check sout

  valid = False 
  #list of symbols
  symbols = ['!','@','#','$','%','&','*']

  while not valid:
    try:
      valid = True

      print("Password Requirements:")
      print("Between 8 to 20 characters long.")
      print("Contains at least one uppercase letter.")
      print("Contains at least one lowercase letter.")
      print("Includes at least one number.")
      print("Includes at least one symbol from the set: !@#$%&*")

      password = input("please enter a password that meets the criteria: ")
      length = len(password)

      #checking the length and validating it
      if not (8 <= length <=20):
        print("invalid length")
        valid = False

      is_upper = False
      is_lower = False
      has_number = False
      has_symbol = False

      for char in password:
                if char.isupper():
                    is_upper = True
                elif char.islower():
                    is_lower = True
                elif char.isdigit():
                    has_number = True
                elif char in symbols:
                    has_symbol = True

      if not is_upper:
          print("must include 1 upper case letter")
      if not is_lower:
          print("must include 1 lower case letter")
      if not has_number:
          print("must include 1 number")
      if not has_symbol:
          print("must include 1 symbol")
      if valid:
          confirm = input("please enter password again for ocnfirmation")
          if password != confirm:
              print("password not matched. try again")
              valid = False
    except Exception:
        print("error, try again")
        valid = False

  print("congratulations password set")
      

main()

