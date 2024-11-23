import math
def square(a):
    return a **2
def rad(a):
    return math.sqrt(a)
def triple(a):
    return a * 3
def sum(a,b):
    return a + b
def numitor(a):
    return sum(square(a),square(square(a)))+rad(a)
x = int(input("Enter the number you want to calculate the equation for: "))
print(f"The result of the equation is: {triple(sum(square(x),square(x**2)))/(sum(square(x),square(x**2))+rad(sum(square(x),square(x**2))))+rad(sum(square(x),square(square(x))))}")