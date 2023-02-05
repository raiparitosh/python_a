                      # more on Recursion in python

#Recursive function to calcuate sum of first N natural number

# def sumNtrlNo(N):

#     if N==1:
#         return 1
#     else:    
#         return N + sumNtrlNo(N-1)

# print("sum of first 5 natural number is",sumNtrlNo(5))    


#Recursive function to calculate sum of first N odd natural numbers

# def oddSum(N):
#     if N==1:
#         return 1
#     else:
#         return N + oddSum(N-2)

# n=int(input("Enter how many odd natural numbers sum you want "))
# print("Sum is",oddSum(n*2-1))


#Recursive function to calculate sum of first N even natural numbers

# def evenSum(N):
#     if N==2:
#         return 2
#     else:
#         return N + evenSum(N-2)

# n=int(input("Enter how many even natural numbers sum you want "))
# print("Sum is",evenSum(n*2))


# Recursive fxn to calculate sum of squares of first N natural numbers

# def squareSum(N):
#     if N==1:
#         return 1
#     else:
#         return N*N + squareSum(N-1)

# n=int(input("Enter how many square numbers sum you want"))
# print("Sum is",squareSum(n))  


# Recursive fxn to calculate sum of cubes of first N natural number

# def cubesSum(N):
#     if N==1:
#         return 1
#     else:
#         return N*N*N + cubesSum(N-1)

# n=int(input("Enter how many cubes numbes sum you want"))
# print("Sum is ",cubesSum(n))


# Recursive fxn to calculate factorial of number

# def fact(N):
#     if N==1:
#         return 1
#     else:
#         return N * fact(N-1)

# n=int(input("Enter the number whose factorial you want"))
# print("Factorial is ",fact(n))


# Recursive fxn to calculate sum of digits of a given number

# def digitSum(N):

#     if N==0:
#         return 0
#     else:
#         return N%10+digitSum(N//10)
        
# n=int(input("Enter the number"))
# print("Sum of digits is",digitSum(n))


# Recursive fxn to find the nth term of the Fibonacci Series

n=int(input("Enter the term you want"))

def fib(n):
    n1=0
    n2=1
                         #not recursive fxn
    if n==1:
        return 0
    elif n==2: 
        return 1
    else:
        while n>2:
           n3 = n1 + n2
           n1 , n2 =n2 , n3
           n-=1
        return n3      

print(fib(n))