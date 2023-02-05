                               
                               #Iterator, Generator, Decorator


#Use iter method to access all the elemrnts of a given set using while loop

# s1={1,4,8,12,16,24}
# it=iter(s1)
# l=(len(s1))
# while l:
#     print(next(it))
#     l-=1
 

#Create a generator function to produce first N odd natural numbers

# def oddGenerator(num):
#     n=1
#     while num:
#         yield n
#         n+=2
#         num-=1

# for e in oddGenerator(int(input("Enter how many odd numbers you want\n"))):
#     print(e,end=' ')

    
#Create a generator to produce first N even natural numbers

# def evenGenerator(num):
#     n=2
#     while num:
#         yield n
#         n+=2
#         num-=1

# for i in evenGenerator(7):
#     print(i,end=' ')


#Create a generator to produce squares of first N natural numbers

# def squareGenerator(num):
#     n=1
#     while num:
#         yield n
#         n+=1
#         num-=1

# for i in squareGenerator(int(input("ENter how many numbers you want"))):
#     print(i**2,end=' ')       


#Create a generator to produce first N terms of Fibonacci series

# def fibGenerator(num):
#     n1=0
#     n2=1
#     print(n1,n2,end=' ')
#     while num>2:
#         yield n1+n2
#         n1,n2=n2,n1+n2
#         num-=1

# for i in fibGenerator(10):
#     print(i,end=' ')


#Create a generator to produce first N prime numbers

# def primeGenerator(num):
#     i=2
#     n=2
#     count=0
#     while n:
#         while i<n:
#             if n%i==0:
#                 break
#             i+=1

#         if i==n:
#             count+=1
#             yield i

#         if count==num:
#             break
#         n+=1
#         i=2

# for e in primeGenerator(int(input("ENter how many prime numbers you want\n"))):
#     print(e,end=' ')            


#