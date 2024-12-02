# Zadanie 6

# Zdefiniowanie łańcucha tekstowego
tresc = "Python jest super"

# a) Wyświetlenie znaku o indeksie zerowym
zerowy_indeks = tresc[0]
print("Znak o indeksie zerowym:", zerowy_indeks)

# b) Wyświetlenie znaku o indeksie ostatnim
ostatni_indeks = tresc[-1]
print("Znak o ostatnim indeksie:", ostatni_indeks)

# c) Wyświetlenie co drugiego znaku, zaczynając od zerowego
co_drugi_znak = tresc[0::2]
print("Co drugi znak, zaczynając od zerowego:", co_drugi_znak)

# d) Wyświetlenie co trzeciego znaku, zaczynając od pierwszego
co_trzeci_znak = tresc[1::3]
print("Co trzeci znak, zaczynając od pierwszego:", co_trzeci_znak)

# e) Wyświetlenie od dziesiątego do ostatniego
od_dziesiatego = tresc[9:]
print("Znaki od dziesiątego do ostatniego:", od_dziesiatego)

# f) Wyświetlenie od końca do początku
od_konca_do_poczatku = tresc[::-1]
print("Od końca do początku:", od_konca_do_poczatku)
