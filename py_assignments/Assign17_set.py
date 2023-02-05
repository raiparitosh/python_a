                    
                                       #set 

#Python program to store all the programming laguages known to you

# s=input("Enter programming languages knoen to you separated by comma")
# s={eval(e) for e in s.split(',')}
# print(s)


#Python program to store your own information in a set.{name,age,gender,so on}

# s2={eval(e) for e in input("Enter your details seperated by comma").split(',')}    #set comprehension
# print(s2)                   
            # yha hmne for loop isliye use kiya h kyuki split() list of str type object return krta h or 
            # hme user se diff. datatypes k object input lena pad skta h, fir unko typecast kiya h eval()se       

# s2=set(input("Enter your details seperated by comma").split(','))
# print(s2)


#Python script to get the datatype of a set

# s3={1,2,4.5,"paritosh",True,6+7j}
# print(s3)
# print(type(s3))

#python script to find if "python" is present in the set.
# thisset={"Java","Python","SQL"}

# thisset={"Java","Python","SQL"}
# for element in thisset:
#     if element == "Python":
#         print("{} is present in the set".format("Pyhton"))
#         break    
# else:
#     print("{} is not present in the set".format("Python"))    


#Python program to add items from another set to the current set.
#thisset={"Python","Django","JavaScript"}
#secondset={"C","CPP","NoSQL"}

# thisset={"Python","Django","JavaScript"}
# secondset={"C","CPP","NoSQL"}
# print(thisset.union(secondset))

# currentset=thisset.union(secondset)
# print(currentset)


#Python program to add elements of a list to a set
#thisset={"Python","Django","JavaScript"}
#mylist=["Java","C"]

# thisset={"Python","Django","JavaScript"}
# print(thisset)
# mylist=["Java","C"]
# thisset.update(mylist)
# print(thisset)


#Python program to remove last item of the given set.
# thisset={"Python","Django","JavaScript","SQL"}

# thisset={"Python","Django","JavaScript","SQL"}
# thisset_new=set()
# for e in thisset:
#     if e=="Python" or e=="Django" or e=="JavaScript":
#         # print(e)
#         thisset_new.add(e)
#     # print(e)
# print(thisset)  
# print(thisset_new)  


#Python program to delete the set completely

# s8={1,2,3,4}
# s8.clear()     #set ko empty kiya
# print(s8)
# del(s8)       #delete kiya
# print(s8)   #delete krne k baad print nhi chalega


#Python program to loop through the set and print values
# thisset={"Python","Django","JavaScript","SQL"}

# thisset={"Python","Django","JavaScript","SQL"}
# for i in thisset:
#     print(i)

#Python program to find the minimum and maximum value in a set

# s10={int(element) for element in input("Enter numbers seperated by comma").split(',')}
# maxvalue=0
# minvalue=1000000
# for e in s10:
#     if e>maxvalue:
#         maxvalue=e  
         
#     if e<minvalue:
#         minvalue=e  
# print("Maximum Value in the set is {}".format(maxvalue))
# print("Minimum value in the set is {}".format(minvalue))        

# print(max(s10),min(s10))    #using built-in functions