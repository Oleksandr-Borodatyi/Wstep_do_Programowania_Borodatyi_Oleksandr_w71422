#Zadanie 10

import numpy as np

# Tworzenie listy z potęgami liczby 2
potegi_2 = [128, 64, 32, 16, 8, 4, 2, 1]

# Tworzenie tablicy ndarray o nazwie wagi
wagi = np.array(potegi_2)

# Tworzenie losowej tablicy ndarray o nazwie liczba_bin
liczba_bin = np.random.randint(0, 2, size=8)

# Definicja funkcji obliczającej wartość liczby binarnej
def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

# Test funkcji
wartosc = wartosc_liczby_bin(wagi, liczba_bin)
print("Tablica wagi:", wagi)
print("Tablica liczba_bin:", liczba_bin)
print("Wartość liczby binarnej:", wartosc)

