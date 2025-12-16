class Pet:
    #var for the vetpet class
    veterinary_office = "MCC Animal Clinic"

    # the usual initializing with private variables
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    #getters and setters 
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    def get_pet_id(self):
        return self.__pet_id
    
    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id
        
    def get_pet_name(self):
        return self.__pet_name
    
    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def get_pet_type(self):
        return self.__pet_type
    
    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # making th emethod to print the owner and pet informatioj
    def print_pet_details(self):
        print("Pet name: " + self.__pet_name)
        print("owner name: " + self.__owner_first_name + " " + self.__owner_last_name)
        print("pet id: " + self.__pet_id)
        print("pet type: " + self.__pet_type)
        print("Vet office: " + Pet.veterinary_office)

# here we create pet objects
def create_pet_info():
    pet1 = Pet("robert", "mills", "ID34343", "rocky")
    pet2 = Pet("mark", "dniels", "ID43532", "buddy")
    pet3 = Pet("celine", "smith", "ID234222", "anubis")
    return pet1, pet2, pet3

#this is where we mess with propertiesand existence checking
def check_property(obj, prop):
    if hasattr(obj, prop):
        print(f"Yes! This pet object has the property '{prop}'")
    else:
        print(f"No, this pet object does NOT have the property '{prop}'")
def main():
    # Create pets
    pet1, pet2, pet3 = create_pet_info()

    # Display pet details
    pet1.print_pet_details()
    pet2.print_pet_details()
    pet3.print_pet_details()

    #checking properties
    check_property(pet1, "_Pet__pet_type")
    check_property(pet2, "_Pet__pet_id")
    check_property(pet3, "_Pet__pet_name")
    check_property(pet3, "_Pet__pet_meds")  

if __name__ == "__main__":
    main()
