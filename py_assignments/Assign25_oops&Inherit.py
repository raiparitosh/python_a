
                           # OOPS and Inheritance 

#Write a python script to create a Profile class with 3 attributes(name, email, age)

# class profile:
     
#      def __init__(self):
#         self.name = "toshiu"
#         self.age = 22
#         self.email = "rai@gmail.com"

#         print(self.name,self.age,self.email)    

# p1 = profile()

# p1.name = "toshu"
# p1.age = 22
# p1.email = "rai@gmail.com"
# print(p1.name)
# print(p1.age)
# print(p1.email)


#Script to update the above profile class with encapsulation

# class profile:
   
#     def __init__(self):
#         self.name = "toshu"
#         self.age = 22
#         self.email = "rai@gmail.com"

#     def get_name(self):
#         return self.name  

#     def set_name(self,name):
#         self.name = name    

#     def get_age(self):
#         return self.age 

#     def set_age(self,age):
#         self.age = age 

#     def get_email(self):
#         return self.email 

#     def set_email(self,email):
#         self.email = email                 

# p1 = profile() 
# print(p1.get_name())
# print(p1.get_age())
# print(p1.get_email())

# p1.set_name("toshurai")
# p1.set_age(50)
# p1.set_email("t@gmail")

# print(p1.get_name())
# print(p1.get_age())
# print(p1.get_email())


#Script to update 2nd question, change email to __email and age to __age.
       #(double underscore -- __ before a variable name is used to hide that variable )

# class profile:
   
#     def __init__(self):
#         self.name = "toshu"
#         self.__age = 22
#         self.__email = "rai@gmail.com"

#     def get_age(self):
#         return self.__age 

#     def set_age(self,age):
#         self.__age = age 

# p1 = profile()

# print(p1.name)
# print(p1.__age)  
# print(p1.age)    
# print(p1.__email)  


#Script to update 2nd question, add a class variable(platform) and create a class method to access it

# class profile:

#     platform = "iNeuron"

#     def __init__(self,name,age,email):
#         self.name = name
#         self.age = age
#         self.email = email

#         print(self.name,self.age,self.email)

#     @classmethod
#     def get_platform(cls):
#         return cls.platform    

# p1 = profile("skr",29,"s@gmail.com")    

# print(profile.get_platform())


#Script to create a calculator class with 2 methods 
# for adding and subtracting

class calculator:

    @staticmethod
    def addition(x,y):
        return x+y
    
    @staticmethod
    def subtraction(x,y):
        return x-y    

c1 = calculator()

# print(calculator.add(5,6))
# print(c1.subtract(8,1))    


# Script to Create a calculator 2.0 class with 2 methods for multiplication and 
# division of 2 values and inherit it from the calculator class.

class calculator2(calculator):

    @staticmethod
    def multiplication(x,y):
        return x*y
    @staticmethod
    def division(x,y):
        return x/y

c2 = calculator2()

# print(c2.addition(3,5))
# print(c2.subtraction(3,5))
# print(c2.multiplication(3,7))
# print(c2.division(30,5))

#Script to create a phone class with 2 methods to print
# the features(caling and sms)

class phone:

    def calling(self):
        print("Calling")

    def sms(self):
        print("sms")

p1 = phone()

# p1.calling()
# p1.sms()     


# Script to create a smartphone class by inheriting 
# calculator2and phone class

class smartphone(calculator2,phone):
    pass

s1 = smartphone()

print(s1.addition(3,4))
s1.calling()
print(s1.multiplication(4,3))