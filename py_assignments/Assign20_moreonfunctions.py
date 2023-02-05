                                        #More on functions


#Program to create a function that takes a list and returns a new list with the original list unique elements

# def fxnReturningList(l1):
#     l2=[]
#     j=1
#     l=len(l1)

#     for i in l1:
#         j=1
#         while j<l:                   

            # if i==l1[j]:
            #     break
            # else:                           #WRONG LOGIC 
            #     l2.append(i)
            # print(i)
            # j+=1

    # return l2        

# lst=[1,3,5,7,9,11,1,3,5,7,9,2,4,6,8,10]
# print("New list with unique elements of original list is ",fxnReturningList(lst))


#Program ot create a function that takes a number as a parameter and check if the number is prime or not

# def isPrime(n):
#     i=2
#     while i<n:
#         if n%i==0:
#             break
#         i+=1
#     if i==n:
#         print(n,"is a prime number")
#     else:
#         print(n,"is not a prime number")    
# num=int(input("Enter a number you want to check\n"))
# isPrime(num)


#Program to create a function that prints the even numbers from the given list.
#samplelist=[1,2,3,4,5,6,7,8,9]

# def evenNoInList(s_l):
#     for i in s_l:
#         if i%2==0:
#             print(i,end=' ')
# samplelist=[1,2,3,4,5,6,7,8,9]
# evenNoInList(samplelist)


#Program to create a function that checks wheather a passed string is palindrome or not











#Program to create a function to find the minimum of three numbers

# def minNumber(a,b,c):
#     min=a
#     if min>b:
#         min=b
#     if min>c:
#         min=c

#     print("Minimum among these 3 numbers is",min)

# minNumber(100,201,30)


#Program to create a function and print a list where the values are aquare of numbers between 1 to 30

# def fxnSqNoInList():
#    l = [i**2 for i in range(1,31)]
#    print(l)

# fxnSqNoInList()


#Program to access a function inside a function














#Program to create a function that accepts a string and calculate 
# the number of upper case letters and lower case letters.

# def countUpperLowerCase(s):
#     upper_case=0
#     lower_case=0

#     for i in s:
#         if i.isupper():
#             upper_case+=1
#         elif i.islower():
#             lower_case+=1
#         else:
#             pass        

#     print("Total upper case letters are",upper_case)
#     print("Total lower case letters are",lower_case)            
# strng=str(input("Enter a string in which total number of upper and lower case  letters you want to count"))
# countUpperLowerCase(strng)



