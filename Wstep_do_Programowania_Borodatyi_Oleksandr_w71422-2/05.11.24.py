"""While 05.11.24
Laboratorium 2
Część 2"""

""" Przykład
x = 3
while x < 5:
    print(f"x:{x}")
"""
# Zadanie 8

'''x=-4
while x <= 4:
    y = 2*x*x - 5*x - 8
    print(f'Dla x= {x}, wartośćfunkcji wynosi {y}')
    x+=0.5'''

#Zadanie 9
'''while True:
    liczba = int(input("Podaj liczba całkowita: "))
    if liczba < 0:
        print("wychdzę z pętli")
        break'''

#Zadanie 10

'''x = int(input("Podaj pierwsza liczbe: "))
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
            print(f"Ostatnia liczba: {x}")'''

#Zadanie 11

x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj drugą liczbe: "))

if x < y:
    print(f"Pierwsza Liczba: {x}")
    while x < y:
        if x%2 == 0:
            print(x)
            if x == y:
                print(f"Ostatnia liczba: {y}")
        x = x + 1
        continue

else:
    print(f"Pierwsza Liczba: {y}")
    while y  < x:
        if y%2 == 0:
            print(y)
            if y == x:
                print(f"Ostatnia liczba: {x}")
        y = y + 1
        continue