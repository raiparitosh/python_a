                          # More Problems on loops

#Script to reverse a number

# n=int(input("Enter the number you want to reverse\n"))
# rev_num=0
# rem=0
# while n!=0:
#     rem=n%10
#     rev_num=rev_num*10+rem
#     n=n//10
# print("Reverse is ",rev_num)                              


#Script to check wheather a given number is prime or not

                    #    M1

# n = int(input("Enter a number"))
# for i in range(2,n):
#     if n % i == 0:
#         print(n," is not a prime number")
#         break
# else:
#     print(n," is a prime number") 

                        #  M2

# n=int(input("Enter a number"))
# i=2
# while i<n:
#     if n%i==0:
#         break
#     i+=1
# if i==n:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")    


#Script to print all Prime numbers under 100
 
                #  M1

# for n in range(2,100):
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         print(n,end = " ") 

                    # M2
# n=2
# i=2
# while n<100:
#     while i<n:
#         if n%i==0:
#             break
#         i+=1
#     if i==n:
#         print(i,end=' ')
#     n+=1 
#     i=2       


#Script to print all prime numbers between two given numbers(both no. inclusive)

                        #   M1
# lb = int(input("Enter lower bound"))
# ub = int(input("ENter upper bound"))
# for n in range(lb,ub+1):
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         print(n,end = " ")

                        #   M2
# lb=int(input("Enter the lower bound"))
# ub=int(input("Enter upper bound"))
# i=2
# while lb<=ub:
#     while i<lb:
#         if lb%i==0:
#             break
#         i+=1
#     if i==lb:
#         print(i,end=' ')
#     lb+=1 
#     i=2       


#Script to find next prime number of a given number

# num = int(input("Enter the number whose next prime number you want"))+1
# i = 0
# count = 0
# while num:
#     for i in range(2,num):
#         if num % i == 0:
#             break
#     else:
#         print(num,end = " ")
#         count += 1
    
#     if count == 1:
#         break
#     num += 1     

#Script to print first N prime numbers

                    # M1
# n =int(input("Enter how many prime numbers you want"))
# count = 0   
# num = 2
# while num:
#     i =2
#     while i<num:
#         if num % i == 0:
#             break
#         i += 1
#     else:
#         print(num,end = " ")
#         count +=1    
#     if count == n:
#         break
#     num += 1

                    # M2
# n=int(input("Enter how  many prime numbers you want to print"))
# count=0
# i=2
# num=2
# while num:
#     i=2
#     while i<num:
#         if num%i==0:
#             break
#         i+=1
#     if i==num:
#         count+=1
#         print(num,end=' ')
#     if count==n:
#         break
#     num+=1
   


#Script to print first N terms of a Fibonacci series

n = int(input("Enter how many terms you want to print"))
n1 = 0
n2 = 1
print(n1,n2,end=' ')
i = 3
while i != n+1:
# while i <= n:
    n3 = n1 + n2
    print(n3,end=' ')
    n1 = n2
    n2 = n3
    i += 1
  




#Script to find the value according to the numbers entered and  
# type of operation on entered numbers

# sum=0
# while True:
#     n=eval(input("Enter number"))
#     o=input("Enter operation")
#     if o=='=':
#         break
#     else:
#         sum=sum+n
# print(sum)    