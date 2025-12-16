'''Task Description:

        Create the Pet Class:
            Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
            Implement get and set methods for each of these attributes.
            Add a method called print_details that prints the details of the pet.
        Create Instances:

        Create three objects of the Pet class with different kinds, breeds, and names.

        Call the print_details method for each object that you created
        Demonstrate a Special Method or Function:

        Choose three of the following and demonstrate its use with the Pet class instances:
            __name__: Display the name of the class.
            type(): Show the class used to instantiate a pet object.
            __module__: Return the module name in which the Pet class is defined.
            __bases__: Display the base classes of the Pet class (if any).
            isinstance(): Check if an instance is of the Pet class.
'''
#creating the pet class 
class Pet:
  #inititalizing and private variables
  def __init__(self,kind,breed, name):
    # the instances 
    self.__kind = kind
    self.__breed = breed
    self.__name = name 

#getter methods and setters,
# TODO: look up later if its good practice to have getters and setters separate
# or  for cleanliness or of its just preference.  
  def get_kind(self):
        return self.__kind
    
  def set_kind(self, kind):
        self.__kind = kind
    
  def get_breed(self):
        return self.__breed
    
  def set_breed(self, breed):
        self.__breed = breed

  def get_name(self):
        return self.__name
    
  def set_name(self, name):
        self.__name = name
#printing method for the details of evertthing

  def print_details(self):
        print(f"Pet type: {self.__kind}")
        print(f"Pet Breed: {self.__breed}")  
        print(f"Pet Name: {self.__name}")

def main():
    #creating pet objects
    pet1 = Pet("Reptile", "Leopard Gecko", "Reptar")
    pet2 = Pet("Dog", "Labrador","Buddy")
    pet3 = Pet("Bird", "Parakeet", "Rose")

       # here are the calls 
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

#the special methods and functions. only 3 req'd
    print("Class name:", Pet.__name__)
    print("type pet: ", type(pet1))
    print("demonstratingg insinstance", isinstance(pet2, Pet))

if __name__ == "__main__":
     main()


