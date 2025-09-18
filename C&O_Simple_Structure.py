class Dog: 
    def __init__(self, name, breed): 
         
        self.name=name 
        self.breed=breed 

    def bark(self): 
        print("Whoof whoof")

dog1=Dog("Bruce","Scottish") 
dog1.bark() 
print(dog1.name)

dog2=Dog("Wayne","Greyhound")
dog2.bark()
print(dog2.breed)