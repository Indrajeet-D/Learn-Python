#try catch becomes try and except Exception
# try:
#     a=int(input("Enter a number"))
#     print(a)
# except ValueError as e:     #ValueError is aa type of Exception
#     print(e)
# except Exception as e:
#     print(e)

#Raising errors

# a=int(input("enter 1 no"))
# b=int(input("enter 2 no"))
# if(b==0):
#     raise ZeroDivisionError("Divide by zero not valid")
#     print("crashed")        #this will not be printed as programe will crash after raising error : user defind message for error 
# else:
#     print(f"divide is {a//b}")


#try - else  statement:  else only run when try is successfully runned means when exception do not occure
# try:
#     a=int(input("Enter a number"))
#     print(a)
# except Exception as e:
#     print(e)
# else:
#     print("in else")

#finally and try--finaly always runs even if function has returned
# def join():
#     try:
#         a=int(input("Enter a number"))
#         print(a)
#         return
#     except Exception as e:
#         print(e)
#         return
#     finally:        #it will run in any condition
#         print("in finally")     #if it is mentioned directly then this will not run, but in this finally it will be runned
    
# join()

#global keyword
# a=12
# def fun():
#     # a=32
#     global a
#     a=32
#     print(a)

# fun()           #will print 32 as it is local variable for fun()
# print(a)        #   1.will print 12 as it is global     2.will print 32 as global var is changed insid fun()


# for getting index and items in list:
# l=[1,2,3,4,5]
# for index , item in enumerate(l):       #first var will have index and second will have items
#     print(f"index is {index}, and item is {item}")

#list comprehension
# squareL=[]
# for i in l:
#     squareL.append(i*i)
# print(squareL)
#can be done as:
# squareL=[i*i for i in l]        #list comprehension
# print(squareL)
# addL=[i+i for i in l]  
# print(addL)

#problems:


