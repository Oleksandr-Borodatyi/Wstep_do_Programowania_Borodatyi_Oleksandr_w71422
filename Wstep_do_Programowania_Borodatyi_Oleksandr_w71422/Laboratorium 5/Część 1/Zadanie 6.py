# Zadanie 6 

import math
import keyword

def wyswietl_funkcje(modul):

    funkcje = dir(modul)
    print(f"Funkcje i atrybuty w module '{modul.__name__}':")
    for funkcja in funkcje:
        print(f" - {funkcja}")
    print("\n")

wyswietl_funkcje(math)
wyswietl_funkcje(keyword)

print("Moduł 'tuple' nie jest zewnętrznym modułem, to wbudowany typ danych w Python.\n")
print("Dostępne metody dla tuple:")
print(dir(tuple))
