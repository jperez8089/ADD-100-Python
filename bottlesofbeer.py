'''Was not sure what bottles of beer on the wall was so i had to look it up. It turns out its a song LOL. 

Although technically in the timeline of the course the concept of lists have not been touched, I relied heavily on a book called
"The python crash course" and they touched the concept of list in conjunction with loops, so I will use it here.

'''

#determining a count variable 
count = list(range(99, 0, -1))

while count: #pop method from pg 39 of py.crash course
  bottle = count.pop(0)

#getting the right word for the amount
# TODO: Already deep into the if else statement, i overcomplicated it but Im sticking with it. Could have slimmed this down 
  
  if bottle == 1:
    right_word = "bottle"
  else:
    right_word = "bottles"

#next line
  future_count = bottle - 1

  if future_count == 1:
    future_bottle_words = "bottle"
  else:
    future_bottle_words = "bottles"

  print(f"{bottle}{right_word} of beer on the wall, {bottle} {right_word}")
  print("Take one down and pass it around,", future_bottle_words)


  