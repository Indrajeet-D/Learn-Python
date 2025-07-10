#to inherit a class we write name of class in ()- parenthesis
# class Hello:
#     def __init__(self,age):
#         print("Hello cons")
#         self.age=age
#     def ages(india):        #self can be replaced with any name
#         print(f"age is: {india.age}")

# class Programmers (Hello):      #Programmes inherit Hello class
#     def __init__(self,name,address):

#         super().__init__(55)      #to call constructor of parent or any method
#         self.name=name
#         print("Pro cons")
#         self.address=address

# done = Programmers("Pro","02934")

from typing import Any


class Employees:        
    salary=0        
    lang="Pyth"
    @classmethod
    def fre(cls):
        print(f"hello its fre and class method to print class attribute {cls.salary}")

    @property
    def __setattr__(self, name: str, value: Any):
        pass
    def __getstate__(self):
        pass
e=Employees()
e.salary=20
e.fre()         #will print class attribute
e.name="Hello man"
print(e.name)



#operator overloading


