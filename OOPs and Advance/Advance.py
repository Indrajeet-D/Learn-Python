# #Walrus operator(:=)  --to use more functionality at one place
# if(n:=len([1,2,3,42,32]))>3:
#     print(f"this len is {n} use it less than 3")

#to mark type
# n:int=3 #we can mark it as type by variable:type ,make easy to understand what type of variable
# s:str="hello"

# def fun(a:int,b:int)->int:      #-> sign show that it return int
#     return a+b
# fun(2,4)

#to mark as list,tuple,dict we can import it
# from typing import List,Tuple       #from is used to specify module such as : from random import randint
# person=List[int]
# tup=Tuple[int,str]
# print(person)
# print(tup)

#match case--extremly simlilar to switch of other language
# def fool(status):
#     match status:
#         case 200:
#             return "error for 200"
#         case 400:
#             return "error for 400"
#         case 404:
#             return "error for 404"
#         case _:     #default case
#             return "unknown error"
        
# print(fool(200))
# print(fool(400))
# print(fool(404))
# print(fool(2001))

# merging dictionary
# dic1={"plane":"trip",
#       2:"hello",
#       3:"bye"}
# dic2={
#     "yellow":"color",
#     2:"good",
#     "nh":"high"
# }

# merged=dic1 | dic2
# print(merged)

#for opening multiple files
# with(
#     open("file.txt") as f1,
#     open("file2.txt") as f2         #ca be used outside at place of pass
# ):
#     pass