def  rectangle(arg):
    if(arg=="rectangle"):
        return True
    else:
        return False
    
def rectArea(a,b):
    print("The area of the rectangle is: ")
    return a*b

def rectPer(a,b):
    print("The perimeter of the rectangle is: ")
    return 2*(a+b)

a = str(input("Enter the shape you want: "))

if(rectangle(a)):
    x = int(input("Enter the length of the rectangle: "))
    y = int(input("Enter the width of the rectangle: "))
    z = str(input("What do you want to calculate: area or perimeter?"))
    if(z=="area"):
        print(rectArea(x,y))
    else:
        print(rectPer(x,y))
    