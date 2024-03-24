print("jaldi jaldi kro toshu")
# marks=float(input("Enter the marks of the student"))
# if 90<marks<=100:
#     print("A Grade")
# elif 80<marks<=90:
#     print("B Grade")
# elif 70<marks<=80:
#     print("C Grade")
# elif 60<marks<=70:
#     print("D Grade")
# elif 50<=marks<=60:
#     print("E Grade")
# else:
#     print("Fail")

# x=int(input("Enter a number"))
# print("Positive" if x>0 else "Non Positive")

a = 54321

rev = 0

while(a!=0):
    rem = a % 10
    rev = rev * 10 + rem
    a = a//10

print(rev)