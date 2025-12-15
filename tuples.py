'''
    Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
    Write a program that uses a for loop to print each class in the tuple.
    Use the len function to print how many courses are in the tuple.
    Make sure to use a main function for this program.
'''

def main():
#making a tuple called programming classes with the provided classes
  programming_classes = ("Intro to Python", "Advanced Python","Database Essentials", "Web Development Basics", "Data structures in python", "Web design fundementals")
#making a for loop to go through the tuple
  for classes in programming_classes:
    print(classes)
    #was wondering why it was printing it for every line but it was a spacing issue.
    #print(f"there are {len(programming_classes)}")
  print(f"there are {len(programming_classes)} classes total")
main()