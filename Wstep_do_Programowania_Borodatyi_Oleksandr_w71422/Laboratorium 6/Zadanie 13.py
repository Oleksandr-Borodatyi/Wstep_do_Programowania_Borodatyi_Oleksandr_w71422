#Zadanie 13

import numpy as np

# Tworzenie macierzy 5x5 wypełnionej zerami
macierz = np.zeros((5, 5), dtype=int)

# Ustawianie jedynek na brzegach
macierz[0, :] = 1  # Góra
macierz[-1, :] = 1  # Dół
macierz[:, 0] = 1  # Lewo
macierz[:, -1] = 1  # Prawo

def zamien_zera_na_jedynki_i_odwrotnie(macierz):
    """Funkcja zamienia zera na jedynki i jedynki na zera w podanej macierzy."""
    return 1 - macierz

# Wynik pierwotnej macierzy
print("Macierz z jedynkami na brzegach:")
print(macierz)

# Zmieniona macierz
odwrocona_macierz = zamien_zera_na_jedynki_i_odwrotnie(macierz)
print("Macierz po zamianie zer na jedynki i odwrotnie:")
print(odwrocona_macierz)
