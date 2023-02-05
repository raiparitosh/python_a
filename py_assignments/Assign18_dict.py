
                          #dict

d={1:"paritosh rai",2:"toshu",3:"papaji",4:"Maa",5:"didi"}
# print(d)


# print(d[4])

# for key in d:
    # print(d[key])

# for key in d:                 
#     print(key,d[key])    

                  #edit dict element
# d[2]="toshu rai"
# print(d)

# d[2]=("tomo","pranjal")
# print(d)

                 #add new element in dict
# d[6]="pta ni kha hogi"
# print(d)

# sample_dict={'C':92,'Java':66,'Python':85}
# print(sample_dict.items())
# print(sample_dict.keys())
# print(sample_dict.values()) 
# s_d=sorted(sample_dict.values())
# print(min(sample_dict.keys()))
# print(s_d)



#Program to create and print a dictionary which stores your information.(name, age, gender....)

# n=int(input("Enter how many data you want to store"))
# d1={}
# for key in range(n):
#     key=eval(input("Enter key value "))
#     data=eval(input("Enter your details "))
#     d1[key]=data
# print(d1)    


#Program to access the items of a dictionary by reffering to its key name

# d2={1:"paritosh rai",2:"toshu",3:"papaji",4:"Maa",5:"didi"}
# for key in d2:
#     print(d2[key])


#Python program to get the list of the values from a dictionary

# d3={1:"paritosh rai",2:"toshu"}
# print(d3.items())


#Python program to change the value of a specific item by refering to its key name

# n=int(input("Enter how many items you want in the dictionary"))
# d4={}
# k=eval(input("Enter the key value whose data you want to change"))
# new_data=eval(input("Enter the data to be updated"))
# for key in range(n):
#     key=eval(input("Enter key value"))
#     data=eval(input("Enter data value"))
#     d4[key]=data
# print(d4)    

# for ke in d4:
#     if ke==k:
#         d4[ke]=new_data
#         break
# else:
#     print("Not found the key whose data you want to change ") 
# print(d4)    


#Python program to print all key names in the dictionary, one by one
 
# d5={1:"paritosh rai",2:"toshu",3:"papaji",4:"Maa",5:"didi"}
# for key in d2:
#     print(key)


#Program to convert two lists into a dictionary in a way that 
# item from list1 is the key and item from list2 is the value
                    #   Method 1
# l2_counter=1
# l1_iterator=1
# for k in l1:
#     l2_counter=1
#     for i in l2: 
#         if l2_counter==l1_iterator:
#             d8[k]=i
#             break
#         l2_counter+=1
#     l1_iterator+=1    
# print(d8)   
#                     #  Method 2
# d8={}
# l1=[1,2,3,4]
# l2=["paritosh","rai","toshu","pranjal"]
# d8={l1[i]:l2[i] for i in range(len(l1))}
# print(d8)

#Program to merge two python dictonaries in one dictionary

# dict_1={1:"Ballia",2:"Banaras",3:"Lucknow",4:"Jaipur"}
# dict_2={5:"Uttar Pradesh",6:"Rajasthan"}
# dict_1.update(dict_2) 
# print(dict_1)

#Program to get the key of lowest value from the dictionary.
# sample_dict={'C':92,'Java':66,'Python':85}

# sample_dict={'C':92,'Java':66,'Python':85}
# j=min(sample_dict.values())
# for i in sample_dict:
#     if sample_dict[i]==j:
#         print(i)
