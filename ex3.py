min = 1000000000000
max = -1000000000000
n = int(input("Introduceti nr. de elemente din lista: "))
for i in range(n):
    x = int(input())
    if x > max:
        max = x
    if x < min:
        min = x
print("Nr. minim: ", min)
print("Nr. maxim: ", max)