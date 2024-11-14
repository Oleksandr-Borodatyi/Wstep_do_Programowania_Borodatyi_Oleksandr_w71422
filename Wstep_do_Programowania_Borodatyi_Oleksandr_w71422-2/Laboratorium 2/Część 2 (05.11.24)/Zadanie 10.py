#Zadanie 10

x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj drugą liczbe: "))

if x < y:
    print(f"Pierwsza Liczba: {x}")
    while x < y:
        print(x)
        x = x+1
        if x ==  y:
            print(f"Ostatnia liczba: {y}")
else:
    print(f"Pierwsza Liczba: {y}")
    while y  < x:
        print(y)
        y = y + 1
        if y == x:
            print(f"Ostatnia liczba: {x}")