#Zadanie 2

    #a
# Kwadra z gwiazdek
liczba_rzędów = int(input("Wprowadź liczbę rzędów dla kwadratu: "))

for _ in range(liczba_rzędów):
    print("* " * liczba_rzędów)  # Wydrukuj rząd gwiazdek


    #b
# Prostokątny trójkąt z hipotenuzą po prawej stronie
liczba_rzędów = int(input("Wprowadź liczbę rzędów dla trójkąta: "))

for i in range(liczba_rzędów):
    # Dodaj spacje na początku wiersza, aby wyśrodkować trójkąt
    print(" " * (liczba_rzędów - i - 1) + "* " * (i + 1))  # Wydrukuj spacje i gwiazdki


    #c
# Równoboczny trójkąt (choinka)
liczba_rzędów = int(input("Wprowadź liczbę rzędów dla choinki: "))

for i in range(liczba_rzędów):
    # Dodaj spacje na początku wiersza, aby wyśrodkować choinkę
    print(" " * (liczba_rzędów - i - 1) + "* " * (2 * i + 1))  # Wydrukuj spacje i gwiazdki
