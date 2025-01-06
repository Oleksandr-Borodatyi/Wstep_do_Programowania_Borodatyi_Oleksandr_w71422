# Zadanie 12

import numpy as np

# Tworzenie tablicy 3x3 wypełnionej zerami
tablica = np.zeros((3, 3), dtype=int)

# Wypełnianie zaznaczonych obszarów jedynkami
tablica[0, :] = 1  # Pierwszy wiersz

# Wynik
print("Tablica 3x3:")
print(tablica)