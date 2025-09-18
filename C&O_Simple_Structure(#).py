class Dog: # With this, we can create Dog objects. 
    # Inside, we can have:
    # data
    # attributes/data fields
    # functions/methods
    def __init__(self, name, breed): 
        # Method to Set up data fields/attributes
        # Special method in pYthon
        # Runs only once when an object is created/instantiated. 
        self.name=name # Name doesn't have to match like ex. self.name=Firstname, just a convention.
        self.breed=breed # Data Fields

    def bark(self): # self gives access to specific Dog objects name and breed 
        print("Whoof whoof")

    #dog1 and dog2 are "Class Dog objects"
dog1=Dog("Bruce","Scottish") # Instance (an object made from dog class)
dog1.bark() # Accessing methods/functions on objects
print(dog1.name)

dog2=Dog("Wayne","Greyhound")
dog2.bark()
print(dog2.breed)

#Each Dog object displays a unique name and breed based on its attribute and show us...
#...how different instances or objects of same class can hold different data and perform the same behaviour with that data. 