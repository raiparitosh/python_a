                           #Functions in Python

# Python program to create a simple function which prints "MySirG"

# def mereguruji():
#     print("MySirG")

# mereguruji()


#Python program to create a function which expects two arguments and print them in the function body

# def PrintTwoArgument(a,b):
#     print("First Aruument is",a)
#     print("Second Argument is",b)

# PrintTwoArgument(7,77)    


#Program to create a function which expects an unknown number of arguments

# def UnknownNoOfArgument(*u):          #*u is not a pointer. It is a concept of Variable Length Arguments in Python
#     print(type(u),u)

# UnknownNoOfArgument(1,2,3)
# UnknownNoOfArgument(11,22,33,44)


#Program to create a function which expects kwargs argument

# def KwargsArgument(**details):
#     print(type(details),details)

# KwargsArgument(a=1,b=2,c=7)    
# KwargsArgument(name="paritosh rai",age=22,gender="male")    


#Program to create a function which expects a list as an argument

# def ListasanArgument(l):
#     print("The list which is given as an argument to this function is",l)

# l1=[1,2,3,7,77,777]   
# ListasanArgument(l1)


#program to create a function that finds maximum of four numbers

# def MaximumFourNumbers(a,b,c,d):
#     print(a,b,c,d)
#     max=a
#     if max<b:
#         max=b
#     if max<c:
#         max=c
#     if max<d:
#         max=d
#     return max    

# print("Maximum number among these 4 is",MaximumFourNumbers(7777,4000,871,91))   
    

#Program to sum all the numbers in a list

# def SumOfListItems(lst):
#     s=0
#     for i in lst:
#         s=s+i

#     s=sum(lst)

#     print("Sum of given list items is",s)

# l1=[3,5,8,5,2]
# SumOfListItems(l1)    

#Program ot multiply all the numbers in a list

# def ProductOfListItems(l):
#     p=1
#     for i in l:
#         p=p*i
#     print("Product of elements of the given list is",p)    

# list=[2,3,4,5]
# ProductOfListItems(list)


#Program to create a function to check wheather a number falls in a given range

# def CheckInRange(num,start,end):
#     if start<end:

#         if start<=num<=end:
#             print("Present")
#         else:
#             print("Not Present")
#     else:
#         print("You entered incorrect range")            

# n=int(input("Enter the number you want to check"))
# print("Enter the range in which you want to check")
# s_range=int(input("Eter starting point of range"))
# e_range=int(input("Enter end of the range"))
# CheckInRange(n,s_range,e_range)


#Program ot create a function to check wheathera given number is even or odd

# def IsEvenOdd(n):
#     if n%2==0:
#         print(n,"is an even number")
#     else:
#         print(n,"is a odd number")    
    
# num=int(input("Enter a number"))
# IsEvenOdd(num)
