#Zadanie 11

x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj drugą liczbe: "))

if x < y:
    print(f"Pierwsza Liczba: {x}")
    while x < y:
        if x%2 == 0:
            print(x)
        x = x + 1
        if x == y:
                print(f"Ostatnia liczba: {y}")
        continue

else:
    print(f"Pierwsza Liczba: {y}")
    while y  < x:
        if y%2 == 0:
            print(y)
        y = y + 1
        if y == x:
                print(f"Ostatnia liczba: {x}")
        continue