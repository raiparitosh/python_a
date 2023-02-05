                                 #Decision Control Problem
                         
#Script to check wheather a given number is positive on non-positive

# n=int(input("Enter a number you want to check"))
# if n>0 :
#     print("%d is a positive number"%n)
# else :
#     print("%d is non-positive number"%n)   


#Script to check wheather a given number is divisible by 5 or not

# n=int(input("Enter the number you want to check"))
# if n%5==0 :
#     print("%d is divisible by 5"%n)
# else :
#     print("%d is not divisible by 5"%n)    


#Script to check wheather a given number is even or odd

# n=int(input("Enter a number"))
# if n%2==0 :
#     print("%d is a even number"%n)
# else :
#     print("%d is an odd number"%n)    


#Script to print greater between two number. Print number only once even if numbers are same

# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# if n1>=n2 :
#     print("%d is greater "%n1)
# else :
#     print("%d is greater "%n2)    


#Script to print two given words in dictionary order

# w1=input("Enter first word")
# w2=input("Enter second word")
# if w1>w2 :
#     print(w2,w1)
# else :
#     print(w1,w2)    


#Script to check wheather a given number is a three digit number or not

# n=int(input("Enter the number you want to check"))
# if 99<n<1000:
#     print("three digit number")
# else:
#     print("not a three digit number")  
            #  Method 2
# n=int(input("Enter the number you want to check"))              
# t=n
# count=0
# n=n//10
# count=count+1
# if n!=0 :
#     n=n//10
#     count=count+1
#     if n!=0 :
#         n=n//10
#         count=count+1
#         if n==0 :
#             print("%d is a 3 digit number phla"%t)
#         if n!=0 :
#             n=n//10
#             count=count+1
#             print("%d is not a 3 digit number"%t)   
#     else :
#         print("%d is not a 3 digit number galat 2"%t)        
# else :
#     print("%d is not a 3 digit number galat 3"%t)   


# Sript to check wheather a number is positive, negative or zero
        
# n=int(input("Enter a number(only integer type)"))
# if n>0 :
#     print("positive number")
# elif n<0 :
#     print("Negative number")
# else :
#     print("Zero")  


#Script to check wheather a given quadratic equation has two real & distinct 
# roots, real & equal roots or imaginary roots

# print("Enter values of a quadratic equation")
# b,a,c=int(input("Enter the value of b")),int(input("Enter the value of a")),int(input("Enter the value of c"))
# d=b*b-4*a*c
# if d>0:
#     print("Real and Distinct roots")
# elif d==0:
#     print("Real and Equal roots")
# else:
#     print("Imaginary roots")    


#Script to check wheather a given year is a leap year or not

# y=int(input("Enter a year"))
# if y%100==0 :
#     if y%400==0 :
#         print("%d is a leap year"%y)
#     else :
#         print("%d is not a leap year"%y) 
# else :
#     if y%4==0 :
#         print("%d is a leap year"%y)
#     else :
#         print("%d is not a leap year")               


#Script to print greater among 3 numbers. print number only once even if numbers are same

# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# n3=int(input("Enter third number"))
# if n1>n2 and n1>n3 :
#     print("%d is greater"%n1)
# if n2>n1 and n2>n3 :
#     print("%d is greater"%n2) 
# if n3>n1 and n3>n2 :
#     print("%d is greater"%n3)       


#Script to take the month value in numeric format and display the number of days in it
 
# m=int(input("Enter the month value in numeric format"))
# if m==1 :
#     print("31")
# elif m==2 :
#     print("28")    
# elif m==3 :
#     print("31")
# elif m==4 :
#     print("30")
# elif m==5 :
#     print("31")
# elif m==6:
#     print("30") 
# elif m==7:
#     print("31") 
# elif m==8:
#     print("31")
# elif m==9:
#     print("30")
# elif m==10:
#     print("31")
# elif m==11:
#     print("30")
# elif m==12:
#     print("31")
# else:
#     print("Incorrect month number")   

            #    Second Method using in operator
# m=int(input("Enter the month number in numeric format "))
# if m in (1,3,5,7,8,10,12):
#     print("31 Days")
# elif m in (4,6,9,11):
#     print("30 Days")
# elif m==2:
#     print("28 or 29 Days")
# else:
#     print("You entered incorrect value of month number")                       


#Script to accept one complex number from the user and display the greater number b/w real and imaginary part

# n=complex(input("Enter a complex number"))
# r_p=n.real
# i_p=n.imag
# if r_p>i_p:
#     print(r_p)
# else:
#     print(i_p)    