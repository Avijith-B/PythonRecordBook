def Triangle():
    a,b,c=(input(("please enter the length of the sides seperated by commas in acending order")).split(","))
    a=int(a)
    b=int(b)
    c=int(c)
    if a==b and b==c:
        print("The triangle is Equilateral")
    elif a ==b or b==c or c==a:
        print("The triangle is an isoseles triangle")
    else:
        print("The triangle is scalene")
# Triangle()
    
def PositiveOrNegetive():
    n = int(input("Enter the INTEGER: "))    
    if n>0:
        print(f"{n} is positive")
    else:
        print(f"{n} is negetive")
# PositiveOrNegetive()

def OddOrEven():
    n = int(input("Enter the number: "))
    if n%2==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
# OddOrEven()

def Quadratic():
    a,b,c = input("Enter the values of a,b,c in ax^2 + bx + c, seperated by commas ").split(",")
    a=int(a)
    b=int(b)
    c=int(c)
    if (b**2)-4*(a*c) < 0:
        print("Roots are Imaginary")
    else:
        Root1 =( -(b) + ((b**2 - 4*a*c))**(1/2) )/(2*a)
        Root2 =( -(b) - ((b**2 - 4*a*c))**(1/2) )/(2*a)
        print(f"Root 1 = {Root1}, Root2 = {Root2}")
# Quadratic()
