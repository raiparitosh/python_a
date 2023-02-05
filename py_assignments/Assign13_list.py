                             # List

#Script to store multiple items in a single variable(items are "java","python","SQL","C") using list

# l1=["Java","Python","SQL","C"]
# print(l1)


#Script to get the data type of a list

# print(type(l1))


#Script to get the last item of the list(mylist=["Java","C","Python"])

# mylist=["Java","C","Python"]
# print(mylist[-1])
# print(mylist[2])


#Script to change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter"
# (list is thislist=["Java","SQL","C","Reactnative","Javascript","Python"])

# thislist=["Java","SQL","C","Reactnative","Javascript","Python"]
# thislist[1]="NoSQL"
# thislist[3]="Flutter"
# print(thislist)


#Script to add an item to the end of the list (item "Python".(mylist=["Java","SQL","C","Reactnative"]))

# mylist=["Java","SQL","C","Reactnative"]
# print(mylist)
# mylist.append("python")
# print(mylist)


#Program to append elements from another list to the current list.
# (firstlist=["Java","Python","SQL"]
#   secondlist=["C","CPP","NoSQL"])

# firstlist=["Java","Python","SQL"]
# secondlist=["C","CPP","NoSQL"]
# firstlist+=secondlist
# print(firstlist)


#Program to print all items by reffering to their index number
# (thislist=["Java","SQL","C","Reactnative","Javascript","Python"])

# thislist=["Java","SQL","C","Reactnative","Javascript","Python"]
# index=0
# while index<6:
#     print(thislist[index])
#     index+=1


#Program to sort the list alphanumerically - thislist=["Java","SQL","C",
# "Reactjs","Javascript","Python"]

# thislist=["Java","SQL","C","Reactjs","Javascript","Python"]
# print(sorted(thislist))
# thislist.sort()
# print(thislist)
 

 #Script to create a list of city names taken from the user

# l9=input("Enter city names seperated by space").split(' ')
# print(l9)
                   #Method 2
# n=int(input("How many cities you want to enter"))
# print("Enter %d city names"%n)
# citylist=[]
# i=0
# while i<n:
#     citylist.append(input())
#     i+=1
# print(citylist)    


#Script to create a list, where each element of the list is a digit of a given number

n=int(input("Enter a number"))
l1=[]
while n>0:
    l1.append(n%10)
    n=n//10
print(l1)    
