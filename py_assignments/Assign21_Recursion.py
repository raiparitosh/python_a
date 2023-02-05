                                   #  Recursion


#Recursive python function to print first N natural numbers

# def printNntrlno(N):

#     if N>0:
#         printNntrlno(N-1)
#         print(N)

# printNntrlno(10)


#Recursive python function to print first N natural number in reverse order

# def printNntrlnoRev(N):

#     if N>0:
#         print(N)
#         printNntrlnoRev(N-1)

# printNntrlnoRev(5)    


#Recursive function to print first N odd natural number 

# def printOddNtrlNo(N):

#     if N>0:
#         printOddNtrlNo(N-2)
#         print(N)

# n=int(input("Enter how many first odd natural numbers you want\n"))        
# print()
# printOddNtrlNo(n*2-1)


#Recursive function to print first N odd natural number in reverse order

# def printOddNtrlNo(N):

#     if N>0:

#         print(N)
#         printOddNtrlNo(N-2)

# n=int(input("Enter how many first odd natural numbers you want\n"))        
# print()
# printOddNtrlNo(n*2-1)


#Recursive function to print first N even natural number 


# def printEvenNtrlNo(N):

#     if N>0:
#         printEvenNtrlNo(N-2)
#         print(N)

# n=int(input("Enter how many first even natural numbers you want\n"))        
# print()
# printEvenNtrlNo(n*2)



#Recursive function to print first N even natural number in reverse order 


# def printEvenNtrlNo(N):

#     if N>0:
#         print(N)
#         printEvenNtrlNo(N-2)
        
# n=int(input("Enter how many first even natural numbers you want\n"))        
# print()
# printEvenNtrlNo(n*2)


#Recursive function to print squares of first N natural numbers

# def printSquare(N):

#     if N>0:

#         printSquare(N-1)
#         print(N**2)

# printSquare(5)


#Recursive function to print cubes of first N natural numbers

# def printCube(N):

#     if N>0:

#         printCube(N-1)
#         print(N**3,end=' ')

# printCube(10)


#Recursive function to print first N multiples of a given number

# def printMultiples(n,m):
#     if m>0:
    
#         printMultiples(n,m-1)
#         print(n*m)

# printMultiples(7,5)


#Recursive function to print a number in reverse order

# def reverseNumber(N):

#     if N>0:
#         print(N%10,end='')
#         reverseNumber(N//10)

# n=int(input("Enter a number you want to reverse\n"))
# reverseNumber(n)


