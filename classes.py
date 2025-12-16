'''
        Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
        Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
        Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.
        Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read.
'''

#first class definition for person

class Person:
  #initializers, variables will be private
  def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone_number
  #methods/getters and setters for info on person
  def get_name(self):
        return self.__name
  #gettter for address 
  def get_address(self):
        return self.__address
  #getter for age
  def get_age(self):
        return self.__age
  def set_name(self, name):
        self.__name = name

  def set_address(self, address):
        self.__address = address

  def set_age(self, age):
        self.__age = age

  def set_phone(self, phone):
        self.__phone = phone

  def get_info(self):
      print(f"{self.__name}, {self.__address},{self.__age}, {self.__phone}")


#here is where we make the instances 
person1 = Person("Javier", "123 Random Street","32","234-234-3432")
person2 = Person("Jay", "323 Random Street","32","234-233-3432")
person3 = Person("Jack", "123 Random Street","32","234-334-3332")

person1.get_info()
person2.get_info()
person3.get_info() 
  

  
  