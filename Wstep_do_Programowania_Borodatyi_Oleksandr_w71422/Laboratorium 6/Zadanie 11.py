# Zadanie 11

import numpy as np

# Tworzenie losowej macierzy 5x5
macierz = np.random.randint(1, 101, size=(5, 5))

# Znajdowanie najmniejszego i największego elementu
najmniejszy = np.min(macierz)
największy = np.max(macierz)

# Największe elementy w każdym wierszu (axis=1) i w każdym z kolumn (axis=0)
najwieksze_w_wierszach = np.max(macierz, axis=1)
najwieksze_w_kolumnach = np.max(macierz, axis=0)

# Suma wartości w poszczególnych wierszach
suma_w_wierszach = np.sum(macierz, axis=1)

# Wyniki
print("Macierz:\n", macierz)
print("Najmniejszy element:", najmniejszy)
print("Największy element:", największy)
print("Największe elementy w wierszach:", najwieksze_w_wierszach)
print("Największe elementy w kolumnach:", najwieksze_w_kolumnach)
print("Suma wartości w wierszach:", suma_w_wierszach)
