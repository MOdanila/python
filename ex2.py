n = int(input("Introduceti nr. : "))
copie = n
invers = 0
while n > 0:
    cifra = n % 10
    invers = invers * 10 + cifra
    n = n // 10
if invers == copie:
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")