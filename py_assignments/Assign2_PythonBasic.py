                           # Python Basics

#Write a python script to add comments and print “Learning Python” on screen                             

# print('"learning python"')   #adding comments


# Write a python script to add multi line comments and print values of 
# four variables each in a new line. Variable contains any values.

"""We are adding
  multi-line coments"""

# p=20     
# q=25
# r=30
# s=35
# print(p,q,r,s,sep="\n")


# Write a python script to print types of variables. Create 5 variables each of them
# containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

# a=35                         #int class
# b=True                       #bool class
# c=5.46                       #float class 
# d='paritosh rai'             #str class 
# e=3+4j

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))


# Write a python script to print the id of two variables containing the same integer values.

# p=20            #id pf both p and q remains same as both
# q=20            #are reffering to the same object             
# print(id(p))           
# print(id(q))


# Create four variables in a Python script and assign values of different data types to
# them. Write a Python script to print value, its type and id of each variable

# a=35                       
# b=True                     
# c=5.46                       
# d='paritosh rai'  
# # f=25

# print(a,type(a),id(a),sep=" - ")
# print(b,type(b),id(b),sep=" - ")
# print(c,type(c),id(c),sep=" - ")
# print(d,type(d),id(d),sep=" - ")


# Script to print all the Keywords

# import keyword
# print(keyword.kwlist)

#Script to print current date and time

# d=12
# m=11
# y=2022
# t='9:55 AM'
# print(d,m,y,sep='-',end='and')
# print(t)

# from datetime import datetime
# dt=datetime.today()
# print(dt)