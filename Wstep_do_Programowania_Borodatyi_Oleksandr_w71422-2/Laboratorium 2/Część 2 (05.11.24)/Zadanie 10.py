#Zadanie 10

x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj drugą liczbe: "))

if x < y:
    print(f"Pierwsza Liczba: {x}")
    while x <= y:
        print(x)
        if x ==  y:
            print(f"Ostatnia liczba: {y}")
        x = x+1
else:
    print(f"Pierwsza Liczba: {y}")
    while y  <= x:
        print(y)
        if y == x:
            print(f"Ostatnia liczba: {x}")
        y = y + 1