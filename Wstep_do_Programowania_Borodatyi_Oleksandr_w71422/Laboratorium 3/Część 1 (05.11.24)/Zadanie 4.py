# Zadanie 4

import random
import string

# Pobranie danych od użytkownika
n = int(input("Podaj liczbę elementów listy (n): "))
x = int(input("Podaj długość każdego ciągu znaków (x): "))

# Generowanie listy ciągów znaków
lista = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, x))) for _ in range(n)]
print("Wygenerowana lista:", lista)

# Konwersja listy na krotkę
krotka = tuple(lista)
print("Krotka:", krotka)

# a) Ilość znaków w liście
ilosc_znakow = sum(len(ciag) for ciag in lista)
print("Ilość znaków w liście:", ilosc_znakow)

# b) Ilość liter 'k' w liście
ilosc_liter_k = sum(ciag.count('k') for ciag in lista)
print("Ilość liter 'k':", ilosc_liter_k)

# c) Ilość ciągów zawierających 'kt'
ilosc_ciagow_kt = sum('kt' in ciag for ciag in lista)
print("Ilość ciągów zawierających 'kt':", ilosc_ciagow_kt)

# d) Ilość ciągów dłuższych niż s
s = int(input("Podaj wartość s: "))
ilosc_ciagow_dluzszych_niz_s = sum(len(ciag) > s for ciag in lista)
print("Ilość ciągów dłuższych niż", s, ":", ilosc_ciagow_dluzszych_niz_s)
