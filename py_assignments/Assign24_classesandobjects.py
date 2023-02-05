                                        # Classes and Objects

#Write a program to create a user class with 3 properties : name, age , email

# class user:
    
#     def __init__(self):
#         self.name = "parth"
#         self.age = 22
#         self.email = xy@gmail.com

# user1 = user()
# print(type(user1))


#Write a program to crete a user class with a method to greet the user

# class user:

#     def greet_method():
#         print("hii there you are studying oop in python")

# user.greet_method()


#Write a python program to create 2 objects of the user class and assign different values

# class user:
#     pass

# user1 = user()
# user1.name = "paritosh"
# user2 = user()
# user2.name = "toshu"

# print(user1.name)
# print(user2.name)


#Write a program to init default values for user object using __init__ method.

# class user:

#     def __init__(self):
#         self.name = "pta nhi"
#         self.age = 23
#         self.email = "kya bola h question me" 

# user1 = user()


#Write a program to delete the age property of the user

# class user:
#     name = "pr"
#     age = 22
#     email = "prtsh"

# user1 = user()    
# del user.age
# print(user.age)


#Write a program to create 3 user objects and find youngest of all.

# class user:
    
#     def __init__(self,age):

#             self.age = age
        
# user1 = user(26)
# user2 = user(21)
# user3 = user(22)

# if user1.age < user2.age and user1.age < user3.age:
#     print("User1 is Youngest")

# elif(user2.age < user1.age and user2.age < user3.age):
#     print("User2 is Youngest") 

# elif(user3.age < user1.age and user3.age < user2.age):
#     print("User3 is Youngest")


#Write a program to  create a laptop class with 4 attributes(brand,ram,cpu,hdd) and 
# 2 methods (showconfig() to print the values,__init__() to initialize the values.)  


# class laptop:

#     def __init__(self,brand,ram,cpu,hdd):
#         self.brand = brand
#         self.ram = ram
#         self.cpu = cpu
#         self.hdd = hdd

#     def showConfig(self):
#         print(self.brand,self.ram,self.cpu,self.hdd)

# l1 = laptop("Asus",16,"i7",1)
# l1.showConfig()

# l2 = laptop("HP",4,"i3",1)
# l3 = laptop("Dell",8,"i5",512)

# l_list = [l1.ram,l2.ram,l3.ram]
# l_list.sort()
# print(l_list)


#Write a program to create a School class and 3 instance variables and 1 class variable.

# class school:
#     name="ALLEN"

#     def __init__(self,principal,classes,teachers):
#         self.principal = principal
#         self.classes = classes
#         self.teachers = teachers 

# a1 = school("raisahab","10 A","lnfParitoshRai")       
# print(a1.principal,a1.classes,a1.teachers)
# print(school.name)


#Define a class Employee with instance variables:- empid,name,salary. Write __init__() method in the class 
# to iitialize instance object variables. Also define instance methods to input fields and display values.
 

class employee:

    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def show_emp_details(self):
        return self.empid,self.name,self.salary

emp1 = employee("ITT07077","Paritosh Rai",4.5)
print(emp1.show_emp_details())


