def main():
#creating a dictonary for the nato 
  nato_dict = { "A": "Alpha", "B": "Bravo", "C": "Charlie",
        "D": "Delta", "E": "Echo", "F": "Foxtrot",
        "G": "Golf", "H": "Hotel", "I": "India", 
        "J": "Juliette", "K": "Kilo", "L": "Lima", 
        "M": "Mike", "N": "November", "O": "Oscar",
        "P": "Papa", "Q": "Quebec", "R": "Romeo", 
        "S": "Sierra", "T": "Tango", "U": "Uniform",
        "V": "Victor", "W": "Whiskey", "X": "X-Ray", 
        "Y": "Yankee", "Z": "Zulu"
}

#makign the spelling portion
  user_word = input("Enter a word for the nato converter: ")
  for letter in user_word.upper():  
      if letter in nato_dict:
          print(nato_dict[letter])
      else:
          print(letter)  


main()
  