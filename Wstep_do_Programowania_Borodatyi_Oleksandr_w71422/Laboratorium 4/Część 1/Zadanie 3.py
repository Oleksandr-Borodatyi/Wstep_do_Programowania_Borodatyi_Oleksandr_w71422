# Zadanie 3

def liczba_dodania_lub_ujemna(liczba):
    if liczba < 0:
        print(f"Liczba jest ujemna: { liczba }")
    elif liczba == 0:
        print(f"Liczba jest równą 0")
    else:
        print(f"Liczba jest dodatną: {liczba}")
liczba_dodania_lub_ujemna(int(input("Wprowadż liczbę: ")))