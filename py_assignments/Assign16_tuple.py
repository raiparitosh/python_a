                    # tuple

#Script to store multiple items in a single variable using tuple.
#  (items are "Java","Python","SQL","C")

# i=("Java","Python","SQL","C")
# print(i)
# print(type(i))


#Program to store only one item using tuple

# i=eval(input("Enter an item"))
# t=(i,)
# print(t)
# print(type(t))


#Program to reverse the tuple

# t1=([eval(e) for e in input("Enter items seperated by comma").split(',')])
# l=len(t1)
# print(l,t1)
# t2=[]
# while l-1>=0:
#     t2.append(t1[l-1]) 
#     l-=1
# print(t2)     
# print(tuple(t2))   


#Program to swap two tuples in python







#Program to check if all items in the tuple are same or not

# t3=tuple([eval(e) for e in input("Enter values seperated by comma").split(',')])
# print(t3)
# l=len(t3)
# i=0   
# while i<l-2:
#     if t3[i]!=t3[i+1]:
#         break
#     i+=1
# if i==l-2:
#     print("All items in the tuple are same")
# else:
#     print("tuple elements are not same") 


#Program to divide the tuple into 4 variables.
# tuple1=(100,200,300,400)

# tuple1=(100,200,300,400)

# fisrt_variable=tuple1[0]
# second_variable=tuple1[1]
# third_variable=tuple1[2]
# forth_variable=tuple1[3]
# print(fisrt_variable,second_variable,third_variable,forth_variable,sep='--')
# print(tuple1)


#Program to copy elements 4 and 5 from the following tuple into a new tuple.
# tuple1=(1,2,3,4,5,6)

# tuple1=(1,2,3,4,5,6)
# new_tuple=()

# new_tuple=new_tuple + tuple1[3:5]                 #by slicing operator
# print(new_tuple)

# new_tuple=tuple1[3]
# # new_tuple=tuple1[4]                          #for beginner
# print(new_tuple)

# tuple1=list(tuple1)
# print(tuple1)
# new_tuple.append(tuple1[3])            
# new_tuple.append(tuple1[4])
# print(new_tuple)
# print(tuple(new_tuple))


#Program to sort a tuple of tuple  by the second item.
# tuple1=(('a',21),('b',37),('c',11),('d',29))

# t1=(('a',21),('b',37),('c',11),('d',29))
# l1=list(t1)
# j=1
# for e in range(0,len(l1)-1):
#     for i in range(0,len(l1)-1):
#         if l1[i][j]>l1[i+1][j]:
#             l1[i],l1[i+1]=l1[i+1],l1[i]
# print(tuple(l1))    


#WAP to print the value 20 from given nested tuple. tuple1=("python",[10,20,30],(2,4,6))

# tuple1=("Python",[10,20,30],(2,4,6))

# for i in range(len(tuple1)):
#     if type(tuple1[i])==list:
#         for j in range(len(tuple1[i])):
#             if tuple1[i][j]==20:
#                 print(tuple1[i][j])

# tuple1=("Python",[10,20,30],(2,4,6))
# i=0
# # print(tuple1[1][1])
# while i<3:
#     if i==1:
#         print(tuple1[i][i])
#     i+=1     

#WAP to change the first item (22) of a list within the following tuple to 222.

# tuple1=(11,[22,33],44,55)
# print(type(tuple1))      
    #you cannot make any change in tuple but here tuple object is of list 
              #type thatswhy we are able to change the value  
#lekin isme doubt h abhi jisko clear krna h
                                                                                      
# for i in range(len(tuple1)):
#     if i==1:
#         for j in range(len(tuple1[i])):
#             if tuple1[i][j]==22:
#                 tuple1[i][j]=222
# print(type(tuple1),tuple1)               



