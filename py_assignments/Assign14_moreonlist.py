                 #More on list

#Script to create a list of first N natural numbers

# n=int(input("Enter upto which natural number you want the list"))
# # [expression for variable in iterable] - this syntax creates a list
# print(n)
# l1=[x for x in range(n+1)]           
# print(l1)


#Script to create a list of first N odd natural numbers

# n=int(input("Enter how many odd natural number you want\n"))
# l2=[x for x in range(1,n*2,2)]
# print(l2)


#Script to create a list of first N even natural numbers

# n=int(input("Enter how many even natural number you want\n"))
# l3=[x for x in range(2,n*2+1,2)]
# print(l3)


#Script to find greatest number in a given list of numbers

# n=int(input("Enter how many elements you want in the list"))
# l4=[]
# i=0
# print("Enter %d elements"%n)
# while i<n:
#     l4.append(int(input()))
#     i+=1
# print("Greatest number in the list is",max(l4))


#Script to find smallest number in a given list of numbers

# n=int(input("Enter how many elements you want in the list"))
# l5=[]
# i=0
# print("Enter %d elements"%n)
# while i<n:
#     l5.append(int(input()))
#     i+=1
# print("Smallest number in the list is",min(l5))


#Script to calculate the sum of elements in a given list of numbers

# n=int(input("Enter how many numbers you want in the list"))
# l6=[]
# i=0
# print("Enter %d numbers"%n)
# while i<n:
#     l6.append(int(input()))
#     i=i+1
# print(l6)
# print("Sum of all the elements in the list is",sum(l6))    


#Script to remove all non int values from a list

# n=int(input("Enter how many elements you want in the list"))
# l7=[]
# i=0
# print("Enter %d list items"%n)
# while i<n:
#     l7.append(eval(input()))
#     i=i+1   
# print(l7)
# i=0 
# l7_new=[]   
                    # by using while loop        
# while i<n:
#     print("is",i)
#     if type(l7[i])==int:
#         l7_new.append(l7[i])
#     i=i+1
                    # by using for loop
# for i in l7:
#     if type(i)==int:
#         l7_new.append(i)                    
# # print(l7_new)   
# l7=l7_new       
# print(l7)        


#Script to print distinct elements along with their frequencies of occurence in the list

# n=int(input("Enter how many elements you want in the list"))
# l8=[]
# i=0
# print("Enter %d list items"%n)
# while i<n:
#     l8.append(eval(input()))
#     i=i+1   
# print(l8)
# i=0
# print()
# while i<n:
#     print(l8[i],l8.count(l8[i]))
#     i=i+1


#Script to print indices of all occurences of a given element ina given list

# l9=[1,2,3,4,1,6,2,8,3,9,4,6,4,2,6,8,9,0,4]
# i=0
# element=int(input("Enter the element whose occurence index you want to check"))
# print("Element is present at these indices\n")
# while i<=18:
#     if l9[i]==element:
#         print(i)
#     i+=1    


#Script to sort a list

# l10=[4,3,7,8,4,5,2,6,86,46,25,75,78,5,632,46,7,1]
# l10.sort()
# print(l10)