class Student:
    def __init__(self,name,age): #constructor
        self.name = name
        self.age = age
    def get(self):
        print(f"{self.name}:{self.age}")
s1 = Student("Sanjey",21) #initializing object while creating
s1.get()
s2 = Student("Cibin",22)
s2.get()