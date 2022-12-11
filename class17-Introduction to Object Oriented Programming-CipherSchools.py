
student1={
    "name":"Aishant Parashar",
    "Marks":78
}
student2={
    "name":"samraj",
    "Marks":89
}

class Person:
    pass
p=Person() #If we call a class it will create new object of the class
print(p)
print(hex(id(p)))

class Person:
    name="Jatin"
    def say_hi(self):
        print(f"Hello Everyone! I am {self.name}")
p=Person()
p.say_hi() 
Person.say_hi(p)
