#Vectori
#listaNr = [1, 2, 3, 4, 5]
#sintaxa range: range(start, stop, step)
'''
for x in listaNr:
    print(x)

for i in range(1, 11, 2):
    print(i)
'''

'''
Sa se scrie un program care sa primeasca un nr de la 
tastatura si, ulterior, sa il caute intr-o lista.
'''
'''
listaNr = [8, 3, 17, 13, 100, 20, 32]
a = int(input("Introduceti nr. : "))
b = False
for x in listaNr:
    if x==a:
        b = True
        break
    else:
        continue
    
if b==True:
    print("Nr. se afla in lista")
else:
    print("Nr. nu se afla in lista")
'''
listaNr = []
a = int(input("Introduceti nr. de elemente de adaugat in lista:"))
for i in range(0,a):
    b = int(input())
    listaNr.append(b)
c = int(input("Introduceti nr. de cautat in lista:"))
d = False
for x in range(len(listaNr)):
    if listaNr[x]==c:
        d=True
        break
    else:
        continue
if d==True:
    print("Nr. se afla in lista")
else:
    print("Nr. nu se afla in lista")  