                            # Strings

#Script to create a string in 3 different ways 

# s1="First way" 
# s2='''Second way'''
# s3=str("Third way")    
# print(s1,s2,s3,sep='\n')                       
# s4=str(123)
# print(s4)


#Script to get the characters from the start to position 5
# (given string "iNeuron" using the slice syntax)

# s="iNeuron"
# print(s[0:6:1])


#Script to get the characters from position 2 to position 5
# (given string "hello learners" using the slice syntax)

# s="hello learners"
# print(s[2:6:1])


#Script to demonstrate string concatination adding space in between
# (given string a="Learning" b="Python")

# a="Learning" 
# b="Python"
# print(a+" "+b)

#Script to get the count of total number of characters in string a="iNeuron"

# a="iNeuron"
# print(len(a))


#Script to reverse a string("iNeuron")

# string="iNeuron"
# print(string[6::-1])

# l=len(string)
# l=l-1
# s=""
# while l>=0:
#     s=s+string[l]    
#     l-=1
# print(s)  
                #   method 2
# while l>=0:
#     print(string[l],end='')
#     l-=1
  

#Script to determine wheather a string contains specific substring

# string=str(input("Enter a string"))
# substring=str(input("Enter the substring you want to check"))
# if substring in string:
#     print("Substring found")
# else:
#     print("SUbstring not found")    


#Script to check if a string contains only numbers

# s=str(input("Enter a string"))
# print(s.isdigit())


#Script to check if a string contains only characters of the alphabet

# s=str(input("Enter a string"))
# print(s.isalpha())


#Script to convert an integer to a string

# n=int(input("Enter a number"))
# print(n)
# print(type(n))
# s=str(n)
# print(s,type(s))
