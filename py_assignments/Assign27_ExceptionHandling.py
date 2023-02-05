                        # Exception Handling


# Script to create a ArithmeticError

# a=7
# b=0
# c=a/b
# print(c)


# Script to create a ValueError

# a=7
# b=int(input("Enter a number"))   #when you enter anything which is not int type
# c=a/b
# print(c)


# Script to handle the ArithmaticError

# a=20
# c=0
# try:
#     b=int(input("Enter a number"))
#     c=a/b

# except ZeroDivisionError:
#     print("Zero se division thodi hota h pagal")    
# except Exception :
#     print("Arithmetic Error ka ZeroDivisionError")    
# print(c)


#Script to handle ValueError

# a=20
# c=0
# try:
#     b=int(input("Enter a number"))
#     c=a/b

# except ValueError:
#     print("Dhyan se padha kro instruction")    
# except Exception :
#     print("Kuch toh gadbad hai")    
# print(c)


# Script to handle multiple exceptions in one try
            # Refer to Question Number-4


# Script to create a calculator with basic operations, and handle maximum numbers of exceptions
# a=0
# b=0
# sum = None
# diff = None
# mul = None
# div = None

# try:
#     a = int(input("Enter the first number"))
#     b = int(input("Enter second number"))
#     div = a/b

# except ZeroDivisionError:
#     print("you cannot divide by Zero")
# except ValueError:
#     print("Tumhe number enter krna tha")    
# except Exception:
#     print("Kuch toh gadbad hai")
# else:
#     sum = a + b
#     diff = a - b
#     mul = a * b
#     div = a / b
# finally:
#     print("Mera chalna toh tay hai")    

# print(sum) 
# print(diff) 
# print(mul)
# print(div)  


# Write a python script to add a finally block for the above script
      # previous question me lga diya h finally block


# Write a python script to implement try except and else block for division  

# a=0
# b=0

# try:
#     a = int(input("Enter the first number"))
#     b = int(input("Enter second number"))
#     div = a/b

# except ZeroDivisionError:
#     print("You cannot divide by Zero")
# except ValueError:
#     print("Tumhe number enter krna tha")    
# except Exception:
#     print("Kuch toh gadbad hai")
# else:
#     print(div)


# Script to raise a ValueError

# a=0
# b=0

# try:
#     a = int(input("Enter the first number"))
#     b = int(input("Enter second number"))
#     if type(a)!= int or type(b)!= int:
#         raise ValueError

# except ValueError:
#     print("ye raise keyword se aya hua Exception hai")
# except Exception:
#     print("Kuch toh gadbad hai")  
# else:
#     print(a,b,sep=" ")          


# Script to implement a nested try except block