                                         #Match Case Problem                                                                    

# Script to display the number of days in a given month number

# m=int(input("Enter month number"))
# match m:
#     case m if m in (1,3,5,7,8,10,12):
#         print("31 Days")
#     case m if m in (4,6,9,11):
#         print("30 Days") 
#     case 2:
#         print("28 or 29 Days")
#     case _:
#         print("Enter correct month number")           
                                #    Method 2
# m=int(input("Enter month number"))
# match m:
#     case 1:
#         print("31")
#     case 2:
#         print("29")
#     case 3:
#         print("31")
#     case 4:
#         print("30")
#     case 5:
#         print("31")
#     case 6:
#         print("30")
#     case 7:
#         print("31")
#     case 8:
#         print("31")
#     case 9:
#         print("30")
#     case 10:
#         print("31")
#     case 11:
#         print("30")
#     case 12:
#         print("31")    
#     case _:
#         print("Enter correct month value")                                            


#Script to display the days of a week in a given week number

# d=int(input("Enter day number"))
# match d:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday") 
#     case 3:
#         print("Wednesday")       
#     case 4:
#         print("Thursday") 
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday") 
#     case 7:
#         print("Sunday")
#     case _:
#         print("Enter right choice")                   


#Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

# a=int(input("Enter first number"))
# b=int(input("Enter second number"))
# o=input("Enter the operation you want to perform")
# match o:
#     case "+":
#         print(a+b)
#     case "-":
#         print(a-b)    
#     case "*":
#         print(a*b) 
#     case "//":
#         print(a//b)
#     case _:
#         print("Choose correct operation")           


#Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit




























































#WAP which takes age and display the category of a person.below-10-kid,below 20-teen
#    below 40-young,below 60-experienced,above or equal to 60-senior citizen

# a=int(input("Enter the age"))
# match a:
#     case a if a<10: 
#         print("Kid")
#     case a if a<20:
#         print("Teen")
#     case a if a<40:
#         print("Young") 
#     case a if a<60:
#         print("Experienced")
#     case a if a>=60:
#         print("Senior Citizen")           
#     case _:
#         print("Choose Correct Age")        


#Program which takes a number from user. print saurabh shukla if the number is even, print prateek jain
# if number is negative odd number and print aditya chaudhary if number is positive odd number   

# n=int(input("Enter a number"))
# match n:
#     case n if n>0 and n%2==0:
#         print("Saurabh Shukla")
#     case n if n<0 and n%2!=0:
#         print("Prateek Jain")
#     case n if n>0 and n%2!=0:
#         print("Aditya Chaudhary")
#     case _:
#         print("Enter correct number")    


#Script to check that string is a single word string or multi-word string

# s=input("Enter a string")
# match s:
#     case s if ' ' in s:
#         print("Multiword string")
#     case s if ' ' not in s:
#         print("Single word string")   


#WAP to check wheather a given number is positive, negative or zero using match case statement

# n=int(input("Enter a number"))
# match n:
#     case n if n>0:
#         print("Positive Number")
#     case n if n<0:
#         print("Negative Number")
#     # case n if n==0:
#     case 0:
#         print("Zero")        


#Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement

# s1=input("Enter first string")
# s2=input("Enter second string")
# match (s1,s2):
#     case (s1,s2) if s1==s2:
#         print("Identical strings")
#     case (s1,s2) if s1>s2:
#         print("{} comes after {}".format(s1,s2))
#     case (s1,s2) if s2>s1:
#         print("{} comes after {}".format(s2,s1))        

# Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year

# y=int(input("Enter year"))
# match y:
#     case y if y%100==0 and y%400==0 and y%4==0:
#         print("Centuary leap year")
#     case y if y%100==0 and y%400!=0:
#         print("Centuary non leap year")    
#     case y if y%100!=0 and y%4==0:
#         print("Non Centuary Leap Year")    
#     case y if y%100!=0 and y%4!=0:
#         print("Non centuary non leap year")            


# WAP to display day name on the basis of user liking of a colour. Ask user for his favourite colour. User
# can answer in a sentense like "i like red colour". Assuming all colour name entered by user is in 
# lowercase. Use match case to display day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black -  Friday
# f. Red - Saturday
# g. All other Colours - Sunday

# s=input("Enter your favourite colour")
# l1=["yellow","blue","orange","white","red","black"]
# for colour in l1:
#     if colour in s:
#         c=colour
#         break
# else:
#     c="other"

# match c:
#     case "yellow":
#         print("Monday") 
#     case "blue":
#         print("Tuesday") 
#     case "orange":
#         print("Wednesday") 
#     case "white":
#         print("Thursday")
#     case "black":
#         print("Friday") 
#     case "red":
#         print("Saturday") 
#     case "other":
#         print("Sunday")                           