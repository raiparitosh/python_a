                                #for and range


#Script to print first 10 multiples of 5

# r=range(5,51,5)
# for i in r:
#     print(i,end=' ')


#Script to print first 10 multiples of N

# n=int(input("Enter the no. whose multiple you want"))
# r=range(n,n*10+1,n)
# for i in r:
#     print(i,end=' ')


#Script to print first M multiples of N

# n=int(input("Enter the no. whose multiple you want"))
# m=int(input("Enter the multiples you want"))
# r=range(n,n*m+1,n)
# for i in r:
#     print(i,end=' ')


#Script to print first 10 multiples of N in reverse order

# n=int(input("Enter the no. whose multiple you want"))
# r=range(n*10,0,-n)
# for i in r:
#     print(i,end=' ')


#Script to print table of user choice

# n=int(input("Enter the no. whose table you want to print"))
# r=range(n,n*10+1,n)
# for i in r:
#     print(i,end=' ')


#Script to print N even natural numbers

# n=int(input("Enter how many even numbers you want to print "))
# r=range(2,2*n+1,2)
# for i in r:
#     print(i,end=' ')


#Script to print first N odd natural numbers

# n=int(input("Enter how many odd numbers you want to print "))
# r=range(1,2*n,2)
# for i in r:
#     print(i,end=' ')


#Script to print squares of first N natural numbers

# n=int(input("Enter the number upto you want"))
# r=range(1,n+1)
# for i in r:
#     print((i)**2,end=' ')
                        #Method-2
# for i in range(int(input("Enter the number upto you want"))):
#     print((i+1)**2,end=' ')                        


#Script to print cubes of first N natural numbers

# n=int(input("Enter the number upto you want"))
# r=range(1,n+1)
# for i in r:
#     print(i*i*i,end=' ')


#Script to display all prime numbers in a range. range-start=15,end=45

                                #  M1
# for n in range(15,46):
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         print(n,end = " ") 
                                #  M2
# r=range(15,45)
# for i in r:
#     a=2
#     while a<i:
#         if i%a==0:
#             break
#         a+=1
#         if a==i-1:
#             print(i,end=' ')



s=input("Enter a string\n")
for i in s:
    if i=='r':
        break
    print(i)
else:
    print("All the characters are successfully processed\n")        