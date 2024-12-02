# Zadanie 17

def wyswietl_parametry(*args):
    
    for parametr in args:
        print(parametr)

dane = input("Podaj liczby oddzielone przecinkami: ")

lista_liczb = [int(x) for x in dane.split(",")]

wyswietl_parametry(*lista_liczb)

#============================================================#

def max_parametr(*args):
    """
    Funkcja znajduje i zwraca wartość maksymalną spośród przekazanych parametrów.
    """
    if args: 
        return max(args)
    else:
        return None


dane = input("Podaj liczby oddzielone przecinkami: ")

lista_liczb = [int(x) for x in dane.split(",")]

maksimum = max_parametr(*lista_liczb)
if maksimum is not None:
    print(f"Maksymalna liczba to: {maksimum}")
else:
    print("Nie podano żadnych liczb.")