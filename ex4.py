while(True):
    print("1. Adunare")
    print("2. Scadere")
    print("3. Inmultire")
    print("4. Impartire")
    print("5. Iesire")
    print("Alegeti o optiune: ")
    optiune = input()
    if optiune == "1":
        print("Adunare")
        print("Introduceti primul numar: ")
        a = int(input())
        print("Introduceti al doilea numar: ")
        b = int(input())
        print(a+b)
    elif optiune == "2":
        print("Scadere")
        print("Introduceti primul numar: ")
        a = int(input())    
        print("Introduceti al doilea numar: ")
        b = int(input())
        print(a-b)
    elif optiune == "3":
        print("Inmultire")
        print("Introduceti primul numar: ")
        a = int(input())
        print("Introduceti al doilea numar: ")
        b = int(input())
        print(a*b)
    elif optiune == "4":
        print("Impartire")
        print("Introduceti primul numar: ")
        a = int(input())
        print("Introduceti al doilea numar: ")
        b = int(input())
        print(a/b)
    elif optiune == "5":
        print("Iesire")
        break
    else:
        print("Optiune invalida")