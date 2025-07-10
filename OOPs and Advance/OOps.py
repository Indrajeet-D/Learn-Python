# class Employees:        #class decleration
#     salary=0        #class atribute
#     lang="Python"

#     def __init__(self,name,salary,language):
#         self.name=name
#         self.salary=salary
#         self.lang=language

    
#     def get_info(self):
#         print(f"salary is {self.salary} and language is {self.lang} ,{self.name}")
   
#     @staticmethod
#     def greet():        #to not to pass self -make it static
#         print("hello")

# Indrajeet = Employees("Ind",25000000,"Java")     #object making
# # Indrajeet.name="Ind"        #object attributes
# # Indrajeet.salary=3000000        #object attribute have high priority over class attributes
# print(Indrajeet.name ,Indrajeet.salary , Indrajeet.lang)
# # Indrajeet.get_info()        #get converted to Employees.get_info(Indrajeet)  - for this we use "self" lagbhag same as this keyword of java
# # Indrajeet.greet()

#Problems
# class Programmers:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address

# JK=Programmers("JK",24,"Delhi")
# PK=Programmers("PK",35,"Mumbai")
# print(JK.name,JK.address,JK.age)
# print(PK.name,PK.address,PK.age)

# class Calculator:
#     @staticmethod
#     def Square(x):
#         print(x**2)
#     @staticmethod
#     def Cube(x):
#         print(x**3)
#     @staticmethod
#     def Square_root(x):
#         print(x** 0.5)

# Calculator.Square(25)
# Calculator.Cube(2)
# Calculator.Square_root(225)

# class Train:
#     def __init__(self,seats,fair):
        
#         self.seats=seats
#         self.fair=fair
#     def get_status(self):
#         print(f"Number of seats: {self.seats}")
#     def book_ticket():
#         print("yoyr ticket is booked")
#     def fairs(self):
#         print(f"fair is :{self.fair}")
        
# Shree=Train(200,340)
# Shree.get_status()

class Hello:
    def __init__(self,age):
        self.age=age
    def ages(india):        #self can be replaced with any name
        print(f"age is: {india.age}")

dav=Hello(23)
dav.ages()