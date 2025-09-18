class Dog: 
    
    def __init__(self, name, breed, owner): 
       
        self.name=name 
        self.breed=breed 
        self.owner=owner

    def bark(self): 
        print("Whoof whoof")

class Owner:
    
    def __init__(self,name,address,contact_number):
        self.name=name
        self.address=address
        self.phone_number=contact_number


owner1=Owner("Danny","122, Springfield","999-808")
dog1=Dog("Bruce","Scottish",owner1) # Passing owner to dog
print(dog1.owner.name)

owner2=Owner("Smith","417, Brooklyn","454-901")
dog2=Dog("Wayne","Greyhound",owner2)
print(dog2.owner.name)