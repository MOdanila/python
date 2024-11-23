n = int(input("Introduceti nr. elementelor din lista: "))
lista = []
pare=0
impare=0
for i in range(n):
    x = int(input())
    lista.append(x)
    if x % 2 == 0:
        pare+=1
    else:
        impare+=1

print("Nr. de elemente pare: ", pare)
print("Nr. de elemente impare: ", impare)