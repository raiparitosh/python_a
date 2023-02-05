                      # Polymorphism and Multithreading


# Script to multiply 2 or 3 or 4 numbers with a single multiply method in a class using method overloading

# class multiplyMethod():

#     def multiply(self,n1,n2=None,n3=None,n4=None):
#         if n4!=None:
#             return n1*n2*n3*n4
#         elif n3!=None:
#             return n1*n2*n3
#         elif n2!=None:
#             return n1*n2
#         else:
#             return "Enter atleast two numbers to perform multiplication"       

# m1 = multiplyMethod()
# print(m1.multiply(2,2,3,4))


# Script to create a user account class with 2 instance variables(userid and balance).
#  Create 3 user objects and add all the users using operator overloading

class UserAccount:

    def __init__(self,userid,balance):
        self.userid = userid
        self.balance = balance

    # def __add__(self,other):
    #     total_userid = self.userid + other.userid 
    #     total_balance = self.balance + other.balance 
    #     u4 = UserAccount(total_userid,total_balance)
    #     return u4    

    def __add__(self,other,third):
        total_userid = self.userid + other.userid + third.userid
        total_balance = self.balance + other.balance + third.balance
        u4 = UserAccount(total_userid,total_balance)
        return u4 

    def __str__(self):
        return str(self.userid) + " " + str(self.balance)   

u1 = UserAccount(11,100000)
u2 = UserAccount(12,150000)
u3 = UserAccount(13,30000000) 

# u4 = u1 + u2 + u3

u4 = UserAccount.__add__(u1,u2,u3)
# u4 = u1.__add__(u2,u3)

# print(u4.userid,u4.balance)

print(u4)    

# Question 3 is implemented in second Question 