class Dog: # Blueprint for creating objects
# Defines what attributes/data/fields/functions/methods that the objects created from this class will have.  
    def __init__(self, name, breed, owner): 
       
        self.name=name # (self.name)Attributes are the variables that store information about an object (each Dog object)
        self.breed=breed 
        self.owner=owner
# self refers to the instance or the specific object of the class itself i.e. dog1 has different values/data assigning different variable_name but they are both dog objects. 
# self word is used to access the specific object attributes and methods from inside of a class.
# self keyword which allows each dog object to have its own values for name and breed. (Personalized)
    def bark(self): # Methods are functions defined inside a class. | They define what action or behaviour an object can perform. 
        print("Whoof whoof")

class Owner:
    
    def __init__(self,name,address,contact_number): #
        self.name=name #Initialize the attributes name and age for each specific object that we create/instantiate
        self.address=address
        self.phone_number=contact_number


owner1=Owner("Danny","122, Springfield","999-808") #Instatiaing the class (When you create an object from a class) | Here, owner1 (object) is an instance of a class (Owner). 
dog1=Dog("Bruce","Scottish",owner1) # Instance of a class | Created from Class blueprint with its own data.
print(dog1.owner.name)

owner2=Owner("Smith","417, Brooklyn","454-901")
dog2=Dog("Wayne","Greyhound",owner2)
print(dog2.owner.name)

# Dog class --> Dog object