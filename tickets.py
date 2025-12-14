'''Assignment Steps:

    Create a list representing 20 seats, numbered 1 to 20.
    Display the list of available seats to the customer.
    Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
    Remove the selected seat from the list of available seats and display the updated list.
    If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
    Ensure the program gracefully handles all scenarios and is user-friendly.
'''

# TODO: try and incorporate functions here for practice in future 

#making a list of seats for 1-20
seats = list(range(1, 21))

#displayin the available seats
print("availble seats: ", seats)

seat = -1
while seat != 0:
  seat = int(input("please enter the seat you want to purchase. tap 0 to exit"))
  if seat == 0:
    print("program ended")
    break
  # seat avaiability, using in keyword to check if its there. 
  if seat in seats:
    #removing seat
    seats.remove(seat)
    print("seat:", seat, "thank you. its available and purchase successful") 
  else:
    print("unavailable. try again")

  #list of seats
  print("seats left: ", seats)

  if len(seats) == 0:
    print("all seats sold")
    break