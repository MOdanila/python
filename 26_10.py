'''
Sa se scrie un program care sa primeasca
un nr de la tastatura si sa afiseze 
"true" daca e par sau "false" daca e impar
'''
a = int(input("Introduceti nr. : "))
if (a%2==0):
    print("True")
else:
    print("False")

'''
Sa se scrie un program care sa primeasca un nr de la
tastatura si sa afiseze ziua din saptamana care corespunde
numarului introdus
'''
a = int(input("Introduceti nr. : "))
if(a==1):
    print("Monday")
elif(a==2):
    print("Tuesday")
elif(a==3):
    print("Wednesday")
elif(a==4):
    print("Thursday")
elif(a==5):
    print("Friday")
elif(a==6):
    print("Saturday")
elif(a==7):
    print("Sunday")
else:
    print("Error")


'''
Sa se scrie un program care sa primeasca un nr de la
tastatura si sa afiseze numarul de cifre pare ale nr.
'''
a = int(input("Introduceti nr. : "))
c=0

while(a):
    x = a%10
    if(x%2==0):
      c+=1
    a//=10
    
print(c)  
    

