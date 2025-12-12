'''Write a Python program to find and print all numbers divisible by 7 between 1 and 300. Use a for loop and the modulus operator (%).'''

#for loop, range 1-300
for n in range(1,300):
#remember - the modulo will tell us a remainder. so it is checking for 0 to let us know the dvisbility 
  if n % 7 == 0:
    print(n)