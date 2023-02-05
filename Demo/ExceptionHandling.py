a=8
# b=1
# c=0
# b = eval(input("Enter a number"))
# c = a/b

try:
    b = int(input("Enter a number"))
    if a == b:
        raise ArithmeticError
    c = a/b

except ZeroDivisionError:
    print("you cannot divide by Zero")
except ValueError:
    print("Tumhe number enter krna tha")
except ArithmeticError:
    print("Maine Raise kiya h Arithmetic Error")        

except Exception:
    print("Error hai check kro")
else:
    print(c)
finally:
    print("Error aye ya na aye finally block toh chalta hi hai")